#!/usr/bin/python3

import re
import os.path
import sys
import glob
import pandas as pd

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

## create tables
def generate_table_names(pg):
    a = []
    for i in pg.itertuples():
        a.append(i)

    for tbl in a[0]:
        if tbl != 0 and tbl != 'nan':
            yield tbl

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

        
def create_tables():
    for xfile in read_excel_files():
        schema_name = generate_schema_name(xfile)
        xpath_file = pd.ExcelFile(os.path.join("us/", xfile))

        try:
            pg = pd.read_excel(xpath_file,
                               sheetname = "Valid Values")
            pgd = pd.DataFrame(pg)
            pgg = pgd.to_dict('list')
        except:
            pass

        if schema_name in ["amazon_food_service_and_jan_san",
                           "amazon_food_service_and_jan_san_lite"]:
            pg_cols = list(pg.columns)
            for tbl in pg_cols:
                tbl = re.sub('-', '_', tbl)
                if " " not in tbl:
                    create_valid_tables(schema_name, tbl)
 
            for k, v in pgg.items():
                k = create_table_name(k)
                insert_valid_values(schema_name, k, v)
            else:
                pg2 = pg
                pg2.columns = pg.iloc[0]
                pg2 = pg2.reindex(pg2.index.drop(0))
                pg2_cols = list(pg2.columns)
                pg2 = pg2.to_dict('list')
                for tbl in pg2_cols:
                    tbl = re.sub('-', '_', tbl)
                    if " " not in tbl:
                        create_valid_tables(schema_name, tbl)
                    
                for k, v in pg2.items():
                    k = create_table_name(k)
                    insert_valid_values(schema_name, k, v)    
            
create_schemas()
create_tables()

dbconn.conn.commit()
dbconn.cur.close()

print("done")
