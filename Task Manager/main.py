import database as db
import plot as p
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def hint():
    print("Available Commands: ")
    print("""
add -------------- To add task
remove ----------- To remove task
person task ------ To see person's task
tasks ------------ To see availble tasks
plot ------------- To show plot
exit ------------- To exit task manager
""")
    print("Enter your command: ")

clear()
print("Hi buddy")
hint()

while True:
    
    msg=input()
    
    if msg=="exit": 
        
        clear()
        break

    elif msg=="add" :
        
        clear()
        print("Name: ")
        person = input()
        print("Task: ")
        task = input()
        print("Start Time: ")
        start = input()
        print("Finish Time: ")
        finish = input()
        db.insert_task(person, start, finish, task)
        
        clear()
        print("Task added successfully")
        hint()
        
    elif msg=="remove" :
        
        clear()
        print("Name: ")
        person = input()

        db_tasks= db.get_person_tasks(person)

        if len(db_tasks)==0:
            print("No task found")
        else:
            print(db.get_person_tasks(person))
            
        print("Do you want to remove all tasks for " + person + "? (y/n)")
        if input()=="y":
            print("Enter task id : ")
            id = input()
            db.remove_task(id)
            clear()
            print("task removed")
        hint()
     
    elif msg=="tasks" :
        
        clear()
        print(db.get_all_tasks())
        hint()
        
    elif msg=="person task" :
        
        clear()
        print("Name: ")
        person = input()
        db_tasks= db.get_person_tasks(person)
        clear()
        if len(db_tasks)==0:
            print("No task found")
            
        else:
            print(db_tasks)
        hint()
            
    elif msg=="plot" :
        
        clear()
        p.show_plot()
             
    else:
        clear()
        print("Invalid command")
        hint()
                