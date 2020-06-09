import random

def busqueda_lineal (lista, objetivo) :
    match=False

    for objeto in lista :
        if objeto == objetivo :
            match = True
            #break
    return match
 
if __name__ == '__main__':
    tamano_de_la_lista = int(input('introduce el tamaño de la lista: '))
    objetivo = int(input('introduce el objetivo: '))
    lista= [random.randint(0,100) for i in range(tamano_de_la_lista)]
    encontrado = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') # operador tersiario

     
