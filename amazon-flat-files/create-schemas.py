#!/usr/bin/python3

import re
import os.path
import sys
import glob
import pandas as pd
import json
from type_dict import type_dict
from number_dict import number_dict

sys.path.append("/omark/pydb")
import dbconn

## hooray globals;; will refactor this mess...
EXCEL_FILES = set()
SCHEMA_NAMES = set()
EXCEL_SCHEMA_MAP = {}

def create_build_schema():
    dbconn.cur.execute(
        """
        create schema if not exists build;
        """)

def create_schema_helper():
    dbconn.cur.execute(
        """
        create or replace function build.create_schemas
                  (schema_list varchar[])
        returns void
        as
        $$
        declare
        s varchar;

        begin

        foreach s in array schema_list
        loop
	execute format('CREATE SCHEMA IF NOT EXISTS %I', s);
        end loop;

        end;
        $$ language plpgsql;
        """)

def create_template_tables_helper():
    dbconn.cur.execute(
        """
        create or replace function build.create_template_tables
                  (schema_list varchar[])
        returns void
        as
        $$
        declare
        s varchar;

        begin

        foreach s in array schema_list
        loop
	     execute format('
             CREATE TABLE IF NOT EXISTS %I.template ();
             ', s);
        end loop;

        end;
        $$ language plpgsql;
        """)


def create_valid_tables_helper():
    dbconn.cur.execute(
        """
        create or replace function build.create_valid_tables
	      (schema_name varchar, tbls varchar[])
        returns void
        as
        $$
        declare
        t varchar;

        begin
        foreach t in array tbls
        loop
	    execute format('
            CREATE TABLE IF NOT EXISTS %1$I.valid_%2$I (
			%2$I VARCHAR PRIMARY KEY
            );', schema_name, t);
        end loop;

        end;
        $$ language plpgsql;
        """)


def add_column_to_template_helper():
    dbconn.cur.execute(
        """
create or replace function build.add_columns_to_tamplate_tables
	(schema_name varchar, column_array varchar[], data_type varchar, optional varchar)
returns void
as
$$
declare
cname varchar;
t_data_type varchar := substring(data_type, '\w+');

t_varchar_n varchar;
t_numeric_first int;
t_numeric_stage varchar;
t_numeric_second int;


begin
if t_data_type = 'varchar'
then
t_varchar_n := substring(data_type, '\d+');
end if;

if t_data_type = 'numeric'
then
t_numeric_first := substring(data_type, '\d+')::int;
t_numeric_stage := substring(data_type, '\d+\)');
t_numeric_second := substring(t_numeric_stage, '\d+')::int;
end if;


foreach cname in array column_array
loop
	if not exists
		(select *
		 from information_schema.columns
		 where (table_schema, table_name, column_name) 
		      = (schema_name, 'template', cname))
	then
	if t_data_type = 'int'
	then 
		execute format('
			alter table %1$I.template
			add column %2$I integer not null;',
			schema_name, cname, t_data_type);
	
	elsif t_data_type = 'numeric'
	then 
		execute format('
			alter table %1$I.template
			add column %2$I %3$I(%4$I, %5$I) not null;',
			schema_name, cname, t_data_type, t_numeric_first::int, t_numeric_second::int);

	elsif t_varchar_n is not null
	then
		execute format('
			alter table %1$I.template
			add column %2$I %3$I(%4$I) not null;',
			schema_name, cname, t_data_type, t_varchar_n);
        else 
		execute format('
			alter table %1$I.template
			add column %2$I %3$I not null;',
			schema_name, cname, t_data_type);
	end if;
end if;
end loop;	
end;
$$ language plpgsql;
""")

def create_helper_functions():
    print('building schemas')
    create_build_schema()
    create_schema_helper()
    create_template_tables_helper()
    create_valid_tables_helper()
    add_column_to_template_helper()
# def drop_helper_functions():
#     dbconn.cur.execute(
#         """
#         drop function create_template_tables(varchar[]);
#         """)

#     dbconn.cur.execute(
#         """
#         drop function create_schemas(varchar[]);
#         """)

def camel_to_underscore(name):
    name = re.sub('-', '_', name)
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    name = re.sub('__', '_', name)
    name = name.lower()
    return name

##
def read_excel_files():
    print('reading excel files')
    us = "us/"
    for xfile in glob.glob(os.path.join(us, "*.*")):
        xfile = re.sub('us/', '', xfile)
        yield xfile

def populate_excel_file_list():
    print('populating excel files set')
    for f in read_excel_files():
        EXCEL_FILES.add(f)

def generate_schema_name(xfile):
        junk, sep, name = xfile.partition("Flat.File.")
        final_name, dot, xl = name.partition(".")
        underscore_name = camel_to_underscore(final_name)
        trimmed_name = underscore_name.strip()
        schema_name = "amazon_{0}".format(underscore_name)
        if schema_name not in ["amazon_inventory_loader",
                               "amazon_price_inventory"]:
            return schema_name

def populate_schema_name_list():
    print('populating schema set')
    for f in EXCEL_FILES:
        sn = generate_schema_name(f)
        if sn:
            SCHEMA_NAMES.add(sn)
            EXCEL_SCHEMA_MAP[f] = sn

## create schemas
def create_schemas():
    sn = list(SCHEMA_NAMES)
    dbconn.cur.execute(
        """
        select create_schemas(array{0});
        """.format(sn))

def create_table_name(s):
    return camel_to_underscore(s)

def create_valid_tables(schema_name, tbl_list):
    print('creating valid tables')
    dbconn.cur.execute(
        """
        select create_valid_tables('{0}', array{1});
        """.format(schema_name, tbl_list))

def create_template_tables():
    print('creating template tables')
    sn = list(SCHEMA_NAMES)
    dbconn.cur.execute(
        """
        select create_template_tables(array{0});
        """.format(sn))

def update_template_table(schema_name, column_name, data_type, optional):
    print(schema_name, column_name, data_type, optional)
    column_list = number_dict.get(column_name, [column_name])
    if optional == "Required":
        try:
            dbconn.cur.execute(
                """
            select build.add_columns_to_tamplate_tables
            ('{0}', array {1}, '{2}', '{3}');
            """.format(schema_name, column_list, data_type, optional))
        except Excepption as e:
            print(e)
            
def insert_valid_values(schema_name, table_name, value_list):
    print('inserting valid values')
    for v in value_list:
        if str(v) != 'nan':
            try:
                dbconn.cur.execute(
                    """
                    begin;
                    insert into {0}.valid_{1} ({1})
                    select $${2}$$
                    where not exists
                        (select *
                         from {0}.valid_{1}
                         where {1} = $${2}$$);
                    commit;
                    """.format(schema_name, table_name, v))
            except:
                print(schema_name, table_name, v)

def pg_to_tables(schema_name, pg_df):
    tbl_list = []
    pg_cols = list(pg_df.columns)
    for tbl in pg_cols:
        tbl = re.sub('-', '_', tbl)
        if " " not in tbl:
            tbl_list.append(tbl)
            create_valid_tables(schema_name, tbl_list)

def insert_pg_vals(schema_name, pg_df):
    pg_vals = pg_df.to_dict('list')
    for col, val in pg_vals.items():
        col = create_table_name(col)
        insert_valid_values(schema_name, col, val)

def create_tables():
    for xfile, schema_name in EXCEL_SCHEMA_MAP.items():
        xpath_file = pd.ExcelFile(os.path.join("us/", xfile))

        try:
            #pg meaning "excel_page"
            #df meaning "DataFrame"
            pg = pd.read_excel(xpath_file,
                               sheetname = "Valid Values")
            pg_df = pd.DataFrame(pg)
        except:
            pass

        if schema_name in ["amazon_food_service_and_jan_san",
                           "amazon_food_service_and_jan_san_lite"]:

            pg_to_tables(schema_name, pg_df)
            insert_pg_vals(schema_name, pg_df)

        elif schema_name:
            pg_df.columns = pg_df.iloc[0]
            pg_df = pg_df.reindex(pg_df.index.drop(0))

            pg_to_tables(schema_name, pg_df)
            insert_pg_vals(schema_name, pg_df)

def get_stuff():
    for xfile, schema_name in EXCEL_SCHEMA_MAP.items():
        xpath_file = pd.ExcelFile(os.path.join("us/", xfile))
        data_defs = pd.read_excel(xpath_file,
                                  sheetname = "Data Definitions")

        pg_df = pd.DataFrame(data_defs)
        pg_df.columns = pg_df.iloc[0]
        pg_df = pg_df.reindex(pg_df.index.drop(0))
        pg_json = (pg_df.to_json(orient = 'records'))
        js = json.loads(pg_json)
        if schema_name:
                for i in js:
                    if i["Field Name"]:
                        fn = i["Field Name"]
                        ff = i["Accepted Values"]
                        if ff:
                            data_type = type_dict[ff]
                            r = i["Required?"]
                            update_template_table(schema_name, fn, data_type, r)

create_helper_functions()

populate_excel_file_list()
populate_schema_name_list()

# create_schemas()
# create_template_tables()
# create_tables()

get_stuff()

#drop_helper_functions()

#print(type_dict)

dbconn.conn.commit()
dbconn.cur.close()

print("done")
