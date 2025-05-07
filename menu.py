# Creación menu de emulador de videojuegos
def main_menu():
    while True:

        # Mostrar el menú principal
        print("\nBienvenido al emulador de videojuegos")
        print("===================================")
        print("Elige un juego para jugar:")
        print("\n==Menu principal==")
        print("1. Adivina el número")
        print("2. Adivina la palabra")
        print("3. Ahorcado")
        print("4. Número 21")
        print("5. Salir")
        print("\nPor favor, elige una opción (1-5):")
        print("===================================")
        # Solicitar al usuario que elija una opción

        choice = input("\n> ").strip()

        if choice == "1":
            print("\nIniciando el juego -Adivina el número...")
            from number import main_menu as number_main # Importar el juego de adivina el número
            number_main()

        elif choice == "2":
            print("\nIniciando el juego -Adivina la palabra...")
            from wordguessing2 import iniciar_juego as wordguessing2_main # Importar el juego de adivina la palabra
            wordguessing2_main()

        elif choice == "3":
            print("\nIniciando el juego -Ahorcado...")
            from hangman import menu_principal as hangman_main # Importar el juego de ahorcado
            hangman_main()

        elif choice == "4":
            print("\nIniciando el juego -Número 21...")
            from Number21 import main as Number21_main # Importar el juego de número 21
            Number21_main()
        
        elif choice == "5":
            print("\nSaliendo del emulador... ¡Gracias por jugar!")
            break

        # Comprobar si la opción es válida
        else:
            print("\nOpción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main_menu()
# Fin del menú principal.