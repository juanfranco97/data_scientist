#un candidato tiene que tener almenos la mitad de los botos totales
import random

def winner(votos) :
    uno=votos.count(1)
    dos=votos.count(2)
    tres=votos.count(3)
    if uno>dos and uno>tres:
        print('el ganador de la eleccion es uno')
    elif dos>uno and dos > tres:
        print('el ganador de la eleccion es dos ')
    else:
        print('elganador de la eleccion es tres')

#O(1)
#O(1)

if __name__ == '__main__':
    votos_size = int(input('introduce el numero de votos : '))
    el ganador = random.randint(1,3) 
    votos= sorted([random.randint(1,3) for i in range(votos_size)]) 
    votos =

    winner(votos)
    