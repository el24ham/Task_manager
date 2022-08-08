from cProfile import label
from cgitb import text
from os import remove
from tracemalloc import start
from turtle import color, right, title
import PySimpleGUI as sg
from tkinter import *
import database as db
from tkinter import ttk
import GUI_plot as gp
#Menu(title="Task Manager")

layout = [[sg.Text("Hello there, welcome to our app")], [sg.Text("Select the option you want:")],[sg.Button("add")], [sg.Button("remove")], [sg.Button("person task")], [sg.Button("tasks")], [sg.Button("table")], [sg.Button("table1")], [sg.Button("exit")]]
window = sg.Window("Task Manager", layout, margins=(300, 150))


while True:
    event, values = window.read()
    if event == "exit" or event == sg.WIN_CLOSED:
        break
    elif event == "add": 
        
            
        def save_info():
            
            
            name_text=entry_n.get()
            task_text=entry_t.get()
            start_text=entry_s.get()
            finish_text=entry_f.get()
            # l = Label(add,text=name_text+"-"+task_text+"-"+start_text+"-"+finish_text )
            # l.pack()
            # name_text.delete(0, END)
            # task_text.delete(0, END)
            # start_text.delete(0, END)
            # finish_text.delete(0, END)
            db.insert_task(name_text,start_text,finish_text,task_text)
            label = Label(add, text="Task saved sucessfully!")
            label.pack()
            
        add = Tk()
        add.geometry("600x300")
        add.title("Adding")
  
        label1 = Label(add,
            text ="Name:",
            foreground="blue")
        label1.pack()
        entry_n=ttk.Entry(add)
        entry_n.pack()
        
        label2 = Label(add,
            text ="Task:",
            foreground="red")
        label2.pack()
        entry_t=ttk.Entry(add)
        entry_t.pack()
        
        label3 = Label(add,
            text ="Start Time:",
            foreground="green")
        label3.pack()
        entry_s=ttk.Entry(add)
        entry_s.pack()
        
        label4 = Label(add,
            text ="Finish Time:",
            foreground="purple")
        label4.pack()
        entry_f=ttk.Entry(add)
        entry_f.pack()
        """"
        label3 = Label(add,
            text ="Start Time:",
            foreground="green")
        label3.pack()
        
        start = Scrollbar(add)

        year_list = Listbox(add, yscrollcommand = start.set, justify='center')
        for year in range(2000,2051):
            year_list.insert(END, 'Year ' + str(year))
        year_list.pack()
        
        month_list = Listbox(add, yscrollcommand = start.set, justify='center')
        for month in range(1,13):
            month_list.insert(END, 'Month ' + str(month))
        month_list.pack()
        
        day_list = Listbox(add, yscrollcommand = start.set, justify='center')
        for day in range(1,32):
            day_list.insert(END, 'Day ' + str(day))
        day_list.pack()
        
        start.config(command = year_list.yview and month_list.yview and day_list.yview)

        label4 = Label(add,
            text ="Finish Time:",
            foreground="purple")
        label4.pack()
        
        finish = Scrollbar(add)

        year_list = Listbox(add, yscrollcommand = finish.set, justify='center')
        for year in range(2000,2051):
            year_list.insert(END, 'Year ' + str(year))
        year_list.pack()
        
        #month_list = Listbox(add, yscrollcommand = finish.set, justify='center')
        #for month in range(1,13):
        #    month_list.insert(END, 'Month ' + str(month))
        #month_list.pack()
        
        #day_list = Listbox(add, yscrollcommand = finish.set, justify='center')
        #for day in range(1,32):
        #    day_list.insert(END, 'Day ' + str(day))
        #day_list.pack()
        
        finish.config(command = year_list.yview)
        """
        
        bt = ttk.Button(add,
                    text ="Submit", command=save_info)
        bt.pack()

    elif event == "remove":
        def remove_info():
            person=entry.get()
            db.remove_task(person)
            label = Label(eliminate, text="Task removed sucessfully!")
            label.pack()
            
        eliminate = Tk()
        eliminate.geometry("600x300")
        eliminate.title("Removing")
        
        label1 = Label(eliminate,
            text = db.get_all_tasks())
        label1.pack() 
        label2 = Label(eliminate,
            text ="Task ID:",
            foreground="blue")
        label2.pack()
        entry = ttk.Entry(eliminate)
        entry.pack() 
        bt = ttk.Button(eliminate,
                    text ="Submit", command=remove_info)
        bt.pack()
    
    elif event == "tasks": 
        show_tasks = Tk()
        show_tasks.geometry("600x300")
        show_tasks.title("Tasks")
  
        label1 = Label(show_tasks,
            text = db.get_all_tasks())
        label1.pack() 
        
    elif event == "person task":
        
        def show_person_tasks():
            name=name_e.get()
            label2 = Label(show_task,
                text = db.get_person_tasks(name))
            #name.delete(0, END)
            label2.pack() 
            
        show_task = Tk()
        show_task.geometry("600x300")
        show_task.title("Person Tasks")
  
        label1 = Label(show_task,
            text ="Name:",
            foreground="blue")
        label1.pack()
        name_e = ttk.Entry(show_task)
        name_e.pack()
        
        bt = ttk.Button(show_task,
                    text ="Submit", command=show_person_tasks)
        bt.pack()
    
    elif event == "table": 
        show_table = Tk()
        show_table.geometry("600x300")
        show_table.title("table")
        table_frame = Frame(show_table)
        table_frame.pack()
        my_table = ttk.Treeview(table_frame)
        my_table['columns'] = ('id', 'name', 'task', 'start', 'finish' , 'duration')
        
        my_table.column("#0", width=0,  stretch=NO)
        my_table.column("id",anchor=CENTER, width=80)
        my_table.column("name",anchor=CENTER,width=80)
        my_table.column("task",anchor=CENTER,width=80)
        my_table.column("start",anchor=CENTER,width=80)
        my_table.column("finish",anchor=CENTER,width=80)
        my_table.column("duration",anchor=CENTER,width=80)
        
        my_table.heading("#0",text="",anchor=CENTER)
        my_table.heading("id",text="Id",anchor=CENTER)
        my_table.heading("name",text="Name",anchor=CENTER)
        my_table.heading("task",text="Task",anchor=CENTER)
        my_table.heading("start",text="Start",anchor=CENTER)
        my_table.heading("finish",text="Finish",anchor=CENTER)
        my_table.heading("duration",text="Duration",anchor=CENTER)
        
        id_list,name_list,task_list,start_list,finish_list,duration_list=gp.plot_show()
        for i in range(len(id_list)):
            my_table.insert(parent='',index='end',iid=i,text='',
            values=(str(id_list[i]),str(name_list[i]),str(task_list[i]),str(start_list[i]),str(finish_list[i]),str(duration_list[i])))
        
        my_table.pack()    
    
    
    elif event == "table1": 
        def person_info():
            table1_frame = Frame(show_table1)
            table1_frame.pack()
            my_table1 = ttk.Treeview(table1_frame)
            my_table1['columns'] = ('id', 'task', 'start', 'finish' , 'duration')
        
            my_table1.column("#0", width=0,  stretch=NO)
            my_table1.column("id",anchor=CENTER, width=80)
            my_table1.column("task",anchor=CENTER,width=80)
            my_table1.column("start",anchor=CENTER,width=80)
            my_table1.column("finish",anchor=CENTER,width=80)
            my_table1.column("duration",anchor=CENTER,width=80)
        
            my_table1.heading("#0",text="",anchor=CENTER)
            my_table1.heading("id",text="Id",anchor=CENTER)
            my_table1.heading("task",text="Task",anchor=CENTER)
            my_table1.heading("start",text="Start",anchor=CENTER)
            my_table1.heading("finish",text="Finish",anchor=CENTER)
            my_table1.heading("duration",text="Duration",anchor=CENTER)
            # text=Text(show_table1, width=80, height=15)
            # text.pack()
            person=table_e.get()
            id_list,task_list,start_list,finish_list,duration_list=gp.plot1_show(person)
            for i in range(len(id_list)):
                # text.insert(END,str(id_list)+" "+str(task_list)+" "+str(start_list)+" "+str(finish_list)+" "+str(duration_list))
                my_table1.insert(parent='',index='end',iid=i,text='',
                values=(str(id_list[i]),str(task_list[i]),str(start_list[i]),str(finish_list[i]),str(duration_list[i])))
            my_table1.pack()
            
        show_table1 = Tk()
        show_table1.geometry("600x300")
        show_table1.title("table")
        label1 = Label(show_table1,
            text ="person name:",
            foreground="blue")
        label1.pack()
        table_e = ttk.Entry(show_table1)
        table_e.pack() 
        bt = ttk.Button(show_table1,
                    text ="Submit", command=person_info)
        bt.pack()
    
    mainloop()
                     
window.close()
