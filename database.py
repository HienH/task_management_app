import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine("sqlite:///test_db.db")  #Create our database

session = sessionmaker(bind=engine)()

Base = declarative_base()

class Tasks(Base):

    __tablename__ = "tasks"
    metadata = MetaData ()
    tasks = Table("tasks", metadata,
    Column("id", Integer, primary_key=True),  #The ID has to be unique so no 2 tasks can have the same ID 
    Column("title",String),
    Column("description",String),
    Column("importance",Integer),
    Column("status",Integer), )

    def __init__(self, tasks)

