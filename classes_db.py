import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine("sqlite:///classes_db.db")  #Create our database

#from pdb import set_trace; set_trace() #in terminal run the py file and then type engine - check for SQLite engine to be displayed then quit 
session = sessionmaker(bind=engine)()

Base = declarative_base()

class Tasks(Base):

    __tablename__ = "tasktable"  #same name as table so "tasktable"
    
    task_id = Column(Integer, primary_key=True)  #The ID has to be unique so no 2 tasks can have the same ID 
    title = Column(String)
    description = Column(String)
    importance = Column(Integer)
    status = Column(Integer)

    def __init__(self, task_id, title, description, importance, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.importance = importance
        self.status = status

#Adding some data: 
#tasktable = Tasks(1, "task1", "first test task", 0, 0)

# session.add(tasktable) #stage information to be added table
# session.commit() #commit to database (ADD info)
# session.close()

ins = tasktable.insert()
str(ins)