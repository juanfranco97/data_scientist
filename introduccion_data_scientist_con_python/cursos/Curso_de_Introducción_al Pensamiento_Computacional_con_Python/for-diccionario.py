estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4,
}

for pais in estudiantes:
    print(pais)
for pais in estudiantes.keys():
    print(pais)   
for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)
for pais, numero_de_estudiantes in estudiantes.items():
    print(pais, numero_de_estudiantes)