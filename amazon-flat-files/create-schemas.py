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

def create_valid_tables(schema_name, table_name):
        try:
            dbconn.cur.execute(
                """
                begin;
                create table if not exists {0}.valid_{1} (
                    {1} varchar primary key
                );
                commit;
                """.format(schema_name, table_name))
        except:
            print("error", " ", schema_name, " ", table_name)

def create_tables():
    for xfile in read_excel_files():
        print(xfile)
        schema_name = generate_schema_name(xfile)
        xpath_file = pd.ExcelFile(os.path.join("us/", xfile))
        ## must fix this. 
        if schema_name in ["amazon_food_service_and_jan_san",
                           "amazon_food_service_and_jan_san_lite"]:
            pg = pd.read_excel(xpath_file,
                               sheetname = "Valid Values")
        else:
            try:
                pg = pd.read_excel(xpath_file,
                               sheetname = "Valid Values")
            except:
                pass
        table_generator = generate_table_names(pg)
        for table_name in table_generator:
            create_valid_tables(schema_name, table_name)
            
create_schemas()
create_tables()

dbconn.conn.commit()
dbconn.cur.close()
