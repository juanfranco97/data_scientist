numero=abs(int(input('introducce un numero ')))
exactitud=0.01
bajo=0.0
alto=max(1.0, numero) #max regresa el valor mas alto entre un conjunto de numeros*
respuesta= (alto+bajo)/2

while abs(respuesta**2 - numero) >= exactitud:
    if respuesta**2 < numero:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo)/ 2

print(f'la raiz es {respuesta}')        