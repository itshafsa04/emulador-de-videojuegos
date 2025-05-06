import random
import menu  # Importamos el menú principal del emulador

def main_menu():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("1. Start Game")
        print("2. Return to Main Menu")
        choice = input("Please choose an option: ")
        if choice == '1':
            difficulty = choose_difficulty()
            result = start_game(difficulty)
            if result == "exit":
                break
        elif choice == '2':
            return "exit"  # Retornar al menú principal del emulador
        else:
            print("Invalid choice. Please try again.")

def choose_difficulty():
    while True:
        print("Choose Difficulty Level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        choice = input("Please choose an option: ")
        if choice == '1':
            return (50, 10, 'easy')
        elif choice == '2':
            return (100, 7, 'medium')
        elif choice == '3':
            return (200, 5, 'hard')
        else:
            print("Invalid choice. Please try again.")

def start_game(difficulty):
    max_number, chances, level = difficulty
    print(f"Hi welcome to the game! This is a number guessing game.")
    print(f"You have {chances} chances to guess the number between 1 and {max_number}. Let's start!")

    number_to_guess = random.randrange(1, max_number + 1)
    guess_counter = 0
    previous_hints = {'even': False, 'odd': False, 'range': False}

    while guess_counter < chances:
        try:
            my_guess = int(input('Please enter your guess: '))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        guess_counter += 1
        if my_guess == number_to_guess:
            print(f'🎉 Correct! The number was {number_to_guess}. You guessed it in {guess_counter} attempts!')
            break
        elif guess_counter >= chances:
            print(f'💀 Out of tries! The number was {number_to_guess}. Better luck next time.')
        else:
            give_hint(my_guess, number_to_guess, guess_counter, chances, level, max_number, previous_hints)

        print(f'You have {chances - guess_counter} attempts left. ⏳')

    return end_game()

def give_hint(my_guess, number_to_guess, guess_counter, chances, level, max_number, previous_hints):
    # Always give higher or lower hint
    if my_guess > number_to_guess:
        print('💡 Hint: 📉 Try a lower number.')
    else:
        print('💡 Hint: 📈 Try a higher number.')

    # Determine which hint to give
    if not previous_hints['even'] and not previous_hints['odd']:
        if number_to_guess % 2 == 0:
            print('💡 Hint: The number is even.')
            previous_hints['even'] = True
        else:
            print('💡 Hint: The number is odd.')
            previous_hints['odd'] = True
    elif not previous_hints['range']:
        range_size = {'easy': 10, 'medium': 20, 'hard': 30}[level]
        range_hint_start = max(1, number_to_guess - range_size // 2)
        range_hint_end = min(max_number, range_hint_start + range_size)
        print(f'💡 Hint: The number is between {range_hint_start} and {range_hint_end}.')
        previous_hints['range'] = True
    else:
        distance = abs(my_guess - number_to_guess)
        if distance == 1:
            print('🔥 Hot! You are very close.')
        else:
            print('❄️ Cold! You are far away.')

def end_game():
    while True:
        print("\nGame Over!")
        print("1. Play Again")
        print("2. Return to Main Menu")
        choice = input("Please choose an option: ")
        if choice == '1':
            difficulty = choose_difficulty()
            return start_game(difficulty)
        elif choice == '2':
            return "exit"  # Retornar al menú principal del emulador
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
