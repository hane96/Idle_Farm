from game_state import GameState
from pomodoro import run_pomodoro
import os
import shop
import time
import threading

def start_passive_income(state):
    def passive_loop():
        while True:
            state.passive_gain()
            time.sleep(10)  #add per 10 secs
    t = threading.Thread(target=passive_loop, daemon=True)
    t.start()


def main_menu():
    state = GameState()
    start_passive_income(state) #passive income 

    while True:
        print("\n=== Productivity Game ===")
        print("1. Show Status")
        print("2. Add Resource")
        print("3. Start Pomodoro")
        print("4. Exit")
        print("5. Delete data")
        print("6. Enter Shop")

        choice = input("Choose an option: ")

        if choice == "1": #show status
            state.show_status()
        elif choice == "2": #add resource
            state.add_resource(10)
            print("Resource added.")
        elif choice == "3": #pomodoro
            run_pomodoro(state)  
        elif choice == "4": #exit
            print("Goodbye!")
            break
        elif choice == '5': #reset data
            if os.path.exists("save_data.json"):
                print("Data deleted")
            state.reset()
        elif choice == "6":
            while True:
                shop.show_shop()
                item_choice = input("輸入商品名稱或 'back': ")
                if item_choice == "back":
                    break
                else:
                    shop.purchase_item(state, item_choice)
        else: 
            print("Invalid choice.")


if __name__ == "__main__": #only run main_menu() in main
    main_menu()
