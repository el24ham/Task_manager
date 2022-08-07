import PySimpleGUI as sg

layout = [[sg.Text("Hello there, welcome to our app")], [sg.Text("Select the option you want")],[sg.Button("add")], [sg.Button("remove")], [sg.Button("person task")], [sg.Button("tasks")], [sg.Button("plot")], [sg.Button("exit")]]
window = sg.Window("Task Manager", layout, margins=(300, 150))

while True:
    event, values = window.read()
    if event == "exit" or event == sg.WIN_CLOSED:
        break

window.close()
