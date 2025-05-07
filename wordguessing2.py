# Libreria RandomWords para obtener palabras aleatorias
from random_word import RandomWords

# Funciones
def iniciar_juego():

    'esta función inicia el juego, pide el nombre del jugador, muestra las reglas, las pistas, obtiene una palabra aleatoria y detecta el modo de juego'
    name = input("Introduce tu nombre: ")
    print(f"\n¡Hola {name}, bienvenido al juego de adivinar la palabra!\n")

    'aqui se obtiene una palabra aleatoria de la librería RandomWords'
    word = palabras()

    'aqui se muestran las reglas del juego y las pistas'
    reglas()
    pista_1, pista_2 = pistas(word)
    print(f"\nPista 1: {pista_1}")
    print(f"Pista 2: {pista_2}")

    'aqui se detecta en que modo esta jugando el jugador'
    modo_juego(word, name)

def palabras():
    'esta función obtiene una palabra aleatoria de la librería RandomWords'
    word = RandomWords().get_random_word()
    return word

def reglas():
    'esta función muestra las reglas del juego'
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
    'esta función genera dos pistas sobre la palabra, una sobre la longitud y otra sobre la primera y última letra'
    pista_1 = f"La palabra comienza con la letra '{word[0]}' y termina con la letra '{word[-1]}'."
    pista_2 = f"La palabra contiene {len(word)} letras."
    return pista_1, pista_2

def reiniciar_juego():
    'esta función sirve para reiniciar el juego'
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
    'esta función detecta si el jugador está jugando en modo normal o en modo ruleta'
    'estos son los turnos que tiene el jugador para adivinar la palabra'
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

        'verifica si el jugador ha introducido un número o un caracter especial'
        if not guess.isalpha():
            print("\nEntrada no válida. Por favor, introduce una letra o una palabra.")
            continue
        
        'si el jugador ha introducido la misma letra, se le avisa'
        if len(guess) == 1:
            if guess in guesses:
                print("\nYa has adivinado esa letra. Intenta con otra.")
                continue

            guesses += guess

            'si el jugador introduce una letra que no está en la palabra, se le resta un intento'
            if guess not in word:
                turns -= 1
                print("\nIncorrecta")
                print(f"Te quedan {turns} intentos.")
            else:
                print("\nCorrecta")
        
        # en caso de que el jugador haya introducido una palabra completa compatible con la longitud de la palabra cambia el modo de juego
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
    'esta función es el modo ruleta, donde el jugador puede adivinar la palabra completa, si acierta gana, si no pierde. Solo tiene un intento'
    if guess == word:
        print(f"\n¡Felicidades {name}, has Ganado!")
        print(f"La palabra era: {word}")
    else:
        print(f"\nLo siento {name}, has perdido.")
        print(f"La palabra era: {word}")

    reiniciar_juego()

if __name__ == "__main__":
    iniciar_juego()

# https://www.freecodecamp.org/news/python-requirementstxt-explained/
# Crear un archivo .txt con palabras para que respalde a la función (palabras)
# Probar PyInstaller y cx_Freeze