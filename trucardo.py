import random
#trucardo
# Definimos los palos y los valores de las cartas
palos = ['Espadas', 'Bastos', 'Oros', 'Copas']
valores = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']

# Definimos la jerarquía de las cartas en el Truco. Debido a la limitación de objetos, nos basamos en los índices de cada arreglo para elaborar la jerarquía.
JERARQUIA = [
    ['1 de Espadas'],
    ['1 de Bastos'],
    ['7 de Espadas'],
    ['7 de Oros'],
    ['3 de Espadas', '3 de Oros', '3 de Copas', '3 de Bastos'],
    ['2 de Espadas', '2 de Oros', '2 de Copas', '2 de Bastos'],
    ['1 de Copas', '1 de Oros'],
    ['12 de Espadas', '12 de Oros', '12 de Copas', '12 de Bastos'],
    ['11 de Espadas', '11 de Oros', '11 de Copas', '11 de Bastos'],
    ['10 de Espadas', '10 de Oros', '10 de Copas', '10 de Bastos'],
    ['7 de Copas', '7 de Bastos'],
    ['6 de Espadas', '6 de Oros', '6 de Copas', '6 de Bastos'],
    ['5 de Espadas', '5 de Oros', '5 de Copas', '5 de Bastos'],
    ['4 de Espadas', '4 de Oros', '4 de Copas', '4 de Bastos']
]

""" JERARQUIA = {
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
} """

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
    valor_carta1 = JERARQUIA.get(carta1.split()[0], 0)
    valor_carta2 = JERARQUIA.get(carta2.split()[0], 0)
    if valor_carta1 > valor_carta2:
        return "Jugador 1"
    elif valor_carta2 > valor_carta1:
        return "Jugador 2"
    else:
        return "Empate"

# Función principal del juego
def jugar_truco():
    cartas = repartir_cartas()
    mano_jugador1 = cartas[0]
    mano_jugador2 = cartas[1]
    cartaJugada = ''
    # print(mano_jugador1, mano_jugador2)
    print(f"Jugador 1 tiene: {mano_jugador1}")
    while(cartaJugada != 0 and cartaJugada != 1 and cartaJugada != 2):
        cartaJugada = int(input('ingrese cual es la posicion de la carta que quiere jugar (1, 2 o 3): ')) - 1
        if(cartaJugada != 0 and cartaJugada != 1 and cartaJugada != 2):
            print('posicion no valida')
    # Jugar una ronda simple (primera carta de cada jugador)
    ganador = determinar_ganador(mano_jugador1[0], mano_jugador2[0])
    # print(f"Jugador 1 juega: {mano_jugador1[0]}")
    # print(f"Jugador 2 juega: {mano_jugador2[0]}")
    # print(f"El ganador de la ronda es: {ganador}")

# Ejecutar el juego
# jugar_truco()
