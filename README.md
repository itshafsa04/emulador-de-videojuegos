# Juego del Número 21 (21Number)

## Descripción 
El **Juego del Número 21** es un juego de estrategia en el que los jugadores intentan alcanzar exactamente 21 puntos. Si un jugador se pasa de 21 o dice el número 21, pierde el juego. Este proyecto implementa el juego en Python, permitiendo jugar contra la máquina o entre dos jugadores.

## Modos de Juego
El juego ofrece dos modos principales:

### 1. Contra la Máquina
- El jugador puede elegir tomar el primer turno (`F`) o el segundo turno (`S`).
- La máquina utiliza una estrategia para intentar ganar el juego.
- El jugador debe ingresar números consecutivos en su turno.
- El juego continúa hasta que uno de los jugadores diga el número 21.

### 2. Entre Dos Jugadores
- Dos jugadores toman turnos para ingresar números consecutivos.
- El jugador que diga el número 21 pierde el juego.
- Si los números ingresados no son consecutivos, el jugador pierde automáticamente.

## Cómo Jugar
1. Ejecuta el script `numero_21.py`.
2. Selecciona el modo de juego:
   - `1` para jugar contra la máquina.
   - `2` para jugar entre dos personas.
3. Sigue las instrucciones en pantalla para ingresar los números.
4. Disfruta del juego y trata de no perder.

## Características Adicionales
- **Validación de Entradas**: El juego valida que los números ingresados sean consecutivos y estén dentro del rango permitido.
- **Reinicio o Salida**: Al final de cada partida, los jugadores pueden optar por reiniciar el juego o salir.
## Código
El código del juego está organizado en varias funciones para facilitar su comprensión y mantenimiento:

- **`nearest_multiple(num)`**: Devuelve el múltiplo más cercano de 4.
- **`lose()`**: Termina el juego con un mensaje de derrota y da la opción de reiniciar.
- **`check_consecutive(sequence)`**: Verifica si los números ingresados son consecutivos.
- **`get_valid_input(prompt, min_val, max_val)`**: Valida la entrada del usuario.
- **`player_turn(sequence, last, player_name, previous_count=None)`**: Maneja el turno del jugador, considerando las reglas avanzadas.
- **`computer_turn(sequence, last, comp_count)`**: Maneja el turno de la máquina.
- **`start_game_vs_computer()`**: Implementa el modo de juego contra la máquina.
- **`start_game_vs_player()`**: Implementa el modo de juego entre dos jugadores.
- **`reiniciar_o_salir()`**: Pregunta al usuario si desea reiniciar el juego o salir.
- **`game_description()`**: Muestra una descripción detallada del juego.
- **`main()`**: Bucle principal del juego que gestiona el menú y las opciones seleccionadas.

## Instalación
Para ejecutar este juego, necesitas tener Python instalado en tu sistema. Puedes descargar Python desde [python.org](https://www.python.org/).

### Pasos de Instalación:
1. Clona este repositorio o descarga el archivo `numero_21.py`:
   ```bash
   git clone https://github.com/tu_usuario/emulador-de-videojuegos.git