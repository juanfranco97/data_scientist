#una fraccion tiene que estar representada por la suma de fraciones donde el numerador sea 1 
# tentativamente por el ejemplo el denominador tiene que ser un numero par

print('este algoritmo permite expresar una fraccion en forma egipcia')
numerador = abs(int(input('introduce el numerador de tu fraccion ')))
denominador = abs(int(input('introduce el denomindaro de tu fraccion ')))

while numerador != 1
  if (numerador%2) == 0 and (denominador%2) == 0:
       denominador = denominador/2
       numerador = numerador/2
  elif (numerador%2) == 0 and (denominador%2) != 0:
      
  else:
  numerador = numerador-1
  print(f' 1 / {denominador}')

#denomindaor no divisible entre dos naturalmente y ambos no divisibles
while n != 9 :
    if (numerador%n) ==0 and (denominador%n) == 0:
        numerador = (numerador/n)
        denominador = (denominador/n)
    else:
        n += 1
n=2
print(f'{numerador} / {denominador}')