import random

def main_menu():
    print("Welcome to the Number Guessing Game!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Please choose an option: ")
    if choice == '1':
        start_game()
    elif choice == '2':
        print("Thank you for playing! Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def start_game():
    print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")

    number_to_guess = random.randrange(100)
    chances = 7
    guess_counter = 0

    while guess_counter < chances:
        guess_counter += 1
        my_guess = input('Please Enter your Guess: ').strip()

        if not my_guess.isdigit():
            print('You must enter a number to continue playing.')
            guess_counter -= 1
            continue

        my_guess = int(my_guess)

        if my_guess == number_to_guess:
            print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
            break
        elif guess_counter >= chances and my_guess != number_to_guess:
            print(f'Oops sorry, The number is {number_to_guess} better luck next time')
        elif my_guess > number_to_guess:
            print('Your guess is higher ')
        elif my_guess < number_to_guess:
            print('Your guess is lesser')

    end_game()

def end_game():
    print("Game Over!")
    print("1. Play Again")
    print("2. Return to Main Menu")
    choice = input("Please choose an option: ")
    if choice == '1':
        start_game()
    elif choice == '2':
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        end_game()

# Start the game by displaying the main menu
if __name__ == "__main__":
    main_menu()
