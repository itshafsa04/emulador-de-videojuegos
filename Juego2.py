# Importar libreria random
import random

# Obtener nombre del usuario y saludar
name = input("¿Cual es tu nombre? ")
print("¡Buena Suerte! ", name)

# Lista de palabras y elegir una al azar
words = ['python', 'java', 'html', 'jugador', 'programador', 'computadora', 'teclado', 'raton', 'pantalla', 'agua', 'luz', 'sombra', 'cielo', 'tierra', 'mar', 'viento', 'fuego', 'nube', 'estrella', 'luna']
word = random.choice(words)

# El usuario deve adivinar la palabra
print("Adivina la palabra: (escribelo en minúsculas)")

# Inicializar variables y turnos
guesses = ''
turns = 12

# Bucle para contar los turnos
while turns > 0:

    failed = 0
    # Mostrar la palabra con los caracteres adivinados
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_")
            failed += 1

    # Si no quedan caracteres por adivinar, el usuario gana
    if failed == 0:
        print("Haz Ganado!!!")
        print("The word is: ", word)
        break

    # Pedir al usuario que adivine un caracter
    guess = input("Adivina la palabra: ")
    guesses += guess

    # Comprobar si el caracter no esta en la palabra
    if guess not in word:
        turns -= 1
        print("Incorrecta")
        print("Te quedan", + turns, 'más intentos')

    # Comprobar si el usuario ha agotado los turnos
    if turns == 0:
        print("Haz perdido :(")