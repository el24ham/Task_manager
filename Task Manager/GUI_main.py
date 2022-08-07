from turtle import color, title
from unicodedata import name
import PySimpleGUI as sg
from tkinter import *

layout = [[sg.Text("Hello there, welcome to our app")], [sg.Text("Select the option you want:")],[sg.Button("add")], [sg.Button("remove")], [sg.Button("person task")], [sg.Button("tasks")], [sg.Button("plot")], [sg.Button("exit")]]
window = sg.Window("Task Manager", layout, margins=(300, 150))

while True:
    event, values = window.read()
    if event == "exit" or event == sg.WIN_CLOSED:
        break
    elif event == "add": 
        add = Tk()
        add.geometry("600x300")
        add.title("Adding")
  
        label = Label(add,
                text ="Name:",
                foreground="blue",
                background="green")
        entry = Entry(add)

        label.pack(fill=BOTH, expand=True)
        entry.pack()

    mainloop()
          
window.close()
