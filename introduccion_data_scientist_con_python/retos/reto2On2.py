import random
# lista[n]+lista[m]=k =true
# basado ordanamiento por busrbuja y con On^2
def algoritmo (lista, numerok): #[1,2,4] y [10,15,3,7]
    n=len(lista) #3
    for i in range(n):#3
        for j in range(n):#1-3
            if (lista[i] + lista[j]) == numerok and lista[i] != lista[j]:
               return True
    return False

if __name__ == '__main__':
    lista= [1,2,4] 
    numerok= 4
    print(algoritmo(lista, numerok))