#!/usr/bin/python3

import re
import os.path
import sys
import glob
import pandas as pd
import json
from type_dict import type_dict

sys.path.append("/omark/pydb")
import dbconn


## some auxilary functions
def read_excel_files():
    us = "us/"
    for xfile in glob.glob(os.path.join(us, "*.*")):
        xfile = re.sub('us/', '', xfile)
        yield xfile

def camel_to_underscore(name):
    name = re.sub('-', '_', name)
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    name = re.sub('__', '_', name)
    name = name.lower()
    return name

def generate_schema_name(xfile):
        junk, sep, name = xfile.partition("Flat.File.")
        final_name, dot, xl = name.partition(".")
        underscore_name = camel_to_underscore(final_name)
        trimmed_name = underscore_name.strip()
        schema_name = "amazon_{0}".format(underscore_name)
        if schema_name not in ["amazon_inventory_loader",
                               "amazon_price_inventory"]:
            return schema_name

## create schemas
def create_schemas():
    for xfile in read_excel_files():
        schema_name = generate_schema_name(xfile)
        dbconn.cur.execute("""
                           create schema if not exists {0};
                           """.format(schema_name))

def create_table_name(s):
    return camel_to_underscore(s)

def create_valid_tables(schema_name, table_name):
    dbconn.cur.execute(
        """
        begin;
        create table if not exists {0}.valid_{1} (
            {1} varchar primary key
        );
        commit;
        """.format(schema_name, table_name))

def create_template_table(schema_name):
    if schema_name:
        dbconn.cur.execute(
            """
            begin;
            create table if not exists {0}.template ();
            commit;
            """.format(schema_name))
        
def update_template_table(schema_name, column_name, data_type, optional):
    print(schema_name)
    if optional == "Required":
        dbconn.cur.execute(
            """
            begin;
            alter table {0}.template
            add column {1} {2} not null;
            commit;
            """.format(schema_name, column_name, data_type))

def insert_valid_values(schema_name, table_name, value_list):
    for v in value_list:
        if str(v) != 'nan':
            try:
                dbconn.cur.execute(
                    """
                    begin;
                    insert into {0}.valid_{1} ({1})
                    select '{2}'
                    where not exists
                        (select *
                         from {0}.valid_{1}
                         where {1} = '{2}');
                    commit;
                    """.format(schema_name, table_name, v))
            except:
                pass

def pg_to_tables(schema_name, pg_df):
    pg_cols = list(pg_df.columns)
    for tbl in pg_cols:
        tbl = re.sub('-', '_', tbl)
        if " " not in tbl:
            create_valid_tables(schema_name, tbl)

def insert_pg_vals(schema_name, pg_df):
    pg_vals = pg_df.to_dict('list')
    for col, val in pg_vals.items():
        col = create_table_name(col)
        insert_valid_values(schema_name, col, val)
        
def create_tables():
    for xfile in read_excel_files():
        schema_name = generate_schema_name(xfile)
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
    s = set()
    for xfile in read_excel_files():
        schema_name = generate_schema_name(xfile)
        create_template_table(schema_name)
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
                            
            # # print("")
            # # print(schema_name)
            # # print(pg_df.columns[2])
            #     print(type(js))
            

# create_schemas()
# create_tables()
get_stuff()

#print(type_dict)

dbconn.conn.commit()
dbconn.cur.close()

print("done")
