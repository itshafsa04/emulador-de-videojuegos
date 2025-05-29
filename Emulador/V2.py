# Librería de palabras randoms
import csv
import random
from random_word import RandomWords

# Constantes
"""
VARIABLES:
MAX_TURNS: Número máximo de intentos permitidos.
MSG_BIENVENIDA: Mensaje de bienvenida al jugador.
MSG_REGLAS: Mensaje que contiene las reglas del juego.
"""
MAX_TURNS = 12
MSG_BIENVENIDA = "Hola {}, bienvenido al juego de adivinar la palabra."
MSG_REGLAS = "\n==Reglas del juego==\n· Tienes {} intentos para adivinar la palabra.\n· Puedes adivinar una letra o la palabra completa.\n· Recuerda que no puedes usar números ni caracteres especiales.\n ·Las palabras estan en inglés. \n====================\n\n¡Buena suerte {}!\n"

# Funciones
def obtener_palabra():
    """
    Obtiene un palabra aleatoria usando la librería RandomWords.
    Si falla, devuelve una palbra por defecto.
    """
    try:
        word = RandomWords().get_random_word()

        if not word:
            print ("Error: No se pudo obtener una palabra aleatoria de RandomWords. Usando archivo de respaldo.")
            with open('randomwords_backup.csv', newline='') as f:
                reader = csv.DictReader(f)
                words = [row['word'] for row in reader]
            return random.choice(words)
        return word
    
    except Exception as e:
        print(f"Error al obtener la palabra: {e}")
        raise

def reglas(name):
    """
    Muestra las reglas del juego al jugador.
    """
    print(MSG_REGLAS.format(MAX_TURNS, name))

def pistas(word):
    """
    Genera dos pistas basadas en la palabra:
    - Primera y última letra.
    - Longitud de la palabra.
    """
    pista_1 = f"La palabra comienza con la letra '{word[0]}' y termina con la letra '{word[-1]}'."
    pista_2 = f"La palabra contiene {len(word)} letras."
    return pista_1, pista_2

def mostrar_palabra(word, guesses):
    """
    Muesta la palabra con letra adivinadas y guiones bajos para las letras no descubiertas.
    """
    return ' '.join([char if char in guesses else '_' for char in word])

def iniciar_juego():
    """
    Inicia una nueva partida:
    - Solicita el nombre del jugador.
    - Genera una palbra aleatoria.
    - Muestra las pistas.
    - Inicia el modo de juego principal. 
    """
    name = input("¿Cuál es tu nombre? ")
    print(MSG_BIENVENIDA.format(name))

    word = obtener_palabra()
    reglas(name)
    pista_1, pista_2 = pistas(word)
    print(f"\nPista 1: {pista_1}")
    print(f"Pista 2: {pista_2}")

    modo_juego(word, name)

def reiniciar_juego(name):
    """
    Pregunta al jugador si desea jugar de nuevo.
    Reinicia el juego si responde 'si', o sale del juego si responde 'no'.
    """
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            iniciar_juego()
            return
        if restart == 'no':
            print(f"\n¡Gracias por jugar {name}! Hasta la próxima.")
            return
        print("\nPor favor, responde con 'si' o 'no'.")

def modo_juego(word, name):
    """
    Modo principal del juego:
    - Permite adivinar una letra a la vez.
    - Si se intenta adivinar la palabra completa y tiene la longitud correcta, entra en el modo ruleta.
    - Si se adivina toda la palabra letra por letra o completa se gana.
    - Si se agotan los intentos, se pierde.
    """
    guesses = set()
    turns = MAX_TURNS
    while turns > 0:
        print("\nPalabra: ", mostrar_palabra(word, guesses))

        if mostrar_palabra(word, guesses).replace(' ', '') == word:
            print(f"\n¡Felicidades {name}, adivinaste la palabra!")
            reiniciar_juego(name)
            return
        
        guess = input("\nAdivina una letra o la palabra completa: ").strip().lower()

        if not validar_entrada(guess, 'letra' if len(guess) == 1 else 'palabra'):
            print("\nEntrada no válida. Por favor, introduce una letra o una palabra.")
            continue

        if len(guess) == 1:
            if guess in guesses:
                print("\nYa has adivinado esa letra, intenta con otra.")
                continue

            guesses.add(guess)

            if guess not in word:
                turns -= 1
                print(f"\nIncorrecto. Te quedan {turns} intentos.")
            else:
                print("\n¡Correcto!")

        elif len(guess) == len(word):
            modo_ruleta(word, guess, name)
            return

        else:
            print(f"\nLa palabra debe tener {len(word)} letras. Intenta de nuevo.")
            continue  # No se descuenta turno

        if turns == 0:
            print(f"\n¡Perdiste! La palabra era: {word}")
            reiniciar_juego(name)
            return

def modo_ruleta(word, guess, name):
    """
    Modo ruleta:
    - El jugador tiene un solo intento para adivinar la palbra completa.
    """    
    if guess == word:
        print(f"\n¡Felicidades {name}, adivinaste la palabra!")
    else:
        print(f"\nIncorrecto. La palabra era: {word}")

    reiniciar_juego(name)

def validar_entrada(entrada, tipo):
    """
    Valida la entrada del jugador:
    - 'letra': debe ser una sola letra alfabética.
    - 'palabra': debe ser una palabra alfabética de más de una letra.
    """
    return entrada.isalpha() and ((tipo == 'letra' and len(entrada) == 1) or (tipo == 'palabra' and len(entrada) > 1))

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_juego()
