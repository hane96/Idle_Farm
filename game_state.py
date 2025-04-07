import json
import os

DATA_FILE = "save_data.json"

class GameState: 
    def __init__(self): #constuctor, same as GameState() in C++
        self.resources = 0
        self.todo_list = []
        self.pomodoro_count = 0
        self.load()

    def load(self): 
        if os.path.exists(DATA_FILE): #data exists
            with open(DATA_FILE, "r") as f: #get data from file
                data = json.load(f)
                self.resources = data.get("resources", 0)
                self.todo_list = data.get("todo_list", [])
                self.pomodoro_count = data.get("pomodoro_count", 0)
        else:
            self.save() #create new data

    def save(self):
        data = {
            "resources": self.resources,
            "todo_list": self.todo_list,
            "pomodoro_count": self.pomodoro_count
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2) #turning pyhton into json, then write into file

    def add_resource(self, amount=1): #resource control
        self.resources += amount
        self.pomodoro_count += 1
        self.save()

    def show_status(self): #show resources, to-do list
        print(f"Resources: {self.resources}\n")
        print(f"To-Do List: {len(self.todo_list)} item(s)")
        print(f"Pomodoro sessions completed: {self.pomodoro_count} times")

    def reset(self):
        self.resources = 0
        self.todo_list = []
        self.pomodoro_count = 0
        self.save()
