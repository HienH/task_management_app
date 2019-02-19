import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select

#Create DB
engine = create_engine('sqlite:///taskmanager.db')

#Connect to DB
connection = engine.connect()

metadata = MetaData()  #initialise metadata object

tasktable = Table("tasktable", metadata, autoload=True, autoload_with=engine) 

def check_db():
    try:
        print(engine.table_names())
        print(repr(tasktable))
        print("Success! database connected")
    except Exception as e:
        print(e)

check_db()
#------SQL Queries sungin SQLalechemy---------#


stmt = 'SELECT * from tasktable' 
results_proxy = connection.execute(stmt)
results = results_proxy.fetchall()

#Getting results 

def print_table_columns():
    first_row = results[0]
    print(first_row.keys())


def print_all_data():
    for row in results:
        print(row)
#print_all_data()

# first_row = results[0]
# print(first_row)

# # second_row = results[1]
# # print(second_row)

#  #Get COLUMN NAMES in a list

# connection = engine.connect()
# stmt = select([mytable]) #select all columns and rows in mytable
# print(stmt)
# results = connection.execute(stmt).fetchall()  #fetch the results
# print(results)

# # to check our SQL command do print(stmt)