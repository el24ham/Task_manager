from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *

#import matplotlib.pyplot as plt; plt.rcdefaults()
#import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def plot_show1(person):
    dict={}
    for task in session.query(Task).filter(Task.name == person):
        list=[]
        
        time1=task.start
        time1=datetime.strptime(time1,'%y/%m/%d')
        list.append(time1)
        time2=task.start
        time2=datetime.strptime(time2,'%y/%m/%d')
        list.append(time2)
        list.append(task.task)
        dict[task.id] = list
    
    sort_orders=sorted(dict.items[1](),key=lambda x : x[1])
    x=[]
    y=[]
    lables=[]
    for i in sort_orders:
        s=i[0] + "-" + i[1]
        x.append(s)
        time_interval = i[1] - i[0]
        y.append(time_interval)
        lables.append(i[2])
        
    plt.bar(x,y,fc="lightgray",ec="black")
    for i in range(len(x)):
        plt.text(i,y[i],lables[i],ha="center",va="bottom")
    
    plt.show()            
                           
        
    
