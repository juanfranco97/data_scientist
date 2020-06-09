numero=abs(int(input('introducce un numero ')))
respuesta = 0.0
exactitud = 0.01
paso = exactitud**2


while abs(numero - respuesta**2 ) >= exactitud:
  respuesta += paso

print(f'la respuesta es {round(respuesta,2)}')