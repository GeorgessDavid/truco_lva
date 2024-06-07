import random
#trucardo
# Definimos los palos y los valores de las cartas
turno = 1
puntosjugador1 = 0
puntosjugador2 = 0
ganadorUltimaRonda = 'Jugador 1' #Default Jugador 1
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
    mazo.remove(mazo[0])
    mazo.remove(mazo[1])
    mazo.remove(mazo[2])
    mazo.remove(mazo[3])
    mazo.remove(mazo[4])
    mazo.remove(mazo[5])
    return [mano_jugador1, mano_jugador2]



def determinar_ganador(carta1, carta2):
    valor_carta1 = 0
    valor_carta2 = 0
    # Función para determinar el ganador de una ronda
    for i in range(len(JERARQUIA)):
        for j in range(len(JERARQUIA[i])):
            if carta1 == JERARQUIA[i][j]:
                valor_carta1 = i

    # Encontrar índice de carta2
    for i in range(len(JERARQUIA)):
        for j in range(len(JERARQUIA[i])):
            if carta2 == JERARQUIA[i][j]:
                valor_carta2 = i
    
    # Devolver el mayor índice
    if valor_carta1 < valor_carta2:
        return "Jugador 1"
    elif valor_carta2 < valor_carta1:
        return "Jugador 2"
    else:
        return "Empate"

def calcular_puntos(juego, seQuiere):
    puntos = 0
    if (juego == 'truco'):
        if(seQuiere == True):
            puntos = 2
        else:
            puntos = 1
    elif(juego == 'retruco'):
        if(seQuiere == True):
            puntos = 3
        else:
            puntos = 2
    elif(juego == 'vale cuatro'):
        if(seQuiere == True):
            puntos = 4
        else:
            puntos = 3
    elif(juego == 'envido'):
        if(seQuiere == True):
            puntos = 2
        else:
            puntos = 1
    elif(juego == 'real envido'):
        if(seQuiere == True):
            puntos = 4
        else:
            puntos = 1
    elif(juego == 'falta envido'):
        if(seQuiere == True):
            puntos = 999
        else:
            puntos = 1
    
    return puntos

# Función principal del juego
def jugar_truco():
    cartas = repartir_cartas()
    mano_jugador1 = cartas[0]
    mano_jugador2 = cartas[1]
    cartaJugada = 0
    print("mano ",turno)
    print("Jugador 1 tiene: ",mano_jugador1)
    #Pregunta si quiere cantar truco o envido, en el principio de cada manos
    while(juego != 'truco' and juego != 'envido' and juego != 'no'):
        juego = input('Cantas truco o envido? (escribí "truco", "envido" o "no")')
        if(juego != 'truco' and juego != 'envido' and juego != 'no'):
            print('Lo que ingresaste no es valido, intenta de nuevo')
    # Pide al jugador que ingrese el numero de la posicion de la carta
    while(cartaJugada != 0 and cartaJugada != 1 and cartaJugada != 2):
        cartaJugada = int(input('ingresa cual es la posicion de la carta que queres jugar (1, 2 o 3): ')) - 1
        if(cartaJugada != 0 and cartaJugada != 1 and cartaJugada != 2):
            print('posicion no valida')
    # Jugar una ronda simple (primera carta de cada jugador)
    ganador = determinar_ganador(mano_jugador1[cartaJugada], mano_jugador2[0])
    print("Jugador 1 juega: ",mano_jugador1[cartaJugada])
    print("Jugador 2 juega: ",mano_jugador2[0])
    
    #Se sacan de la mano las cartas jugadas
    mano_jugador1.remove(mano_jugador1[cartaJugada])
    mano_jugador2.remove(mano_jugador2[0])
    # print(f"El ganador de la ronda es: {ganador}")

# Ejecutar el juego
jugar_truco()