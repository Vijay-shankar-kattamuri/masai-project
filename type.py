import json
import random
import time

def update_leaderboard(username, wpm, leaderboard_file='leaderboard.json'):
    try:
        with open(leaderboard_file, 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    leaderboard.append({'username': username, 'wpm': wpm})
    leaderboard.sort(key=lambda x: x['wpm'], reverse=True)

    with open(leaderboard_file, 'w') as file:
        json.dump(leaderboard, file, indent=2)

def show_leaderboard(leaderboard_file='leaderboard.json'):
    try:
        with open(leaderboard_file, 'r') as file:
            leaderboard = json.load(file)
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(f"{entry['username']}: {entry['wpm']} WPM")
    except FileNotFoundError:
        print("\nLeaderboard is empty.")

def load_words_from_json(category, words_file='words.json'):
    try:
        with open(words_file, 'r') as file:
            words_data = json.load(file)
        return words_data.get(category, [])
    except FileNotFoundError:
        print(f"Words file '{words_file}' not found.")
        return []

def get_user_input():
    return input("\nType the words exactly as shown. Press 'Ctrl + Q' to quit.\nYour typing starts now: ")

def main():
    print("Welcome to the Terminal Typing Test!")

    username = input("Enter your username: ")

    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Choose a typing category (e.g., 'animals', 'fruits'): ")
            words = load_words_from_json(category.lower())

            if not words:
                print("Invalid category or words file not found.")
                continue

            random.shuffle(words)
            start_time = time.time()

            typed_words = get_user_input().split()
            end_time = time.time()

            time_taken = round(end_time - start_time, 2)
            words_typed = len(typed_words)
            wpm = round((words_typed / time_taken) * 60)  # Words per minute

            print(f"\nYour Typing Metrics:")
            print(f"Words Typed: {words_typed}")
            print(f"Time Taken: {time_taken} seconds")
            print(f"Words Per Minute (WPM): {wpm}")

            update_leaderboard(username, wpm)

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            print("Exiting the Typing Test. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
