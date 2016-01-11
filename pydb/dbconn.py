#!/usr/bin/python2
import psycopg2

conn = psycopg2.connect("dbname=omark user=postgres")

cur = conn.cursor()
