import time
from game_state import GameState

def run_pomodoro(state):
    print("\nChoose Pomodoro duration:")
    print("1. 10 minutes (+2 resources)")
    print("2. 15 minutes (+3 resources)")
    print("3. 30 minutes (+8 resources)")
    print("4. 40 minutes (+11 resources)")
    print("5. 60 minutes (+18 resources)")

    choice = input("Choose an option: ")
    
    if choice == "1":
        duration = 10  #5
        reward = 2
    elif choice == "2":
        duration = 15  #5
        reward = 3
    elif choice == "3":
        duration = 30  #3.75
        reward = 8
    elif choice == "4":
        duration = 40 #3.33
        reward = 12
    elif choice == "5":
        duration = 60  #3
        reward = 20
    else:
        print("Invalid choice. Using 10 minutes by default.")
        duration = 10
        reward = 2
    try:
        print(f"\n Pomodoro Timer started for {duration} minutes!")
        for i in range(duration , 0, -1):  #turn into seconds 測試中 之後記得改回duration*60
            minutes, seconds = divmod(i, 60)
            print(f" {minutes:02}:{seconds:02} remaining...", end="\r")
            time.sleep(1)

        print("\n✅ Pomodoro session complete!")
        state.add_resource(reward)
        print(f" You earned {reward} resource(s)! Current: {state.resources}")
    except KeyboardInterrupt:
        print("\n ⚠️  session interrupted. No resources earned.")

