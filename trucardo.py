import random
#trucardo
# Definimos los palos y los valores de las cartas
palos = ['Espadas', 'Bastos', 'Oros', 'Copas']
valores = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']

# Definimos la jerarquía de las cartas en el Truco
jerarquia = {
    '1 Espadas': 14,
    '1 Bastos': 13,
    '7 Espadas': 12,
    '7 Oros': 11,
    '3': 10,
    '2': 9,
    '1': 8,
    '12': 7,
    '11': 6,
    '10': 5,
    '7': 4,
    '6': 3,
    '5': 2,
    '4': 1
}

# Creamos el mazo de cartas
mazo = []
for i in palos:
    for j in valores:
        carta = j+' de '+i
        mazo.append(carta)

# Función para barajar y repartir las cartas
def repartir_cartas():
    random.shuffle(mazo)
    mano_jugador1 = []
    mano_jugador2 = []
    '''cartas jugador 1'''
    mano_jugador1.append(mazo[0])
    mano_jugador1.append(mazo[1])
    mano_jugador1.append(mazo[2])
    '''cartas jugador 2'''
    mano_jugador2.append(mazo[3])
    mano_jugador2.append(mazo[4])
    mano_jugador2.append(mazo[5])
    return mano_jugador1, mano_jugador2

# Función para determinar el ganador de una ronda
def determinar_ganador(carta1, carta2):
    valor_carta1 = jerarquia.get(carta1.split()[0], 0)
    valor_carta2 = jerarquia.get(carta2.split()[0], 0)
    if valor_carta1 > valor_carta2:
        return "Jugador 1"
    elif valor_carta2 > valor_carta1:
        return "Jugador 2"
    else:
        return "Empate"

# Función principal del juego
def jugar_truco():
    mano_jugador1 = repartir_cartas()
    mano_jugador2 = repartir_cartas()
    
    # print(f"Jugador 1 tiene: {mano_jugador1}")
    # print(f"Jugador 2 tiene: {mano_jugador2}")
    
    # Jugar una ronda simple (primera carta de cada jugador)
    # ganador = determinar_ganador(mano_jugador1[0], mano_jugador2[0])
    # print(f"Jugador 1 juega: {mano_jugador1[0]}")
    # print(f"Jugador 2 juega: {mano_jugador2[0]}")
    # print(f"El ganador de la ronda es: {ganador}")

# Ejecutar el juego
jugar_truco()
