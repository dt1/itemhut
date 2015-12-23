#!/usr/bin/python3

import re
import os.path
import sys
import glob
import read_excel_files as rxf

sys.path.append("/omark/pydb")
import dbconn

import pandas as pd

def valid_column_names(pg):
    a = []
    for i in pg.itertuples():
        a.append(i)

    for j in a[0]:
        if j != 0 and j!= 'nan':
            try:
                dbconn.cur.execute(
                    """
                begin;
                create table if not exists table_test.valid_{1} (
                    {1} varchar primary key
                );
                commit;
                """.format('table_test', j))
            except:
                print("error")
            
def create_tables():
    for xfile in rxf.read_excel_files():
        print(xfile)
        us = "us/"
        xfile = pd.ExcelFile(os.path.join(us, xfile))
        if xfile in ["Flat.File.FoodServiceAndJanSan-Lite.US.xlsx",
                     "Flat.File.FoodServiceAndJanSan.xls"]:
            pg = pd.read_excel(xfile,
                               sheetname = "Valid Values")

        try:
            pg = pd.read_excel(xfile,
                               sheetname = "Valid Values",
                               skiprows = 0)
        except:
            pass
        valid_column_names(pg)

create_tables()

dbconn.conn.commit()
dbconn.cur.close()
