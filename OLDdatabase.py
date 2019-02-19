import sqlalchemy
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

#---------SQLAlchemy connect to database----------------#
engine = create_engine("sqlite:///taskdatabase.db")  #Create our database
conn = engine.connect()
session = sessionmaker(bind=engine)()
Base = declarative_base()

connection = engine.connect()


#---------TESTS to Check DB connection----------------#

def check_db_exists():
    try:
        f = open ("taskdatabase.db")
        f.close()
        print("file found")
#        return True
    except FileNotFoundError:
        print("file not found")
#check_db_exists()

def query_db_conn(): #add name in ()
    try:
        connection = engine.connect()
        print("ok")
        return conn
    except Exception as e:
        print(e)
#query_db_conn()

def print_db_tables():
    connection = engine.connect()
    print(engine.table_names())

#print_db_tables()



#---------------------Adding some data: -----------#


# class Taskmanager(db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    # title = db.Column(db.String) #limited to 50 charachters
    # description = db.Column(db.String) 
    # important = db.Column(db.Integer)
    # status = db.Column(db.Integer)  #can also do BOOLEAN! TRUE FALSE INSTAEAD OF INT 0 1


