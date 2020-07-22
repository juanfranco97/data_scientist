#we have two arrays and we have to combinate this arrays in only one 
# the new array must be use the same that first array A+B=A
#A=n elements B=m elements

import random

def combination (A,B):
    A_size=len(A)
    B_size=len(B)

    for i in range(B_size):
        A[i] = B[i]
    return A
#O(n) time
#O(1) memory space


if __name__ == '__main__':
    size_of_the_first_array = int(input('introduce el tamaño de la lista uno : '))
    fisrt_array= sorted([random.randint(0,100) for i in range(size_of_the_first_array)]) 
    size_of_the_second_array = int(input('introduce el tamaño de la lista dos : '))
    second_array= sorted(
        [random.randint(0,100) for i in range(size_of_the_second_array)]
        + 
        [0 for i in range( size_of_the_first_array)]
        ) 
    print(fisrt_array)
    print(second_array)
    
    new_A_array=sorted(combination(second_array, fisrt_array))
    print(f'la lista combinada es: {new_A_array}')
