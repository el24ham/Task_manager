from cProfile import label
from cgitb import text
from os import remove
from tracemalloc import start
from turtle import color, right, title
import PySimpleGUI as sg
from tkinter import *
import database as db

#Menu(title="Task Manager")

layout = [[sg.Text("Hello there, welcome to our app")], [sg.Text("Select the option you want:")],[sg.Button("add")], [sg.Button("remove")], [sg.Button("person task")], [sg.Button("tasks")], [sg.Button("plot")], [sg.Button("exit")]]
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
            entry_n.delete(0, END)
            entry_t.delete(0, END)
            entry_s.delete(0, END)
            entry_f.delete(0, END)
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
        entry_n=Entry(add)
        entry_n.pack()
        
        label2 = Label(add,
            text ="Task:",
            foreground="red")
        label2.pack()
        entry_t=Entry(add)
        entry_t.pack()
        
        label3 = Label(add,
            text ="Start Time:",
            foreground="green")
        label3.pack()
        entry_s=Entry(add)
        entry_s.pack()
        
        label4 = Label(add,
            text ="Finish Time:",
            foreground="purple")
        label4.pack()
        entry_f=Entry(add)
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
        
        bt = Button(add,
                    text ="Submit", command=save_info)
        bt.pack()

    elif event == "remove":
        def remove_info():
            person=entry.get()
            db.remove_task(person)
            entry.delete(0, END)
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
        entry = Entry(eliminate)
        entry.pack() 
        bt = Button(eliminate,
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
            name_e.delete(0, END)
            label2.pack() 
            
        show_task = Tk()
        show_task.geometry("600x300")
        show_task.title("Person Tasks")
  
        label1 = Label(show_task,
            text ="Name:",
            foreground="blue")
        label1.pack()
        name_e = Entry(show_task)
        name_e.pack()
        
        bt = Button(show_task,
                    text ="Submit", command=show_person_tasks)
        bt.pack()
    
    elif event == "Plot": 
        pass
    
    mainloop()
                     
window.close()
