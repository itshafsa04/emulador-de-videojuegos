# Importar libreria random
import random

# Obtener nombre del usuario y saludar
name = input("\n¿Cual es tu nombre? ")
print("\n¡Buena Suerte! ", name)

# Lista de palabras y elegir una al azar
words = ['python', 'java', 'html', 'jugador', 'programador', 'computadora', 'teclado', 'raton', 'pantalla', 'agua', 'luz',
        'sombra', 'cielo', 'tierra', 'mar', 'viento', 'fuego', 'nube', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 
        'universo', 'cosmos', 'espacio', 'tiempo', 'historia', 'ciencia', 'arte', 'musica', 'danza', 'teatro', 'cine', 
        'literatura', 'poesia', 'filosofia', 'matematica', 'geografia', 'biologia', 'quimica', 'fisica', 'verano', 'invierno', 
        'primavera', 'otoño', 'calor', 'frio', 'lluvia', 'nieve', 'viento', 'tormenta', 'relampago', 'trueno', 'rayo', 'nube', 
        'cielo', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'inteligencia', 'artificial', 'robot', 
        'computadora', 'tecnologia', 'internet', 'redes', 'sociales', 'comunicacion', 'informacion', 'datos', 'programacion', 
        'software', 'hardware', 'sistema', 'red', 'servidor', 'cliente', 'nube', 'almacenamiento', 'seguridad', 'ciberseguridad', 
        'hackeo', 'virus', 'malware', 'phishing', 'spam', 'firewall', 'antivirus', 'encriptacion', 'autenticacion', 'contraseña']

word = random.choice(words)

# El usuario deve adivinar la palabra
print("\n\nAdivina la palabra: (escribelo en minúsculas)")

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
            print("\n_")
            failed += 1

    # Si no quedan caracteres por adivinar, el usuario gana
    if failed == 0:
        print("\n")
        print("\nHás Ganado!!!")
        print("\nLa palara es: ", word)
        print("\n")
        break

    # Pedir al usuario que adivine un caracter
    guess = input("\nAdivina la palabra: ")
    guesses += guess

    # Comprobar si el caracter no esta en la palabra
    if guess not in word:
        turns -= 1
        print("\nIncorrecta")
        print("\nTe quedan", + turns, 'intentos')

    # Comprobar si el usuario ha agotado los turnos
    if turns == 0:
        print("\nHás perdido :(")