"""Given a list of integers arr, modify it such that every 0 appears twice while maintaining the original list size. Modify the list in place."""

def zero_transformation (array):
    lenth = len(array)
    aux_array=[]
    aux_lenth = 0
    for num in array:
        if aux_lenth == lenth:
            break
        aux_array.append(num)
        if num == 0:
            aux_array.append(0)
        aux_lenth = len(aux_array)
    return aux_array

def zero_in_place (array):
    i=0
    for element in array :
        if element == 0:
            array[i+2] = array[i+1]
            array[i+1] = 0
        i +=1
    return array

            





if __name__ == "__main__":
    test_array = [1,0,2,3,0,4,5,0]
    #test_array = [0,0]
    #new_array = zero_transformation(test_array)
    new_array = zero_in_place(test_array)
    print(new_array)

    #como hacer multimples test