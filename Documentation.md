# Trucardo

## Variables Constantes
### Jerarquía:
Constante en la que definimos qué carta es más alta. Utilizamos listas de listas porque no podemos utilizar objetos. Fue la mejor manera que encontramos aplicar esta lógica. 

## Funciones
### obtener_jerarquia:
Esta función espera una carta (string) y busca la carta en la lista de JERARQUIA.

### repartir_cartas:
Esta funcion recibe como parámetro un arreglo (o lista) en el cual contenga todas las cartas en juego. Luego mezcla los elementos del arreglo y devuelve dos arreglos nuevos correspondientes a la mano del jugador y a la mano de la máquina.

### determinar_ganador:
Esta función recibe dos parámetros de tipo string, correspondientes a la carta que lanza el jugador 1 y la carta que lanza el jugador dos. Esta función utiliza el método **obtener_jerarquia** para luego comparar cuál es la carta ganadora, la función devuelve quién es el ganador.

### separar_tanto:
Esta función espera un string, este corresponde a una carta el cual la función separará el número y lo convertirá en integer, y el palo de la carta. La función devuelve una nueva lista con los valores del número y el palo de la carta.

### calcular_tanto:
Esta función espera un arreglo, el cual corresponde a la mano del jugador, este arreglo puede ser de 2 elementos como mínimo. Luego, la función obtiene carta por carta, el número y el palo por separado, utilizando el método **separar_tanto**. Dentro de la función se declara la variable *tanto*, que inicialmente tiene el valor de 0, luego se redefine su valor y se devuelve finalizando la función.

### calcular_puntos:
Esta función recibe cinco parámetros:
-   Como primer parámetro debe recibir un string, que corresponde a la instancia del juego en el momento de llamar a la función (puede ser Envido, Real Envido, Truco, etc.).
-   Como segundo parámetro debe recibir un valor booleano, que indica que el jugador acepte o no acepte el juego cantado para así calcular el puntaje.
-   Como tercer parámetro debe recibir un número entero que se utilizará para sumar los puntos del jugador 1.
-   Como cuarto parámetro debe recibir otro número entero que se uitlizará para sumar los puntos del jugador 2.
-   Como quinto parámetro debe recibir un string, que indicaría a qué jugador se le suman los puntos.