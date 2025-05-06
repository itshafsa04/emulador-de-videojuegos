# importar librerías
from random_word import RandomWords

# Funcion para iniciar el juego
def iniciar_juego():

    # Pedir el nombre del jugador
    name = input("Introduce tu nombre: ")
    print(f"\n¡Hola {name}, bienvenido al juego de adivinar la palabra!\n")

    # Elegir una palabra al azar
    word = palabras()

    # Reglas del juego
    reglas()

    # Generar pistas
    pista_1, pista_2 = pistas(word)
    print(f"\nPista 1: {pista_1}")
    print(f"Pista 2: {pista_2}")
    

    print("\nPalabra: ", end=' ')
    for char in word:
        print("_", end=' ')
    print("\n")

    # Pedir al usuario que adivine la palabra o una letra
    while True:
        guess = input(f"\nAdivina la palabra o una letra: ").strip().lower()
        
        if not guess.isalpha():
            print("\nEntrada no válida. Por favor, introduce una letra o una palabra.")
 

        if (len(guess) == len(word)):
            modo_ruleta(word, guess)


        elif (len(guess) == 1):
            modo_normal(word, guess)

        else:
            print("\nEntrada no válida. Por favor, introduce una letra o la palabra completa.")

# Funciones del juego

def palabras():
    # Lista de palabras y elegir una al azar
    word = RandomWords().get_random_word()
    return word

def reglas():
    # Mostrar reglas
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
    # Generar pistas
    pista_1 = f"La palabra comienza con la letra '{word[0]}' y termina con la letra '{word[-1]}'."
    pista_2 = f"La palabra contiene {len(word)} letras."
    return pista_1, pista_2

def reiniciar_juego():
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            iniciar_juego()
            break
        elif restart == 'no':
            print("\n¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

# Funciones de los modos
def modo_normal(word, guess):

    turns = 12
    guessed_leaters = guess

    # Bucles
    while turns > 0:
        failed = 0
        print("\nPalabra: ", end=' ')
        for char in word:
            if char in guessed_leaters:
                print(char, end=' ')
            else:
                print("_", end=' ')
                failed += 1
        
        if failed == 0:
            print("\n¡Felicidades, has Ganado!")
            print(f"La palabra era: {word}")
            reiniciar_juego()
            return

        guess = input("\nIntroduce una letra: ").strip().lower()
        if not guess.isalpha() or len(guess) != 1:
            print("\nEntrada no válida. Por favor, introduce una letra.")
            continue

        if guess in guessed_leaters:
            print("\nYa has usado esa letra. Intenta con otra.")
            continue
    
        guessed_leaters += guess

        if guess not in word:
            turns -= 1
            print(f"\nIncorrecto. Te quedan {turns} intentos.")
            continue

        if turns == 0:
            print("\nLo siento, has perdido.")
            print(f"La palabra era: {word}")
            reiniciar_juego()
            return

def modo_ruleta(word, guess):
    
    # Mostrar la palabra con letras adivinadas y guiones bajos
    print("\nPalabra: ", end=' ')
    for char in word:
        print("_", end=' ')
    print("\n")
    
    # while True:
    if not guess.isalpha() or len(guess) != len(word):
        print("\nEntrada no válida. Por favor, introduce una palabra de la longitud correcta.")

    if guess == word:
            print(f"\n¡Felicidades, has Ganado!")
            print(f"La palabra era: {word}")
    else:
            print(f"\nLo siento, has perdido.")
            print(f"La palabra era: {word}")
    
    reiniciar_juego()

# Función principal para iniciar el juego
if __name__ == "__main__":
    iniciar_juego()