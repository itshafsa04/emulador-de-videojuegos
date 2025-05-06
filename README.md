# Emulador de Videojuegos

## Descripción
Este emulador de videojuegos contiene 4 juegos:
- Adivina el número
- Adivina la palabra
- Número 21
- Ahorcado

## Instalación
Para instalar y configurar el proyecto, sigue estos pasos:

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/itshafsa04/emulador-de-videojuegos.git
    ```
2. **Navega al directorio del proyecto:**
    ```bash
    cd emulador-de-videojuegos
    ```
3. **Asegúrate de tener Python instalado:**
    - Puedes descargar Python desde python.org.
    - Para verificar que Python está instalado correctamente, ejecuta:
    ```bash
    python --version
    ```

## Licencia
Este proyecto está bajo la licencia Apache 2.0. Consulta el archivo `LICENSE` para más detalles.

## Juegos

### Adivina el Número

#### Descripción
Este proyecto es un juego de adivinanza de números desarrollado en Python. El objetivo del juego es proporcionar entretenimiento y desafiar a los jugadores a adivinar un número aleatorio dentro de un número limitado de intentos. Los jugadores tienen 7 oportunidades para adivinar el número correcto, que se genera aleatoriamente entre 0 y 99.

#### Uso
1. **Inicia el juego:**
    ```bash
    python main.py
    ```
2. **Jugando el juego:**
    - Introduce tus adivinanzas cuando se te solicite. El juego te indicará si tu adivinanza es mayor o menor que el número a adivinar.
    - Tienes 7 intentos para adivinar el número correcto.
3. **Final del juego:**
    - Si adivinas el número correcto, el juego te felicitará.
    - Si agotas tus intentos, el juego revelará el número correcto.

### Adivina la Palabra

#### Descripción
Este juego se basa en que el usuario debe adivinar una palabra oculta letra por letra. El juego proporciona una palabra al azar y el usuario tiene un número limitado de intentos para adivinar la palabra correcta.

#### Características
- El juego selecciona una palabra al azar de una lista predefinida.
- El usuario tiene 12 intentos para adivinar la palabra.
- El juego muestra las letras adivinadas correctamente y los intentos restantes.
- El usuario puede jugar nuevamente después de terminar la partida.


### Hangman

#### Descripción
¡Bienvenido al Juego de Hangman! Este es un juego simple de línea de comandos donde puedes adivinar los nombres de frutas y animales. Puedes adivinar la palabra letra por letra o intentar adivinar la palabra completa de una vez.

#### Características
- Adivina los nombres de frutas y animales.
- Tres niveles de dificultad: Fácil, Medio y Difícil.
- Opción para adivinar la palabra letra por letra o la palabra completa.
- Mantiene un historial de juegos y estadísticas del jugador.


### Juego del Número 21 (21Number)

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
=======

## Contribución
Para contribuir al proyecto, sigue estos pasos:

1. **Haz un fork del repositorio:**
    - En GitHub, haz clic en el botón `Fork` en la página del repositorio para crear una copia del proyecto en tu cuenta.
2. **Clona tu fork:**
    ```bash
    git clone https://github.com/itshafsa04/emulador-de-videojuegos.git
    ```
3. **Crea una nueva rama para tus cambios:**
    ```bash
    git checkout -b feature-nueva
    ```
4. **Realiza tus cambios y haz commit:**
    ```bash
    git add .
    git commit -m "Descripción de los cambios"
    ```
5. **Envía tus cambios a tu repositorio fork:**
    ```bash
    git push origin feature-nueva
    ```
6. **Abre una pull request:**
    - En GitHub, ve a la página de tu fork y haz clic en `New pull request` para solicitar que tus cambios sean añadidos al proyecto original.

## Autores
- **Hafsa El Bouslami**
- **Michael Uribe**
- **Diana Sierra**
- **Iván Jiménez**