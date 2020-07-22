def insertion_sort_increased(array):
    
    for j in range(1,len(array)):
        key = array[j]
        i = j-1
        while i > -1 and array[i] > key :
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key
    return array

def insertion_sort_decreasing(array):
    
    for j in range(1,len(array)):
        key = array[j]
        i = j-1
        while i > -1 and array[i] < key :
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key
    return array

def linear_search(array, value):
    i = 0
    for val in array:
        if array[i] == value:
            return True
        i += 1
    return False

def binary_sum(num1,num2):
    num= num1+num2
    num="{0:b}".format(num)
    return num

def merge_sort()

if __name__ == '__main__':
    array2 = [31,41,59,26,41,58]
    array = [3,4,2,5,3,2,4,23,34,2,21,4,1,2,3,4,2,3,1,12,5,-1,-2,-23,-4,-43]
    #print(insertion_sort_increased(array))
    #print(insertion_sort_decreasing(array))
    #value = int(input('Enters a value to search in the array: '))
    #searh=linear_search(array2 , value)
    #if searh == True:
    #    print(f'congratulations {value} is in array')
    #else:
    #    print('Sorry, try with other value')
    #num1 = int(input('Enters first number: '))
    #num2 = int(input('Enters second number: '))
    #print(binary_sum(num1,num2))