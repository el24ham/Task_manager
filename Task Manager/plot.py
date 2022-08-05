import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def plot_show():
    print("hello")
