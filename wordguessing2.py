from random_word import RandomWords

def iniciar_juego():
    name = input("Introduce tu nombre: ")
    print(f"\n¡Hola {name}, bienvenido al juego de adivinar la palabra!\n")

    word = palabras()
    reglas()
    pista_1, pista_2 = pistas(word)
    print(f"\nPista 1: {pista_1}")
    print(f"Pista 2: {pista_2}")

    modo_juego(word, name)

def palabras():
    word = RandomWords().get_random_word()
    return word

def reglas():
    print(f"\n\nAdivina la palabra: ")
    print("\n==Reglas del juego==")
    print("· Tienes 12 intentos para adivinar la palabra.")
    print("· Puedes adivinar una letra o la palabra completa.")
    print("· Si adivinas la palabra, ganas.")
    print("· Si no adivinas la palabra, pierdes.")
    print("· Recuerda que no puedes usar números ni caracteres especiales.")
    print("====================")
    print("\n¡Buena suerte!\n")

def pistas(word):
    pista_1 = f"La palabra comienza con la letra '{word[0]}' y termina con la letra '{word[-1]}'."
    pista_2 = f"La palabra contiene {len(word)} letras."
    return pista_1, pista_2

def reiniciar_juego():
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            iniciar_juego()
            return
        elif restart == 'no':
            print("\n¡Gracias por jugar! Hasta la próxima.")
            return
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

def modo_juego(word, name):
    guesses = ''
    turns = 12
    while turns > 0:
        print("\nPalabra: ", end=' ')
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print("_", end=' ')
                failed += 1

        if failed == 0:
            print(f"\n\n¡Felicidades {name}, has Ganado!")
            print(f"La palabra era: {word}")
            reiniciar_juego()
            return

        guess = input("\n\nAdivina una letra o la palabra completa: ").strip().lower()

        if not guess.isalpha():
            print("\nEntrada no válida. Por favor, introduce una letra o una palabra.")
            continue

        if len(guess) == 1:
            if guess in guesses:
                print("\nYa has adivinado esa letra. Intenta con otra.")
                continue

            guesses += guess

            if guess not in word:
                turns -= 1
                print("\nIncorrecta")
                print(f"Te quedan {turns} intentos.")
            else:
                print("\nCorrecta")

        elif len(guess) == len(word):
            modo_ruleta(word, guess, name)
            return

        else:
            print("\nEntrada no válida. Por favor, introduce una letra o la palabra completa.")

        if turns == 0:
            print(f"\nLo siento {name}, has perdido.")
            print(f"La palabra era: {word}")
            reiniciar_juego()
            return

def modo_ruleta(word, guess, name):
    if guess == word:
        print(f"\n¡Felicidades {name}, has Ganado!")
        print(f"La palabra era: {word}")
    else:
        print(f"\nLo siento {name}, has perdido.")
        print(f"La palabra era: {word}")

    reiniciar_juego()

if __name__ == "__main__":
    iniciar_juego()
