#!/usr/bin/python3
import psycopg2
import psycopg2.extras

conn = psycopg2.connect("dbname=itemhut user=postgres")

cur = conn.cursor()
dcur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
