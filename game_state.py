import json
import os

DATA_FILE = "save_data.json"

class GameState: 
    def __init__(self): #constuctor, same as GameState() in C++
        self.resources = 0
        self.todo_list = []
        self.load()

    def load(self): 
        if os.path.exists(DATA_FILE): #data exists
            with open(DATA_FILE, "r") as f: #get data from file
                data = json.load(f)
                self.resources = data.get("resources", 0)
                self.todo_list = data.get("todo_list", [])
        else:
            self.save() #create new data

    def save(self):
        data = {
            "resources": self.resources,
            "todo_list": self.todo_list
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2) #turning pyhton into json, then write into file

    def add_resource(self, amount=1): #resource control
        self.resources += amount
        self.save()

    def show_status(self): #show resources, to-do list
        print(f"Resources: {self.resources}")
        print(f"To-Do List: {len(self.todo_list)} item(s)")
