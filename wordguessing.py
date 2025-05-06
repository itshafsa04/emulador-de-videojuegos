# Juego de Adivinanza de Palabras
# Importar libreria random
import random

def iniciar_juego():
    # Obtener nombre del usuario y saludar
    name = input("\n¿Cuál es tu nombre? ")
    print(f"\nHola {name}, ¡Bienvenido al juego de adivina la palabra!")
    print("\n¡Vamos a jugar!\n")

    # Lista de palabras y elegir una al azar
    words = list(set(['python', 'java', 'html', 'jugador', 'programador', 'computadora', 'teclado', 'raton', 'pantalla', 'agua', 'luz','sombra', 'cielo', 'tierra', 'mar', 'viento', 'fuego', 'nube', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'espacio', 'tiempo', 'historia', 'ciencia', 'arte', 'musica', 'danza', 'teatro', 'cine', 'literatura', 'poesia', 'filosofia', 'matematica', 'geografia', 'biologia', 'quimica', 'fisica', 'verano', 'invierno', 'primavera', 'otoño', 'calor', 'frio', 'lluvia', 'nieve', 'viento', 'tormenta', 'relampago', 'trueno', 'rayo', 'nube', 'cielo', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'inteligencia', 'artificial', 'robot', 'computadora', 'tecnologia', 'internet', 'redes', 'sociales', 'comunicacion', 'informacion', 'datos', 'programacion', 'software', 'hardware', 'sistema', 'red', 'servidor', 'cliente', 'nube', 'almacenamiento', 'seguridad', 'ciberseguridad', 'hackeo', 'virus', 'malware', 'phishing', 'spam', 'firewall', 'antivirus', 'encriptacion', 'autenticacion', 'contraseña']))
    word = random.choice(words)

    # El usuario debe adivinar la palabra
    print(f"\n\nAdivina la palabra: ")
    print(f"\nLa palabra tiene, {len(word)} letras.")
    print("\n==Reglas del juego==")
    print("· Tienes 12 intentos para adivinar la palabra.")
    print("· Si adivinas la palabra, ganas.")
    print("· Si no adivinas la palabra, pierdes.")
    print("· Recuerda que no puedes usar números ni caracteres especiales.")
    print("====================")
    print("\n¡Buena suerte!\n")

    # Inicializar variables y turnos
    guesses = ''
    turns = 12

    # Bucle principal del juego
    while turns > 0:
        failed = 0
        print("\nPalabra: ", end=' ')
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print("_", end=' ')
                failed += 1

        # Si no quedan caracteres por adivinar, el usuario gana
        if failed == 0:
            print(f"\n\n¡Felicidades {name}, has Ganado!")
            print(f"La palabra era: {word}")
            break

        # Pedir al usuario que adivine un caracter
        guess = input("\n\nAdivina una letra: ").strip().lower()

        # Comprobar si el caracter no está en la palabra
        if not guess.isalpha() or len(guess) != 1:
            print("\nEntrada no válida. Por favor, introduce una letra.")
            continue

        if guess in guesses:
            print("\nYa has adivinado esa letra. Intenta con otra.")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("\nIncorrecta")
            print(f"Te quedan {turns} intentos.")

        # Comprobar si el usuario ha agotado los turnos
        if turns == 0:
            print(f"\nLo siento {name}, has perdido.")
            print(f"La palabra era: {word}")

    # Preguntar al usuario si desea jugar de nuevo o salir
    reiniciar_juego()

# Función para el modo ruleta
def la_ruleta():
    # Obtener nombre del usuario y saludar
    name = input("\n¿Cuál es tu nombre? ").strip()
    print(f"\nHola {name}, ¡Bienvenido al modo ruleta del juego de adivina la palabra!")
    print("\n¡Vamos a jugar!\n")

    # Lista de palabras y elegir una al azar
    words = list(set(['python', 'java', 'html', 'jugador', 'programador', 'computadora', 'teclado', 'raton', 'pantalla', 'agua', 'luz','sombra', 'cielo', 'tierra', 'mar', 'viento', 'fuego', 'nube', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'espacio', 'tiempo', 'historia', 'ciencia', 'arte', 'musica', 'danza', 'teatro', 'cine', 'literatura', 'poesia', 'filosofia', 'matematica', 'geografia', 'biologia', 'quimica', 'fisica', 'verano', 'invierno', 'primavera', 'otoño', 'calor', 'frio', 'lluvia', 'nieve', 'viento', 'tormenta', 'relampago', 'trueno', 'rayo', 'nube', 'cielo', 'estrella', 'luna', 'sol', 'planeta', 'galaxia', 'universo', 'cosmos', 'inteligencia', 'artificial', 'robot', 'computadora', 'tecnologia', 'internet', 'redes', 'sociales', 'comunicacion', 'informacion', 'datos', 'programacion', 'software', 'hardware', 'sistema', 'red', 'servidor', 'cliente', 'nube', 'almacenamiento', 'seguridad', 'ciberseguridad', 'hackeo', 'virus', 'malware', 'phishing', 'spam', 'firewall', 'antivirus', 'encriptacion', 'autenticacion', 'contraseña']))
    word = random.choice(words)

    # Generar pistas
    pista_1 = f"La palabra comienza con la letra '{word[0]}'"
    pista_2 = f"La palabra termina con la letra '{word[-1]}'"

    # Mostrar reglas del modo ruleta
    print(f"\n\nAdivina la palabra: ")
    print(f"\nLa palabra tiene, {len(word)} letras")
    print("\n==Reglas del modo ruleta==")
    print("· Solo tienes una oportunidad para adivinar la palabra completa.")
    print("· Si aciertas ganas, si fallas, pierdes.")
    print("==========================")
    print("\n¡Buena suerte!\n")

    # Mostrar pistas
    print(f"\nPista 1: {pista_1}")
    print(f"Pista 2: {pista_2}")

    # Mostrar la palabra con letras adivinadas y guiones bajos
    print("\nPalabra: ", end=' ')
    for char in word:
        print("_", end=' ')
    print("\n")

    # Pedir al usuario que adivine la palabra completa
    while True:
        guess = input("\nAdivina la palabra completa: ").strip().lower()
        if not guess.isalpha() or len(guess) != len(word):
            print("\nEntrada no válida. Por favor, introduce una palabra de la longitud correcta.")
            continue
        break

    if guess == word:
        print(f"\n¡Felicidades {name}, has Ganado!")
        print(f"La palabra era: {word}")
    
    else:
        print(f"\nLo siento {name}, has perdido.")
        print(f"La palabra era: {word}")

    # Preguntar al usuario si desea jugar de nuevo o salir
    reiniciar_juego()

def reiniciar_juego():
    while True:
        restart = input("\n¿Quieres jugar de nuevo? (si/no): ").strip().lower()
        if restart == 'si':
            seleccionar_modo()
            break
        elif restart == 'no':
            print("\n¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("\nPor favor, responde con 'si' o 'no'.")

def seleccionar_modo():
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
    seleccionar_modo()