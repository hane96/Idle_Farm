import json
import os
from item import Item

DATA_FILE = "save_data.json"

class GameState: 
    def __init__(self): #constuctor, same as GameState() in C++
        self.resources = 0
        self.item = []
        self.pomodoro_count = 0
        self.load()

    def load(self): 
        if os.path.exists(DATA_FILE): #data exists
            with open(DATA_FILE, "r") as f: #get data from file
                data = json.load(f)
                self.resources = data.get("resources", 0)
                self.item = [Item.from_dict(i) for i in data.get("item", [])]
                self.pomodoro_count = data.get("pomodoro_count", 0)
        else:
            self.save() #create new data

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump({
                "resources": self.resources,
                "item": [item.to_dict() for item in self.item],
                "pomodoro_count": self.pomodoro_count
            }, f, indent=2) #turning python into json, then write into file

    def add_resource(self, amount=1): #resource control
        self.resources += amount
        self.pomodoro_count += 1
        self.save()

    def show_status(self): #show resources, item, pomodoro times
        print(f"Resources: {round(self.resources)}\n")
        print(f"Item: {len(self.item)} item(s)")
        for item in self.item:
            print(f" - {item.name}: {item.description} (Rate: {item.passive_rate}/sec)")
        print(f"Pomodoro sessions completed: {self.pomodoro_count} times")

    def passive_gain(self): #passive gain
        total = sum( (item.passive_rate*item.amount) for item in self.item)
        self.resources += total
        if total > 0:
            print(f"\n Passive +{total} resource(s). Current: {self.resources}")
        self.save()

    def reset(self):
        self.resources = 0
        self.item = []
        self.pomodoro_count = 0
        self.save()
