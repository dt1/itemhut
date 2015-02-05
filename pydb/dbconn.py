#!/usr/bin/python2
import psycopg2
from psycopg2.extras import Json
import json


conn = psycopg2.connect("dbname=omark user=postgres")

cur = conn.cursor()

# cur.execute("SELECT * FROM jdata")

# print(cur.fetchone())
