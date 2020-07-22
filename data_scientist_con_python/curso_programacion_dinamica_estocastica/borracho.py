#Clase para inicializar un borracho
import random
class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre
#Es la extensión que hace que un borracho se desplace entr cuatro coordenadas
class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def camina(self):
        #random.choice() escoge aleatoriamente entre una estructura 
        #iterable en este caso un arreglo con cuatro coordenadas
        return random.choice([(1,0),(0,1),(-1,0),(0,-1)])