import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice] #lista[1] =71 
        posicion_actual = indice  #1

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual: #90 > 71
            lista[posicion_actual] = lista[posicion_actual - 1] # 71 =90
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista
    

if __name__ == '__main__':
    tamano_de_la_lista = int(input('introduce el tamaño de la lista: '))
    lista= [random.randint(0,100) for i in range(tamano_de_la_lista)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)