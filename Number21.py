# Código en Python para jugar al juego del número 21

# Devuelve el múltiplo más cercano de 4
def nearest_multiple(num, base=4):
    """Devuelve el múltiplo más cercano del número base."""
    if num >= base:
        return num + (base - (num % base))
    return base

# Termina el juego con un mensaje de derrota y da la opción de reiniciar
def lose():
    """Muestra un mensaje de derrota y pregunta si se desea reiniciar."""
    print("\n\n¡HAS PERDIDO!")
    print("¡Mejor suerte la próxima vez!")
    while True:
        restart = input("¿Quieres reiniciar el juego? (si / no): ").strip().lower()
        if restart == "si":
            return True  # Reinicia el juego
        elif restart == "no":
            print("Saliendo del juego...")
            return False  # Sale del juego
        else:
            print("Opción no válida. Por favor, ingresa 'si' o 'no'.")

# Verifica si los números son consecutivos
def check_consecutive(sequence):
    """Verifica si los números en la secuencia son consecutivos."""
    for i in range(1, len(sequence)):
        if (sequence[i] - sequence[i - 1]) != 1:
            return False
    return True

# Valida la entrada del usuario
def get_valid_input(prompt, min_val, max_val):
    """Solicita al usuario un número válido dentro de un rango."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Por favor, ingresa un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

# Maneja el turno del jugador
def player_turn(sequence, last, player_name):
    """Maneja el turno del jugador."""
    print(f"\nTurno de {player_name}.")
    num_count = get_valid_input(f"{player_name}, ¿cuántos números deseas ingresar? (1-3): ", 1, 3)
    print("Ahora ingresa los valores:")
    for _ in range(num_count):
        value = get_valid_input("> ", last + 1, last + 3)
        sequence.append(value)
        last = value
    print(f"Orden de entradas después del turno de {player_name}: {sequence}")
    return sequence, last

# Selecciona la dificultad del juego
def select_difficulty():
    """Permite al usuario seleccionar la dificultad del juego."""
    while True:
        print("\nSelecciona la dificultad:")
        print("1. Fácil")
        print("2. Medio")
        print("3. Difícil")
        difficulty = input("> ").strip()
        if difficulty in ["1", "2", "3"]:
            return difficulty
        print("Opción no válida. Por favor, selecciona una opción válida.")

# Maneja el turno de la máquina
def computer_turn(sequence, last, comp_count):
    """Maneja el turno de la máquina."""
    print("\nTurno de la máquina:")
    for _ in range(comp_count):
        sequence.append(last + 1)
        last += 1
    print(f"Orden de entradas después del turno de la máquina: {sequence}")
    return sequence, last

# Juego contra la máquina con dificultad
def start_game_vs_computer():
    """Inicia el juego contra la máquina con la dificultad seleccionada."""
    difficulty = select_difficulty()
    sequence = []
    last = 0
    while True:
        print("Ingresa 'F' para tomar el primer turno.")
        print("Ingresa 'S' para tomar el segundo turno.")
        chance = input("> ").strip().upper()

        if chance == "F":
            while True:
                if last == 20:
                    return lose()
                sequence, last = player_turn(sequence, last, "Jugador")
                if not check_consecutive(sequence):
                    print("\nNo ingresaste números consecutivos.")
                    return lose()
                if last == 21:
                    return lose()
                # Ajusta la estrategia de la máquina según la dificultad
                if difficulty == "1":  # Fácil
                    comp_count = 1
                elif difficulty == "3":  # Difícil
                    comp_count = 4 - (len(sequence) % 4)
                else:  # Medio (por defecto)
                    comp_count = 2
                sequence, last = computer_turn(sequence, last, comp_count)
                if last == 21:
                    print("\n\n¡FELICITACIONES!")
                    print("¡HAS GANADO!")
                    return reiniciar_o_salir()

        elif chance == "S":
            comp_count = 1
            while last < 20:
                sequence, last = computer_turn(sequence, last, comp_count)
                if last == 20:
                    return lose()
                sequence, last = player_turn(sequence, last, "Jugador")
                if not check_consecutive(sequence):
                    print("\nNo ingresaste números consecutivos.")
                    return lose()
                near = nearest_multiple(last)
                comp_count = near - last
                if comp_count == 4:
                    comp_count = 3
            print("\n\n¡FELICITACIONES!")
            print("¡HAS GANADO!")
            return reiniciar_o_salir()

        else:
            print("Opción no válida. Por favor, ingresa 'F' o 'S'.")

# Juego entre dos jugadores
def start_game_vs_player():
    """Inicia el juego entre dos jugadores."""
    sequence = []
    last = 0
    player1 = input("Ingresa el nombre del Jugador 1: ").strip()
    player2 = input("Ingresa el nombre del Jugador 2: ").strip()
    current_player = player1

    while True:
        print(f"\nTurno de {current_player}.")
        sequence, last = player_turn(sequence, last, current_player)
        if not check_consecutive(sequence):
            print(f"\n{current_player}, no ingresaste números consecutivos.")
            print(f"¡{current_player} ha perdido!")
            return lose()
        if last == 21:
            print(f"\n{current_player} dijo '21'.")
            print(f"¡{current_player} ha perdido!")
            return lose()
        current_player = player1 if current_player == player2 else player2

# Pregunta al usuario si desea reiniciar o salir
def reiniciar_o_salir():
    """Pregunta al usuario si desea reiniciar el juego o salir."""
    while True:
        print("\n¿Deseas reiniciar el juego o salir?")
        print("1. Reiniciar")
        print("2. Salir")
        choice = input("> ").strip()

        if choice == "1":
            return True  # Reinicia el juego
        elif choice == "2":
            print("Saliendo del juego...")
            return False  # Sale del juego
        else:
            print("Opción no válida. Por favor, selecciona '1' o '2'.")

# Muestra la descripción del juego
def game_description():
    """Muestra una descripción del juego y sus reglas."""
    print("\n=== Descripción del Juego ===")
    print("El juego del número 21 es un juego de estrategia en el que los jugadores intentan alcanzar exactamente 21 puntos.")
    print("Si un jugador se pasa de 21 o dice el número 21, pierde el juego.")
    print("\n=== Cómo Jugar ===")
    print("1. Puedes jugar contra la máquina o contra otro jugador.")
    print("2. En cada turno, puedes ingresar entre 1 y 3 números consecutivos.")
    print("3. El jugador que diga el número 21 pierde.")
    print("4. Si los números ingresados no son consecutivos, el jugador pierde automáticamente.")
    print("=============================\n")

# Bucle principal del juego
def main():
    """Bucle principal del juego que muestra el menú principal."""
    while True:
        print("\n=== Menú Principal ===")
        print("1. Jugar contra la máquina")
        print("2. Jugar entre dos personas")
        print("3. Descripción del juego")
        print("4. Salir del juego")
        print("=======================")
        mode = input("Selecciona una opción: ").strip()

        if mode == "1":
            if not start_game_vs_computer():
                continue
        elif mode == "2":
            if not start_game_vs_player():
                continue
        elif mode == "3":
            game_description()
        elif mode == "4":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

if __name__ == "__main__":
    main()
# Fin del juego del número 21
# Hecho por [Iván Jiménez]
