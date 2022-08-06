from datetime import datetime
import os
from turtle import color
from tabulate import tabulate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import Task
from tabledef import *
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('sqlite:///tasks.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def plot_show1(person):
    dic={}
    for task in session.query(Task).filter(Task.name == person):
        list=[]
        dic[task.id]=[]
        format = '%Y/%m/%d'
        time1=task.start
        time11=datetime.strptime(time1, format).date()
        list.append(time11)
        time2=task.finish
        time22=datetime.strptime(time2, format).date()
        list.append(time22)
        list.append(task.task)
        dic.update({task.id:list})
    
    
    sort_orders=sorted(dic.items(),key=lambda x : x[1])
    
    #name_list=[]
    start_list=[]
    finish_list=[]
    duration_list=[]
    task_list=[]
    id_list=[]
    for i in range(len(sort_orders)):
        id=sort_orders[i][0]
        start=sort_orders[i][1][0]
        finish=sort_orders[i][1][1]
        task=sort_orders[i][1][2]
        
        #s=start.strftime("%Y/%m/%d") + "-" + finish.strftime("%Y/%m/%d")
        #name_list.append(s)
        id_list.append(id)
        start_list.append(start)
        finish_list.append(finish)
        time_interval = str(finish-start)
        d=time_interval.split(" ")
        duration_list.append(int(d[0]))
        task_list.append(task)
    
        
    dict={'Task id':id_list,
          'Task':task_list,
          'Start':start_list,
          'Finish':finish_list,
          'Duration':duration_list}
    
    df=pd.DataFrame(dict,columns=['Task id','Task','Start','Finish','Duration'])
    print(tabulate(df,headers='keys',tablefmt='psql'))
    
