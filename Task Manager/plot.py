from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def plot_show1(person):
    object=()
    performance=[]
    for task in session.query(Task).filter(Task.name == person):
        s=task.start + "-" + task.finish
        time1=task.start
        time1=datetime.strptime(time1,'%y/%m/%d')
        time2=task.start
        time2=datetime.strptime(time2,'%y/%m/%d')
        time_interval = time2 - time1
        performance.append(time_interval)
        s += (str(task.id) + " " + task.name + " " + task.task + " " + task.start + " " + task.finish + "\n")
