
import random

print("=" * 40)
print("       MOOD-BASED PRODUCTIVITY BUDDY")
print("=" * 40)

session_count = 0

activities = {
    "happy": [
        "Start a creative project.",
        "Help someone with a task.",
        "Learn something new."
    ],
    "sad": [
        "Take a gentle 5-minute walk.",
        "Listen to your favorite song.",
        "Write down three things you appreciate."
    ],
    "stressed": [
        "Take 5 slow, deep breaths.",
        "Organize your desk for 3 minutes.",
        "Step away from your screen briefly."
    ],
    "tired": [
        "Drink a glass of water.",
        "Stretch gently for 2 minutes.",
        "Take a short break from your screen."
    ],
    "motivated": [
        "Work on your biggest priority for 15 minutes.",
        "Learn one new Python concept.",
        "Finish one task you've been postponing."
    ]
}

while True:
    print("\nHow are you feeling today?")
    print("1. Happy 😊")
    print("2. Sad 😔")
    print("3. Stressed 😰")
    print("4. Tired 😴")
    print("5. Motivated 🚀")
    print("6. Exit")

    choice = input("\nChoose an option (1-6): ").strip()

    if choice == "6":
        print(f"\nYou completed {session_count} session(s).")
        print("Remember: small steps count. Goodbye! 👋")
        break

    moods = {
        "1": "happy",
        "2": "sad",
        "3": "stressed",
        "4": "tired",
        "5": "motivated"
    }

    if choice not in moods:
        print("Invalid choice. Please enter 1-6.")
        continue

    mood = moods[choice]
    suggestion = random.choice(activities[mood])
    session_count += 1

    print("\n" + "-" * 40)
    print(f"Your mood: {mood.capitalize()}")
    print(f"Your activity: {suggestion}")
    print("Challenge: Give yourself 5 minutes!")
    print("You've got this! 💪")
    print("-" * 40)

    again = input("\nCheck another mood? (y/n): ").strip().lower()

    if again != "y":
        print(f"\nSessions completed: {session_count}")
        print("Take care of yourself. Goodbye! 👋")
        break
