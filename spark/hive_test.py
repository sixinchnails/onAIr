from pyhive import hive
from datetime import datetime
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['DEFAULT']['host']
port = config['DEFAULT']['port']
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']
database = config['DEFAULT']['database']
auth = config['DEFAULT']['auth']

hive_con = hive.Connection(
    host=host,
    port=port,
    username=username,
    password=password,
    database=database,
    auth=auth
)

cursor = hive_con.cursor()
date = datetime.today().strftime("%Y%m%d")

test_query='''
select * from k_means_data_points_;
''' + date

cursor.execute(test_query.replace(';', ''))

try:
    output = cursor.fetchall()
except:
    output = None

print(output)
