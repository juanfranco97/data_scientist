#Given an array A of numbers, we define a sigma transformation of the i-th element as sigma_trans(i) = sum(A[0], ..., A[i]).
#Compute the sigma transformations of all the elements of the array.
#The length of the array n is 0 <= n <= 10^9.
#All values v of A are 0 <= v <= 10^6.

import random

def sigma_transformatio(array):
    for i in range (len(array)-1):
        array[i+1] += array[i]
    return array
#O(n+n1)= O(n) time
#O(1)    memory space

if __name__ == '__main__':
    array_size = int(input('introduce el tamaño de la lista : '))
    array= sorted([random.randint(0,1000000) for i in range(array_size)]) 
    print(array)
    new_array = sigma_transformatio(array)
    print(f'el array con transformacion sigma es : {new_array} ')