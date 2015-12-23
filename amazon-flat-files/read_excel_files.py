#!/usr/bin/python3

import re
import os.path
import glob

def read_excel_files():
    us = "us/"
    for xfile in glob.glob(os.path.join(us, "*.*")):
        xfile = re.sub('us/', '', xfile)
        yield xfile
