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
        duration = 10
        reward = 2
    elif choice == "2":
        duration = 15
        reward = 3
    elif choice == "3":
        duration = 30
        reward = 8
    elif choice == "4":
        duration = 40
        reward = 11
    elif choice == "5":
        duration = 60
        reward = 18
    else:
        print("Invalid choice. Using 10 minutes by default.")
        duration = 10
        reward = 2

    print(f"\n🍅 Pomodoro Timer started for {duration} minutes!")
    for i in range(duration * 60, 0, -1):  #turn into seconds
        minutes, seconds = divmod(i, 60)
        print(f"⏳ {minutes:02}:{seconds:02} remaining...", end="\r")
        time.sleep(1)

    print("\n✅ Pomodoro session complete!")
    state.add_resource(reward)
    print(f"🎉 You earned {reward} resource(s)! Current: {state.resources}")


