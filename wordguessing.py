# Juego de Adivinanza de Palabras

# Importar libreria random
import random

def iniciar_juego():
    # Obtener nombre del usuario y saludar
    name = input("\n¿Cuál es tu nombre? ")
    print("\nHola", name, "¡Bienvenido al juego de adivina la palabra!")
    print("\n¡Vamos a jugar!\n")

    # Lista de palabras y elegir una al azar
    words = ['python', 'java', 'html', 'jugador', 'programador', 'computadora', 'teclado', 'raton', 'pantalla', 'agua', 'luz','sombra', 'cielo', 'tierra', 'mar', 'viento', 'fuego', 'nube', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'espacio', 'tiempo', 'historia', 'ciencia', 'arte', 'musica', 'danza', 'teatro', 'cine', 'literatura', 'poesia', 'filosofia', 'matematica', 'geografia', 'biologia', 'quimica', 'fisica', 'verano', 'invierno', 'primavera', 'otoño', 'calor', 'frio', 'lluvia', 'nieve', 'viento', 'tormenta', 'relampago', 'trueno', 'rayo', 'nube', 'cielo', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'inteligencia', 'artificial', 'robot', 'computadora', 'tecnologia', 'internet', 'redes', 'sociales', 'comunicacion', 'informacion', 'datos', 'programacion', 'software', 'hardware', 'sistema', 'red', 'servidor', 'cliente', 'nube', 'almacenamiento', 'seguridad', 'ciberseguridad', 'hackeo', 'virus', 'malware', 'phishing', 'spam', 'firewall', 'antivirus', 'encriptacion', 'autenticacion', 'contraseña']
    word = random.choice(words)

    # El usuario debe adivinar la palabra
    print("\n\nAdivina la palabra: (escribe las letras en minúsculas)")
    print("\nLa palabra tiene", len(word), "letras")
    print("\n====Reglas del juego==")
    print("· Tienes", 12, "intentos para adivinar la palabra")
    print("· Si adivinas la palabra, ganas")
    print("· Si no adivinas la palabra, pierdes")
    print("· Recuerda que solo puedes usar letras minúsculas y no puedes usar números ni caracteres especiales")
    print("· Si escribes una letra que ya has adivinado, no perderás un intento")
    print("· Si escribes una letra que no esté en la palabra, perderás un intento")
    print("· Si escribes un número o un carácter especial, perderás un intento")
    print("· Si escribes una letra mayúscula, perderás un intento")
    print("=====================")
    print("\n¡Buena suerte!\n")

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
            while True:
                change_mode = input("\n¿Quieres cambiar de modo? (si/no): ").strip().lower()
                if change_mode == 'si':
                    seleccionar_modo()
                    break
                elif change_mode == 'no':
                    print("\nSiguiendo en modo normal...")
                    iniciar_juego()
                    break
                else:
                    print("\nPor favor, responde con 'si' o 'no'.")
        elif restart == 'no':
            print("\n¡Hasta la próxima!")
            break
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

def la_ruleta():
    # Obtener nombre del usuario y saludar
    name = input("\n¿Cuál es tu nombre? ")
    print("\nHola", name, "¡Bienvenido a la ruleta!")

    # Lista de palabras y elegir una al azar
    words = ['python', 'java', 'html', 'jugador', 'programador', 'computadora', 'teclado', 'raton', 'pantalla', 'agua', 'luz','sombra', 'cielo', 'tierra', 'mar', 'viento', 'fuego', 'nube', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'espacio', 'tiempo', 'historia', 'ciencia', 'arte', 'musica', 'danza', 'teatro', 'cine', 'literatura', 'poesia', 'filosofia', 'matematica', 'geografia', 'biologia', 'quimica', 'fisica', 'verano', 'invierno', 'primavera', 'otoño', 'calor', 'frio', 'lluvia', 'nieve', 'viento', 'tormenta', 'relampago', 'trueno', 'rayo', 'nube', 'cielo', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'inteligencia', 'artificial', 'robot', 'computadora', 'tecnologia', 'internet', 'redes', 'sociales', 'comunicacion', 'informacion', 'datos', 'programacion', 'software', 'hardware', 'sistema', 'red', 'servidor', 'cliente', 'nube', 'almacenamiento', 'seguridad', 'ciberseguridad', 'hackeo', 'virus', 'malware', 'phishing', 'spam', 'firewall', 'antivirus', 'encriptacion', 'autenticacion', 'contraseña']
    word = random.choice(words)

    # El usuario debe adivinar la palabra
    print("\n\nAdivina la palabra completa: (escribe las letras en minúsculas)")
    print("\nLa palabra tiene", len(word), "letras")
    print("\n==Reglas del juego==")
    print("· Tienes 1 intento para adivinar la palabra completa")
    print("· Si adivinas la palabra, ganas")
    print("· Si no adivinas la palabra, pierdes")
    print("· Recuerda que solo puedes usar letras minúsculas y no puedes usar números ni caracteres especiales")
    print("=======================")
    print("\n¡Buena suerte!\n")

    # Inicializar variables
    print(" ".join("_" for _ in word))

    # Pedir al usuario que adivine la palabra completa
    guess = input("\nAdivina la palabra: ")

    # Comprobar si la palabra es correcta
    if guess == word:
        print("\n¡Has ganado! La palabra era:", word)
    else:
        print("\nHas perdido. La palabra era:", word)
        print("\nFin del juego")
    
    # Preguntar al usuario si desea jugar de nuevo o salir
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            while True:
                change_mode = input("\n¿Quieres cambiar de modo? (si/no): ").strip().lower()
                if change_mode == 'si':
                    seleccionar_modo()
                    break
                elif change_mode == 'no':
                    print("\nSiguiendo en modo ruleta...")
                    la_ruleta()
                    break
                else:
                    print("\nPor favor, responde con 'si' o 'no'.")
        elif restart == 'no':
            print("\n¡Hasta la próxima!")
            break
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

def seleccionar_modo():
    # Preguntar al usuario qué modo desea jugar
    while True:
        modo = input("\n¿Quieres jugar en modo normal o en modo ruleta? (normal/ruleta): ").strip().lower()
        if modo == 'normal':
            print("\nIniciando el juego en modo normal...")
            iniciar_juego()
            break
        elif modo == 'ruleta':
            print("\nIniciando el juego en modo ruleta...")
            la_ruleta()
            break
        else:
            print("\nPor favor, responde con 'normal' o 'ruleta'.")
        
# Función principal para iniciar el juego
if __name__ == "__main__":
    # Preguntar al usuario qué modo desea jugar
    while True:
        modo = input("\n¿Quieres jugar en modo normal o en modo ruleta? (normal/ruleta): ").strip().lower()
        if modo == 'normal':
            print("\nIniciando el juego en modo normal...")
            iniciar_juego()
            break
        elif modo == 'ruleta':
            print("\nIniciando el juego en modo ruleta...")
            la_ruleta()
            break
        else:
            print("\nPor favor, responde con 'normal' o 'ruleta'.")