#!/usr/bin/python2

import pandas as pd
import sys

pfile = str(sys.argv[1])
sname = str(sys.argv[2])


x2 = pd.ExcelFile(pfile)
x2 = x2.parse('Valid Values')

aa = []
for i in x2.itertuples():
    aa.append(i)

for j in aa[0]:
    if j != 0:
        print(
'''
create table {0}.valid_{1} (
     {1} varchar primary key
);'''.format(sname, j))
