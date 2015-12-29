#!/usr/bin/python3

import os.path
import sys

sys.path.append("/omark/pydb")
import dbconn

schemas = dbconn.execute(
"""
select schema_name
from information_schema.schemata
where schema_name ~~* 'amazon%';
""")

schemas.fetchall()
