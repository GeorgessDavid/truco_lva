import random

# Definimos los palos y los valores de las cartas
# palos = ['Espadas', 'Bastos', 'Oros', 'Copas']
# valores = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']

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

# Función para definir la jerarquía de las cartas.
def obtener_jerarquia(carta):
    for i in range(len(JERARQUIA)):
        for j in range(len(JERARQUIA[i])):
            if JERARQUIA[i][j] == carta:
                return i
# Función para barajar y repartir las cartas
def repartir_cartas(mazo):
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
    for i in range(6): #Rango 6 porque el juego está programado para que se juegue entre dos usuarios, por lo que las cartas repartidas siempre son 6.
        mazo.remove(mazo[i])
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
        ganadorUltimaRonda = 'Jugador 1'
        return ganadorUltimaRonda
    elif valor_carta2 < valor_carta1:
        ganadorUltimaRonda = 'Jugador 2'
        return ganadorUltimaRonda
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

def calcular_puntos(juego, seQuiere, puntosjugador1, puntosjugador2, jugadorQueSuma):
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
    else:
        puntos = 1
    
    if(jugadorQueSuma == 'Jugador 1'):
        puntosjugador1 = puntosjugador1 + puntos
    else:
        puntosjugador2 = puntosjugador2 + puntos
    
    return [puntosjugador1, puntosjugador2]

def maquinaDecideSiCantar(turno, juegoActual, confirmacion):
    if(confirmacion == False):
        if(juegoActual == '' or juegoActual == 'no' and turno == 1):
            posiblesJuegos = ['truco', 'envido', 'real envido', 'falta envido', 'no']
            numeroRandom = random.randint(0,4)
            juegoActual = posiblesJuegos[numeroRandom]
        elif(juegoActual == '' or juegoActual == 'no' and turno > 1):
            posiblesJuegos = ['truco', 'no']
            numeroRandom = random.randint(0,1)
            juegoActual = posiblesJuegos[numeroRandom]
        elif(juegoActual == 'truco'):
            posiblesJuegos = ['retruco', 'no']
            numeroRandom = random.randint(0,1)
            juegoActual = posiblesJuegos[numeroRandom]
        elif(juegoActual == 'retruco'):
            posiblesJuegos = ['vale cuatro', 'no']
            numeroRandom = random.randint(0,1)
            juegoActual = posiblesJuegos[numeroRandom]
    else:
        posiblesJuegos = ['si', 'no']
        numeroRandom = random.randint(0,1)
        juegoActual = posiblesJuegos[numeroRandom]
    
    return juegoActual

def crear_mazo():
    palos = ['Espadas', 'Bastos', 'Oros', 'Copas']
    valores = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
    mazo = []
    for palo in palos:
        for valor in valores:
            carta = valor + ' de ' + palo
            mazo.append(carta)
    return mazo

# Función principal del juego
def jugar_truco(puntosjugador1, puntosjugador2, mazo):
    if(len(mazo) <= 10):
        mazo = crear_mazo()
    cartas = repartir_cartas(mazo)
    mano_jugador1 = cartas[0]
    mano_jugador2 = cartas[1]
    juego = ''
    turno = 1
    ganadorUltimaRonda = 'Jugador 1' #Default Jugador 1
    rondasGanadasJugador1 = 0
    rondasGanadasJugador2 = 0
    cantoMaquina = False
    cantoJugador = False
    
    
    while(turno < 4 and rondasGanadasJugador1 < 2 and rondasGanadasJugador2 < 2):
        if(len(mazo) <= 10):
            mazo = crear_mazo()
        confirmacion = ''
        cartaJugada = int(99) #Le pongo 99 porque para cumplir la condicion tiene que ser 0, 1 o 2
        print("Mano",turno)
        print("Jugador 1 tiene:",mano_jugador1)
        print("Comienza jugando:", ganadorUltimaRonda)
        if(ganadorUltimaRonda == 'Jugador 2'):
            if(cantoMaquina == False):
                cantaMaq = maquinaDecideSiCantar(turno, juego, False)
                if(cantaMaq != 'no'):
                    juego = cantaMaq
                    print('Jugador 2 canta:', cantaMaq)
                    cantoMaquina = True
                    cantoJugador = False
                else:
                    print("Jugador 2 juega:",mano_jugador2[0])
        #Pregunta si quiere cantar truco o envido, en el principio de cada manos
        if(cantoMaquina == False):
            if(juego == '' or juego == 'no' and turno == 1):
                juego = ''
                while(juego != 'truco' and juego != 'envido' and juego != 'real envido' and juego != 'falta envido' and juego != 'no'):
                    juego = input('Cantas truco, envido, real envido o falta envido? (escribí "truco", "envido", "real envido", "falta envido" o "no"): ')
                    if(juego != 'truco' and juego != 'envido' and juego != 'real envido' and juego != 'falta envido' and juego != 'no'):
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(juego == 'truco' or juego == 'envido' or juego == 'real envido' or juego == 'falta envido'):
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
            elif(juego == '' or juego == 'no' and turno > 1):
                juego = ''
                while(juego != 'truco' and juego != 'no'):
                    juego = input('Cantas truco? (escribí "truco" o "no"): ')
                    if(juego != 'truco' and juego != 'no'):
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(juego == 'truco'):
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
            elif(juego == 'truco' and cantoJugador == False):
                confirmacion = ''
                while(confirmacion != 'si' and confirmacion != 'no'):
                    confirmacion = input('Queres cantar retruco? (por "si" o por "no"): ')
                    if(confirmacion != 'si' and confirmacion != 'no'):
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(confirmacion == 'si'):
                        juego = 'retruco'
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
            elif(juego == 'retruco' and cantoJugador == False):
                confirmacion = ''
                while(confirmacion != 'si' and confirmacion != 'no'):
                    confirmacion = input('Queres cantar vale cuatro? (por "si" o por "no"): ')
                    if(confirmacion != 'si' and confirmacion != 'no'):
                        print('Lo que ingresaste no es valido, intenta de nuevo')
                    elif(confirmacion == 'si'):
                        juego = 'vale cuatro'
                        confirmacion = maquinaDecideSiCantar(turno, juego, True)
                        if(confirmacion == 'no'):
                            print('Jugador 2 no quiso')
                            resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 1')
                            puntosjugador1 = resultado[0]
                            puntosjugador2 = resultado[1]
                            return [puntosjugador1, puntosjugador2]
                        else:
                            print('Jugador 2 quiso')
                            cantoJugador = True
                            cantoMaquina = False
        else:
            confirmacion = ''
            while(confirmacion != 'si' and confirmacion != 'no'):
                confirmacion = input('Aceptas lo que cantó Jugador 2? (por "si" o por "no"): ')
                if(confirmacion != 'si' and confirmacion != 'no'):
                    print('Lo que ingresaste no es valido, intenta de nuevo')
                elif(confirmacion == 'no'):
                    resultado = calcular_puntos(juego, False, puntosjugador1, puntosjugador2, 'Jugador 2')
                    puntosjugador1 = resultado[0]
                    puntosjugador2 = resultado[1]
                    return [puntosjugador1, puntosjugador2]
                elif(confirmacion == 'si'):
                    print('se juega', juego)
                    print("Jugador 2 juega:",mano_jugador2[0])
                    cantoMaquina = False
        # Pide al jugador que ingrese el numero de la posicion de la carta
        while(cartaJugada == '' or cartaJugada > len(mano_jugador1)-1 or cartaJugada <= -1):
            cartaJugada = int(input('ingresa cual es la posicion de la carta que queres jugar (tenes '+str(len(mano_jugador1))+' cartas): ')) - 1
            if(cartaJugada > len(mano_jugador1)-1 or cartaJugada <= -1):
                print('posicion no valida')
        
        ganador = determinar_ganador(mano_jugador1[cartaJugada], mano_jugador2[0])
        print("Jugador 1 juega:",mano_jugador1[cartaJugada])
        if(ganadorUltimaRonda == 'Jugador 1'):
            print("Jugador 2 juega:",mano_jugador2[0])
        
        #Se sacan de la mano las cartas jugadas
        mano_jugador1.remove(mano_jugador1[cartaJugada])
        mano_jugador2.remove(mano_jugador2[0])
        print("El ganador de la ronda es:",ganador)
        if(ganador == 'Jugador 1'):
            rondasGanadasJugador1 = rondasGanadasJugador1 + 1
        elif(ganador == 'Jugador 2'):
            rondasGanadasJugador2 = rondasGanadasJugador2 + 1
        print('rondas ganadas jugador 1:', rondasGanadasJugador1)
        print('rondas ganadas jugador 2:', rondasGanadasJugador2)
        turno = turno + 1
        if(ganador != 'Empate'):
            ganadorUltimaRonda = ganador

    if(rondasGanadasJugador1 > rondasGanadasJugador2):
        resultado = calcular_puntos(juego, True, puntosjugador1, puntosjugador2, 'Jugador 1')
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
    elif(rondasGanadasJugador1 < rondasGanadasJugador2):
        resultado = calcular_puntos(juego, True, puntosjugador1, puntosjugador2, 'Jugador 2')
        puntosjugador1 = resultado[0]
        puntosjugador2 = resultado[1]
    else:
        print('Empate, no se suman puntos')
        
    return [puntosjugador1, puntosjugador2]

# Ejecutar el juego
puntosJuego = 0
while(puntosJuego != 30 and puntosJuego != 15 and puntosJuego != 50):
    puntosJuego = int(input('Indica a cuantos puntos va a ser el truco ("15", "30" o "50"): '))
    if(puntosJuego != 30 and puntosJuego != 15 and puntosJuego != 50):
        print('No es valido lo que ingresaste, intenta de nuevo')

puntosjugador1 = 0
puntosjugador2 = 0
# Creamos el mazo de cartas
mazo = crear_mazo()
while(puntosjugador1 < puntosJuego and puntosjugador2 < puntosJuego):
    resultado = jugar_truco(puntosjugador1, puntosjugador2, mazo)
    puntosjugador1 = resultado[0]
    puntosjugador2 = resultado[1]
    print('Puntos de Jugador 1:', puntosjugador1)
    print('Puntos de Jugador 2:', puntosjugador2)

#si los dos pasan el puntaje a alcanzar, gana el que tenga mas puntos
if(puntosjugador1 >= puntosJuego and puntosjugador2 >= puntosJuego):
    if(puntosjugador1 > puntosjugador2):
        print('Ganador: Jugador 1')
    else:
        print('Ganador: Jugador 2')
elif(puntosjugador1 >= puntosJuego):
    print('Ganador: Jugador 1')
else:
    print('Ganador: Jugador 2') 