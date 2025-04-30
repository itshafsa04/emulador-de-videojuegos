import random

# List of fruits and animals
frutas = [
    'apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'nectarine',
    'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon'
]

animales = [
    'cat', 'dog', 'elephant', 'giraffe', 'hippopotamus', 'kangaroo', 'lion', 'monkey', 'penguin', 'rabbit',
    'squirrel', 'tiger', 'zebra', 'alligator', 'bear', 'cheetah', 'dolphin', 'flamingo', 'gorilla', 'hedgehog'
]

someWords = frutas + animales
historial_juegos = []

def elegir_palabra(dificultad):
    """Selecciona una palabra aleatoria de la lista según la dificultad."""
    if dificultad == 'fácil':
        palabras_filtradas = [palabra for palabra in someWords if len(palabra) <= 5]
    elif dificultad == 'medio':
        palabras_filtradas = [palabra for palabra in someWords if 6 <= len(palabra) <= 8]
    else:  # difícil
        palabras_filtradas = [palabra for palabra in someWords if len(palabra) > 8]
    return random.choice(palabras_filtradas)

def mostrar_palabra(palabra, letras_adivinadas):
    """Muestra la palabra con las letras adivinadas y guiones bajos para las no adivinadas."""
    display = [char if char in letras_adivinadas else '_' for char in palabra]
    print(' '.join(display))

def obtener_adivinanza():
    """Obtiene una letra o palabra adivinada del usuario."""
    while True:
        adivinanza = input('Enter a letter or the entire word to guess: ').lower()
        if len(adivinanza) == 1 and not adivinanza.isalpha():
            print('Enter only a LETTER')
        elif len(adivinanza) > 1 and not adivinanza.isalpha():
            print('Enter only LETTERS')
        else:
            return adivinanza

def jugar(dificultad):
    """Función principal para jugar al juego de Hangman."""
    palabra = elegir_palabra(dificultad)
    letras_adivinadas = set()
    oportunidades = len(palabra) + 2
    print('Guess the word! HINT: word is a name of a fruit or an animal')
    mostrar_palabra(palabra, letras_adivinadas)

    while oportunidades > 0:
        adivinanza = obtener_adivinanza()
        if len(adivinanza) == 1:
            if adivinanza in letras_adivinadas:
                print('You have already guessed that letter')
                continue

            letras_adivinadas.add(adivinanza)
            if adivinanza in palabra:
                print(f'Good guess! {adivinanza} is in the word.')
            else:
                print(f'Sorry, {adivinanza} is not in the word.')
                oportunidades -= 1

            mostrar_palabra(palabra, letras_adivinadas)

            if all(char in letras_adivinadas for char in palabra):
                print('Congratulations, You won!')
                historial_juegos.append({'palabra': palabra, 'resultado': 'ganado'})
                break
        else:
            if adivinanza == palabra:
                print('Congratulations, You won!')
                historial_juegos.append({'palabra': palabra, 'resultado': 'ganado'})
                break
            else:
                print(f'Sorry, {adivinanza} is not the word.')
                oportunidades -= 1

        if oportunidades == 0:
            print(f'You lost! The word was {palabra}')
            historial_juegos.append({'palabra': palabra, 'resultado': 'perdido'})

def mostrar_instrucciones():
    """Muestra las instrucciones del juego."""
    print("\nInstrucciones del Juego:")
    print("1. El objetivo es adivinar la palabra secreta letra por letra o adivinando la palabra completa.")
    print("2. Tienes un número limitado de oportunidades para adivinar.")
    print("3. Cada vez que adivinas una letra correctamente, se revela en la palabra.")
    print("4. Si adivinas todas las letras o la palabra completa antes de que se acaben las oportunidades, ganas.")
    print("5. Si se acaban las oportunidades antes de adivinar la palabra completa, pierdes.")

def mostrar_historial():
    """Muestra el historial de juegos jugados."""
    print("\nHistorial de Juegos:")
    if not historial_juegos:
        print("No hay juegos en el historial.")
    else:
        for juego in historial_juegos:
            print(f"Palabra: {juego['palabra']}, Resultado: {juego['resultado']}")

def mostrar_estadisticas():
    """Muestra las estadísticas del jugador."""
    juegos_ganados = sum(1 for juego in historial_juegos if juego['resultado'] == 'ganado')
    juegos_perdidos = sum(1 for juego in historial_juegos if juego['resultado'] == 'perdido')
    total_juegos = len(historial_juegos)
    porcentaje_exito = (juegos_ganados / total_juegos * 100) if total_juegos > 0 else 0

    print("\nEstadísticas del Jugador:")
    print(f"Juegos ganados: {juegos_ganados}")
    print(f"Juegos perdidos: {juegos_perdidos}")
    print(f"Porcentaje de éxito: {porcentaje_exito:.2f}%")

def menu_principal():
    """Función para mostrar el menú principal y manejar la selección del usuario."""
    while True:
        print("\nMenú de Juegos")
        print("1. Jugar Hangman")
        print("2. Mostrar Instrucciones")
        print("3. Mostrar Historial de Juegos")
        print("4. Mostrar Estadísticas del Jugador")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            while True:
                print("\nSelecciona la dificultad")
                print("1. Fácil")
                print("2. Medio")
                print("3. Difícil")
                print("4. Volver al menú principal")
                dificultad_opcion = input("Selecciona una opción: ")

                if dificultad_opcion == '1':
                    jugar('fácil')
                elif dificultad_opcion == '2':
                    jugar('medio')
                elif dificultad_opcion == '3':
                    jugar('difícil')
                elif dificultad_opcion == '4':
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
        elif opcion == '2':
            mostrar_instrucciones()
        elif opcion == '3':
            mostrar_historial()
        elif opcion == '4':
            mostrar_estadisticas()
        elif opcion == '5':
            print("¡Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    try:
        menu_principal()
    except KeyboardInterrupt:
        print('\n¡Adiós! Intenta de nuevo.')
