# Emulador-de-videojuegos
Emulador de videojuegos que contiene 4 juegos en Python.

# Juego de adivinar la palabra
==Adivina la palabra==

## Descripción
Este juego se basa en que el usuario deve adivinar una palabra oculta letra por letra. El juego proporciona una palabra al azar y el usuario tiene un número limitado de intentos para adivinar la palabra correcta.

## Características
- El juego selecciona una palabra al azar de una lista predefinida.
- El usuario tiene 12 intentos para adivinar la palabra.
- El juego muestra las letras adivinadas correctamente y los intentos restantes.
- El usuario puede jugar nuevamente después de terminar la partida.
  
## Juego 2.
==21Number==

## Descripción 
El juego del número 21 es un juego de estrategia en el que los jugadores intentan alcazar exactamente 21 puntos. Si un jugador se pasa de 21 o dice el número 21, pierde el juego. Este proyecto implementa el juego en Python, permitiendo jugar contra la máquina o entre dos jugadores.

## Modos de juego
 En este juego hay dos modos de juego que son los siguientes:

- **Contra la máquina** : 
1. El jugador puede elegir tomar el primer turno (F) o el segundo turno (S).
2. La máquina seguirá una estrategia para intentar ganar el juego.
3. El jugador debe ingresar números consecutivos en su turno.
4. El juego continúa hasta que uno de los jugadores ingrese el número 21.

- **Entre dos jugadores** :
1. Cada jugador toma turnos para ingresar números consecutivos.
2. El jugador que ingrese el número 21 pierde el juego.
3. Si los números ingresados no son consecutivos, el jugador pierde el juego.

## Cómo jugar
1. Ejecuta el script numero_21.py
2. selecciona el modo de juego:
  - 1 para jugar contra la máquina.
  - 2 para jugar entre dos personas.
3. Sigue las instrucciones en pantalla para ingresar los números.
4. Disfruta del juego y trata de no perder.

## Código
El código del juego está dividida en varias funciones:
- **nearest_multiple(num): Devuelve el múltiplo más cercano de 4.**
- **lose(): Termina el juego con un mensaje de derrota yda la opción de reiniciar.**
- **check_consecutive(sequence):Verifica si los números son consecutivos.**
- **get_valid_input(prompt,min_val,max_val):Valida la entrada del usuario.**
- **player_turn(sequence, last, player_name): Maneja el turno del jugador.**
-  **computer_turn(sequence, last, comp_count): Maneja el turno de la máquina.**
- **start_game_vs_computer(): Juego contra la máquina.**
- **start_game_vs_player(): Juego entre dos jugadores.**
- **reiniciar_o_salir(): Pregunta al usuario si desea reiniciar o salir.**
- **main(): Bucle principal del juego.**





## Instalación
Para ejecutar este juego, neesitar tener Python instalado en tu sistema. Puedes descargar Python desde python.org.

1. Clona este repositorio o descarga el archivo 'wordguessing.py'.