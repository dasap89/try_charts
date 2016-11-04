# -*- coding: utf-8 -*-
import os
import pandas
import sqlite3
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


table_name = 'charts_datamodel'
con = sqlite3.connect("db.sqlite3")
con.text_factory = str
cur = con.cursor()

df = pandas.read_csv("eFw3Cefj.csv", usecols = ["Регион", "Страна", "Значение"], header=0)

df.columns = ["region", "country", "value"]

df.to_sql(table_name, con, if_exists='append', index=False)


con.close()