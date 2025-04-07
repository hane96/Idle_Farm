from game_state import GameState

def main_menu():
    game = GameState()

    while True:
        print("\n--- Idle_Farm ---")
        game.show_status()

        print("\nOptions:")
        print("1. Gain 1 Resource (Test)")
        print("2. Save and Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            game.add_resource(1)
            print("Gained 1 resource!")
        elif choice == "2":
            print("Saving and exiting...")
            game.save()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__": #only run main_menu() in main
    main_menu()
