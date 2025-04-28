# Código en Python para jugar al juego del número 21

# Devuelve el múltiplo más cercano de 4
def nearest_multiple(num):
    if num >= 4:
        return num + (4 - (num % 4))
    return 4

# Termina el juego con un mensaje de derrota y da la opción de reiniciar
def lose():
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
    for i in range(1, len(sequence)):
        if (sequence[i] - sequence[i - 1]) != 1:
            return False
    return True

# Valida la entrada del usuario
def get_valid_input(prompt, min_val, max_val):
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
    print(f"\nTurno de {player_name}.")
    num_count = get_valid_input(f"{player_name}, ¿cuántos números deseas ingresar? (1-3): ", 1, 3)
    print("Ahora ingresa los valores:")
    for _ in range(num_count):
        value = get_valid_input("> ", last + 1, last + 3)
        sequence.append(value)
        last = value
    print(f"Orden de entradas después del turno de {player_name}: {sequence}")
    return sequence, last

# Maneja el turno de la máquina
def computer_turn(sequence, last, comp_count):
    for _ in range(comp_count):
        sequence.append(last + 1)
        last += 1
    print("Orden de entradas después del turno de la máquina:")
    print(sequence)
    return sequence, last

# Juego contra la máquina
def start_game_vs_computer():
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
                comp_count = 4 - (len(sequence) % 4)
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

# Bucle principal del juego
def main():
    while True:
        print("Selecciona el modo de juego:")
        print("1. Jugar contra la máquina")
        print("2. Jugar entre dos personas")
        mode = input("> ").strip()

        if mode == "1":
            if not start_game_vs_computer():
                break
        elif mode == "2":
            if not start_game_vs_player():
                break
        else:
            print("Opción no válida. Por favor, selecciona '1' o '2'")

if __name__ == "__main__":
    main()
# Fin del código