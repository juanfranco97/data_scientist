import random

def busqueda_bin (lista,comienzo,final, objetivo):
    print(f'buscar {objetivo} entre {comienzo} y {final-1}')
    if comienzo > final :
        return False

    medio= (comienzo+final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] > objetivo:
        return busqueda_bin(lista, comienzo, (medio-1), objetivo)
    else :
        return busqueda_bin(lista, (medio+1), final, objetivo)


if __name__ == '__main__':
    tamano_de_la_lista = int(input('introduce el tamaño de la lista: '))
    objetivo = int(input('introduce el objetivo: '))
    lista= sorted([random.randint(0,100) for i in range(tamano_de_la_lista)]) # ordenar la lista
    encontrado = busqueda_bin(lista,0,len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') # operador tersiario
