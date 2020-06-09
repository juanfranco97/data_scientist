
print('este algoritmo permite expresar una fraccion en forma egipcia')
numerador = abs(int(input('introduce el numerador de tu fraccion ')))
denominador = abs(int(input('introduce el denomindaro de tu fraccion ')))
n=2

while numerador != 0:
    if (numerador/denominador) >= (1/n):
        print(f'1 / {n}')
        numerador = (numerador*n)-(denominador)
        denominador = denominador * n
    else:
        n += 1
