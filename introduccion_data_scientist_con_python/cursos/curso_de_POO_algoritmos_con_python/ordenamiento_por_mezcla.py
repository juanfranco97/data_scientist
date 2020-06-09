import random

# Log lineal or O(n log n)
def merge_sort_list(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_side = list[:mid]
        right_side = list[mid:]

        merge_sort_list(left_side)
        merge_sort_list(right_side)

        # iterators
        i = 0
        j = 0
        k = 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                list[k] = left_side[i]
                i += 1
            else: 
                list[k] = right_side[j]
                j += 1
            
            k += 1
        
        while i < len(left_side):
            list[k] = left_side[i]
            i += 1
            k += 1
        
        whilej < len(right_side):
            list[k] = right_side[j]
            j += 1
            k += 1

    return list
    

    
        
if __name__ == '__main__':
    tamano_de_la_lista = int(input('introduce el tamaño de la lista: '))
    lista= [random.randint(0,100) for i in range(tamano_de_la_lista)]
    print(lista)
    print('_'*20)
    lista_ordenada = merge_sort_list(list)
    print(lista_ordenada)