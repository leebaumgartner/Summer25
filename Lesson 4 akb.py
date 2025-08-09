from random import randrange

def get_user_weapon():
    print("\nChoose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    while True:
        try:
            choice = int(input("Enter the number of your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_opponent_weapon():
    return randrange(1, 4)  

def determine_winner(user, opponent):
    weapons = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\nYou chose: {weapons[user]}")
    print(f"Opponent chose: {weapons[opponent]}")

    if user == opponent:
        print("It's a tie!")
    elif (user == 1 and opponent == 3) or \
         (user == 2 and opponent == 1) or \
         (user == 3 and opponent == 2):
        print("You win!")
    else:
        print("You lose!")

def main():
    play_again = 'y'

    while play_again.lower() == 'y':
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()
        determine_winner(user_weapon, opponent_weapon)

        play_again = input("\nWould you like to play again? (y/n): ")

if __name__ == "__main__":
    main()
print("This was completed by Annaleigh Baumgartner")
