
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def insert_task(person, start, finish, task):
    task1 = Task(person, task, start, finish)
    session.add(task1)
    session.commit()
    
   
def get_all_tasks():
    s = ""
    for task in session.query(Task).order_by(Task.id):
        s += (str(task.id) + " " + task.name + " " + task.task + " " + task.start + " " + task.finish + "\n")    
    return s

def get_person_tasks(person):
    s = " "
    for task in session.query(Task).filter(Task.name == person):
        s += (str(task.id) + " " + task.name + " " + task.task + " " + task.start + " " + task.finish + "\n")
    return s

def remove_task(id):
    session.query(Task).filter(Task.id == id).delete()
    session.commit()

def remove_all_tasks(person):
    session.query(Task).filter(Task.name == person).delete()
    session.commit()
    