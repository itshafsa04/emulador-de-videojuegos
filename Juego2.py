# Juego de Adivinanza de Palabras

# Importar libreria random
import random

def iniciar_juego():
    # Obtener nombre del usuario y saludar
    name = input("\n¿Cuál es tu nombre? ")
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

    # El usuario debe adivinar la palabra
    print("\n\nAdivina la palabra: (escribe la letra en minúsculas)")

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
                print("_", end=' ')
                failed += 1

        print()

        # Si no quedan caracteres por adivinar, el usuario gana
        if failed == 0:
            print("\nHas Ganado!!!")
            print("\nLa palabra es: ", word)
            break

        # Pedir al usuario que adivine un caracter
        guess = input("\nAdivina una letra: ")
        guesses += guess

        # Comprobar si el caracter no está en la palabra
        if guess not in word:
            turns -= 1
            print("\nIncorrecta")
            print("\nTe quedan", turns, 'intentos')

        # Comprobar si el usuario ha agotado los turnos
        if turns == 0:
            print("\nHas perdido :(")
            print("\nLa palabra era: ", word)
            break

    # Fin del juego
    print("\nFin del juego")
    print("\nGracias por jugar")
    print("\nHasta la próxima :)")

    # Preguntar al usuario si desea jugar de nuevo o salir
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            print("\nReiniciando el juego...")
            iniciar_juego()
        elif restart == 'no':
            print("\n¡Hasta la próxima!")
            break
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

# Iniciar el juego por primera vez
iniciar_juego()
# Fin del juego