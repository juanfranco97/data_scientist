import random


def remuve_duplicate1(random_list):
    return list(set(random_list))


if __name__ == '__main__':
    random_list = [1,2,3,4,5,23,34,2,"hola","hola",True, False, False]
    print(remuve_duplicate1(random_list))
#no se imprime True por que es un fallo en python 
