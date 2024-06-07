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

# Función para definir la jerarquía de las cartas.
def obtener_jerarquia(carta):
    for i in range(len(JERARQUIA)):
        for j in range(len(JERARQUIA[i])):
            if JERARQUIA[i][j] == carta:
                return i
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
    valor_carta1 = obtener_jerarquia(carta1)
    valor_carta2 = obtener_jerarquia(carta2)
    # valor_carta1 = JERARQUIA.get(carta1.split()[0], 0)
    # valor_carta2 = JERARQUIA.get(carta1.split()[0], 0)
    if valor_carta1 < valor_carta2:  #Como utilizamos los índices para determinar cuál es la carta más alta, cuanto más bajo el número del valor, más alto es el valor de la carta.
        return "Jugador 1"
    elif valor_carta2 < valor_carta1:
        return "Jugador 2"
    else:
        return "Empate"

# Función para descartar la carta jugada.
def carta_jugada(carta, mazo):
    while len(mazo) > 0 and len(carta) > 0:
        for i in range(len(mazo)):
            if carta == mazo[i]:
                cartasEnMano = mazo
                mazo.remove(carta)
                return cartasEnMano
            else:
                return 'Error, se esperaba que ingrese la carta jugada y la mano del jugador.'
    else:
        return 'Error inesperado, se esperaba un dato tipo String y un Arreglo.'
    

# Función para separar el tanto recibido, devuelve número como integer y el palo de la carta.
def separar_tanto(string):
    numero = ''
    palo = ''
    
    partes = string.split(' de ')
    numero = int(partes[0])
    palo = partes[1]

    return [numero, palo]

# Función para calcular el tanto de la mano.
def calcular_tanto(cartas):
    while len(cartas) >= 2: 
        num = []
        palo = []
        # separamos los números y los palos
        for i in range(len(cartas)):
            naipe = separar_tanto(cartas[i])
            num.append(naipe[0])
            palo.append(naipe[1])

        tanto = 0

        # Caso particular de que las 3 cartas sean del mismo palo ya que no se utiliza la flor.
        if palo[0] == palo[1] == palo[2]:
            masAlta1 = num[0]
            masAlta2 = num[1]
            if num[1] > masAlta1:
                masAlta1 = num[1]
                masAlta2 = num[0]
            if num[2] > masAlta1:
                masAlta2 = masAlta1
                masAlta1 = num[2]
            elif num[2] > masAlta2:
                masAlta2 = num[2]
                tanto = masAlta1 + masAlta2
                return tanto
        
        # Caso 1: Dos cartas del mismo palo y sin figuras
        if palo[0] == palo[1] and num[0] < 10 and num[1] < 10:
            tanto = 20 + num[0] + num[1]
        elif palo[0] == palo[2] and num[0] < 10 and num[2] < 10:
            tanto = 20 + num[0] + num[2]
        elif palo[1] == palo[2] and num[1] < 10 and num[2] < 10:
            tanto = 20 + num[1] + num[2]

        # Caso 2 Dos cartas del mismo palo y con almenos una figura
    
        elif palo[0] == palo[1]:
            if num[0] > 10 and num[1] > 10:
                tanto = 20
            elif num[0] > 10:
                tanto = 20 + num[1]
            elif num[1] > 10:
                tanto = 20 + num[0]
        elif palo[0] == palo[2]:
            if num[0] > 10 and num[2] > 10:
                tanto = 20
            elif num[0] > 10:
                tanto = 20 + num[2]
            elif num[2] > 10:
                tanto = 20 + num[0]
        elif palo[1] == palo[2]:
            if num[1] > 10 and num[2] > 10:
                tanto = 20
            elif num[1] > 10:
                tanto = 20 + num[2]
            elif num[2] > 10:
                tanto = 20 + num[1]

        # Caso 3 Ningún par de cartas del mismo palo
        else:
            if num[0] < 10 and num[0] >= num[1] and num[0] >= num[2]:
                tanto = num[0]
            elif num[1] < 10 and num[1] >= num[0] and num[1] >= num[2]:
                tanto = num[1]
            elif num[2] < 10 and num[2] >= num[0] and num[2] >= num[1]:
                tanto = num[2]
            
        return tanto
    else:
        print('Error, se esperaba un arreglo de dos o más cartas')
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
jugar_truco()
