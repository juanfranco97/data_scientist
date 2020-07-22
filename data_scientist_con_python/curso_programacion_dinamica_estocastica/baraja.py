""" juego del poker falta programacion defesiva """
import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']


def crear_baraja():
    """ Crea una baraja con todas las conbinaciones de palos y valores"""
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    """ Crea una mano con base al numero de barajas que por default es 1 
        y el tamaño que se quiera de la mano """
    mano = random.sample(barajas, tamano_mano) 
    #mano = random.random(barajas, tamano_mano) 
    return mano

def fun_escalera(i, valores):
    escaleras = 0
    j = 0
    print(valores[i])
    print(VALORES[j])
    #for _ in range(10):
    #    if valores[i] == VALORES[j]:
    #        escaleras += 1
    #        if escaleras >= tamano_mano :
    #            return 1
    #        if i == tamano_mano :
    #            return 0         
    #        fun_escalera(i+1, valores)
    #    else : j += 1

    


def main(tamano_mano, intentos,no_barajas):
    barajas = crear_baraja() * no_barajas
    #print(barajas)

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    dos_pares = 0
    tercias = 0
    escalera = 0
    color = 0
    full = 0
    poker = 0
    escalera_de_color = 0 
    escalera_real_de_color = 0


    for mano in manos:
        valores = []
        palos = []
        #print(dos_pares)
        for carta in mano:
            palos.append(carta[0])
            valores.append(carta[1])
  
        counter = dict(collections.Counter(valores))
        i=0
        for val in counter.values():
            if val == 2:
                i += 1
                if i == 1:
                    pares += 1
                else:
                    dos_pares += 1
            elif val == 3:
                tercias += 1  

        escalera = fun_escalera(0, valores)
            
        

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas y jugando {no_barajas} barajas es {probabilidad_par}')
    probabilidad_dos_par = dos_pares / intentos
    print(f'La probabilidad de obtener dos pares en una mano de {tamano_mano} cartas y jugando {no_barajas} barajas es {probabilidad_dos_par}')                
    probabilidad_tercia = tercias / intentos
    print(f'La probabilidad de obtener una tercia en una mano de {tamano_mano} cartas y jugando {no_barajas} barajas es {probabilidad_tercia}')
    #probabilidad_escalera = escalera / intentos
    #print(f'La probabilidad de obtener una escalera en una mano de {tamano_mano} cartas y jugando {no_barajas} barajas es {probabilidad_escalera}')
   


if __name__ == '__main__':
    no_barajas= int(input('Con cuantas barajas se va a jugar:'))
    tamano_mano = int(input('De cuantas cartas sera la mano sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos,no_barajas)