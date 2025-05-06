import random
import menu  # Importamos el menú principal del emulador


def main_menu():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("1. Start Game")
        print("2. Return to Main Menu")
        choice = input("Please choose an option: ")
        if choice == '1':
            result = start_game()
            if result == "exit":
                break  # ← Salimos del menú del juego y volvemos al menú general
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")


def start_game():
    print("Hi welcome to the game! This is a number guessing game.")
    print("You have 7 chances to guess the number. Let's start!")


    number_to_guess = random.randrange(100)
    chances = 7
    guess_counter = 0


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
        elif my_guess > number_to_guess:
            print('📈 Your guess is too high.')
        elif my_guess < number_to_guess:
            print('📉 Your guess is too low.')


        print(f'You have {chances - guess_counter} attempts left.')


    return end_game()  # ← devolvemos lo que diga end_game()




def end_game():
    while True:
        print("\nGame Over!")
        print("1. Play Again")
        print("2. Return to Main Menu")
        choice = input("Please choose an option: ")
        if choice == '1':
            return start_game()  # ← sigue jugando
        elif choice == '2':
            menu.main_menu()  # Vuelve correctamente al **menú principal de todos los juegos**
            return  # 🔹 Detiene la ejecución para evitar el doble menú
        else:
            print("Invalid choice. Please try again.")