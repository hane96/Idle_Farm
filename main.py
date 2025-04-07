from game_state import GameState
from pomodoro import run_pomodoro  # ← 新增這行
import os 

def main_menu():
    state = GameState()

    while True:
        print("\n=== Productivity Game ===")
        print("1. Show Status")
        print("2. Add Resource")
        print("3. Start Pomodoro 🍅")  # ← 新選項
        print("4. Exit")
        print("5. Delete data")

        choice = input("Choose an option: ")

        if choice == "1":
            state.show_status()
        elif choice == "2":
            state.add_resource()
            print("Resource added.")
        elif choice == "3":
            run_pomodoro(state)  # ← 呼叫番茄鐘
        elif choice == "4":
            print("Goodbye!")
            break
        elif choice == '5':
            if os.path.exists("save_data.json"):
                print("Data deleted")
            state.reset()
        else: 
            print("Invalid choice.")


if __name__ == "__main__": #only run main_menu() in main
    main_menu()
