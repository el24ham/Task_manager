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
    dict={}
    for task in session.query(Task).filter(Task.name == person):
        list=[]
        #s=task.start + "-" + task.finish
        time1=task.start
        time1=datetime.strptime(time1,'%y/%m/%d')
        list.append(time1)
        time2=task.start
        time2=datetime.strptime(time2,'%y/%m/%d')
        list.append(time2)
        time_interval = time2 - time1
        list.append(time_interval)
        list.append(task.task)
        dict[task.id] = list
    #sort_orders=sorted    
        
    
