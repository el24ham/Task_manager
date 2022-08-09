from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///tasks.db', echo=True)
Base = declarative_base()

class Task(Base):
    """"""
    __tablename__ = "tasks"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    task = Column(String)
    start = Column(String)
    finish = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, name, task, start, finish):
        """"""
        self.name = name
        self.task = task
        self.start = start
        self.finish = finish

# create tables
Base.metadata.create_all(engine)

