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

d = {aa[0]:aa[1:] for aa in zip(*aa)}

d.pop(0)

for k, v in d.items():
    d[k] = set(v)

for k, v in d.items():
    a = '''insert into {0}.valid_{1} values'''.format(sname, k)
    b = ''
    for vv in v:
        if type(vv) != float:
            b += ('\n(\'{0}\'),'.format(vv))
    c = a + b
    c = c[:-1]
    c += ';\n'
    print(c)

