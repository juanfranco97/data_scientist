numero=abs(int(input('introducce un numero ')))
respuesta=0
while respuesta**2 < numero:
    respuesta +=1
if respuesta**2 == numero:
    print(f'la raiz cuadrada es {respuesta}')
else:
    print(f'{numero} no tiene raiz entera')