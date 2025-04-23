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
def player_turn(sequence, last):
    print("\nTu turno.")
    num_count = get_valid_input("¿Cuántos números deseas ingresar? (1-3): ", 1, 3)
    print("Ahora ingresa los valores:")
    for _ in range(num_count):
        value = get_valid_input("> ", last + 1, last + 3)
        sequence.append(value)
        last = value
    return sequence, last

# Maneja el turno de la computadora
def computer_turn(sequence, last, comp_count):
    for _ in range(comp_count):
        sequence.append(last + 1)
        last += 1
    print("Orden de entradas después del turno de la computadora:")
    print(sequence)
    return sequence, last

# Inicia el juego
def start_game():
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
                sequence, last = player_turn(sequence, last)
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
                    return True

        elif chance == "S":
            comp_count = 1
            while last < 20:
                sequence, last = computer_turn(sequence, last, comp_count)
                if last == 20:
                    return lose()
                sequence, last = player_turn(sequence, last)
                if not check_consecutive(sequence):
                    print("\nNo ingresaste números consecutivos.")
                    return lose()
                near = nearest_multiple(last)
                comp_count = near - last
                if comp_count == 4:
                    comp_count = 3
            print("\n\n¡FELICITACIONES!")
            print("¡HAS GANADO!")
            return True

        else:
            print("Opción no válida. Por favor, ingresa 'F' o 'S'.")

# Bucle principal del juego
def main():
    while True:
        print("El jugador 2 es la computadora.")
        print("¿Quieres jugar al juego del número 21? (si / no)")
        ans = input("> ").strip().lower()
        if ans == "si":
            if not start_game():
                break
        elif ans == "no":
            print("¿Quieres salir del juego? (si / no)")
            nex = input("> ").strip().lower()
            if nex == "si":
                print("Estás saliendo del juego...")
                break
            elif nex == "no":
                print("Continuando...")
            else:
                print("Opción no válida.")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()