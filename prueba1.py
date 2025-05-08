from random_word import RandomWords

MAX_TURNS = 12

def iniciar_juego():
    name =input("¿Cuál es tu nombre? ")
    print(f"Hola {name}, bienvenido al juego de adivinar la palabra.")

    word = palabras()
    reglas(name)
    pista_1, pista_2 = pistas(word)
    print(f"\nPista 1: {pista_1}")
    print(f"Pista 2: {pista_2}")

    modo_juego(word, name, MAX_TURNS)

def palabras():
    try:
        word = RandomWords().get_random_word()
        if word :
            return word
        else:
            raise ValueError("No se pudo obtener una palabra aleatoria.")
    except Exception as e:
        print(f"Error al obtener la palabra: {e}")
        return "palabra"

def reglas(name):
    print(f"\n\nAdivina la palabra: ")
    print("\n==Reglas del juego==")
    print(f"· Tienes {MAX_TURNS} intentos para adivinar la palabra.")
    print("· Puedes adivinar una letra o la palabra completa.")
    print("· Recuerda que no puedes usar números ni caracteres especiales.")
    print("====================")
    print(f"\n¡Buena suerte {name}!\n")

def pistas(word):
    pista_1 = f"La palabra comienza con la letra '{word[0]}' y termina con la letra '{word[-1]}'."
    pista_2 = f"La palabra contiene {len(word)} letras."
    return pista_1, pista_2

def reiniciar_juego(name):
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            iniciar_juego()
            return
        elif restart == 'no':
            print(f"\n¡Gracias por jugar {name}! Hasta la próxima.")
            return
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

def mostrar_palabra(word, guesses):
    return ' '.join([char if char in guesses else '_' for char in word])

def modo_juego(word, name, MAX_TURNS):
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
            print("\nEntrada no válida, Por favor, introduce una letra o una palabra.")
            continue

        if len(guesses) == 1:
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
            print("\nEntrada no válida. Por favor, introduce una letra o la palabra completa.")
        
        if turns == 0:
            print(f"\n¡Perdiste! La palabra era: {word}")
            reiniciar_juego(name)
            return
        
def modo_ruleta(word, guess, name):
    if guess == word:
        print(f"\n¡Felicidades {name}, adivinaste la palabra!")
        reiniciar_juego(name)
    else: 
        print(f"\nIncorrecto. La palabra era: {word}")

    reiniciar_juego(name)

def validar_entrada(entrada, tipo):
    if tipo == 'letra' and len(entrada) == 1 and entrada.isalpha():
        return True
    elif tipo == 'palabra' and len(entrada) > 1 and entrada.isalpha():
        return True
    return False

if __name__ == "__main__":
    iniciar_juego()

# Fallos
# El modo normal no funciona correctamente
