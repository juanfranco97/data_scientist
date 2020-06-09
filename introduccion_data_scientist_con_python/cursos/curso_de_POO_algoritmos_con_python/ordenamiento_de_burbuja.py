import random

def ordenamiento_de_burbuja (lista):
    n= len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista [j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

    
        
if __name__ == '__main__':
    tamano_de_la_lista = int(input('introduce el tamaño de la lista: '))
    lista= [random.randint(0,100) for i in range(tamano_de_la_lista)]
    print(lista)
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
   
 # while True:
   #     for elemento in lista:
   #         if lista[n] > lista[n+1]:
   #             lista[n], lista[n+1] = lista[n+1], lista[n]
   #             return True
   #         return False
   #     n +=1
   # return lista
# return indica el fin de la ejecucion de la funcion 
#por eso no funciona este algoritmo