# Librerias
from random_word import RandomWords

# Funciones

## Funciones del juego
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
def pistas(word):
    # Generar pistas
    pista_1= print(f"La palabra tiene {len(word)} letras.")
    pista_2= print(f"La palabra comienza con la letra '{word[0]}' y termina con la letra '{word[-1]}'.")
    return pista_1, pista_2
## Modos del juego
def modo_normal(word, guess):
    # Modo normal
    if guess in word:
        print(f"\n¡Correcto! La letra '{guess}' está en la palabra.")
    else:
        print(f"\n¡Incorrecto! La letra '{guess}' no está en la palabra.")

def modo_ruleta(word, guess):
    # Modo ruleta
    if guess == word:
        print(f"\n¡Felicidades! Has adivinado la palabra '{word}' correctamente.")
    else:
        print(f"\n¡Incorrecto! La palabra correcta era '{word}'.")

## Juego
def main():
    # Pedir al usuario su nombre
    nombre = input("Introduce tu nombre: ").strip().capitalize()
    print(f"\n¡Hola {nombre}, bienvenido al juego de adivinar la palabra!\n")

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
            continue

        if (len(guess) == len(word)):
            modo_ruleta(word, guess)

        elif (len(guess) == 1):
            modo_normal(word, guess)

        else:
            print("\nEntrada no válida. Por favor, introduce una letra o la palabra completa.")

if __name__ == "__main__":
    main()
