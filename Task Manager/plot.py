from datetime import datetime
import os
from turtle import color
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *
import numpy as np
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def plot_show1(person):
    dic={}
    for task in session.query(Task).filter(Task.name == person):
        list=[]
        dic[task.id]=[]
        time1=task.start
        time11=datetime.strptime(time1,'%y/%m/%d')
        list.append(time11)
        time2=task.finish
        time22=datetime.strptime(time2,'%y/%m/%d')
        list.append(time22)
        list.append(task.task)
        dic.update({task.id:list})
    
    
    sort_orders=sorted(dic.items(),key=lambda x : x[1])
    
    x_list=[]
    y_list=[]
    labels=[]
    for i in range(len(sort_orders)):
        id=sort_orders[i][0]
        start=sort_orders[i][1][0]
        finish=sort_orders[i][1][1]
        task=sort_orders[i][1][2]
        
        s=start.strftime("%Y/%m/%d") + "-" + finish.strftime("%Y/%m/%d")
        x_list.append(s)
        time_interval = str(finish-start)
        d=time_interval.split(" ")
        y_list.append(int(d[0]))
        labels.append(task)
    
    x = np.arange(len(x_list)) 
    width = 0.35 
    fig, ax = plt.subplots()
    rect = ax.bar(x - width/2, y_list, width, label='time')
    ax.set_ylabel('duration')
    ax.set_title('name')
    ax.set_xticks(x, x_list)
    ax.legend()
    ax.bar_label(rect, padding=3)
    fig.tight_layout()

    plt.show()
