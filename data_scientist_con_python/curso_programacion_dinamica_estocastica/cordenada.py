#Clase para modificar las coordenadas de un borracho
class Coordenada:
    #Inicializa las coordenadas de partida o en las que se encuentra
    #un borracho
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Esta función suma una distancia nueva delta a las coordenadas  
    #iniciales x e y que se definieron en el constructor
    def mover(self, delta_x, delta_y):
        #Retorna la coordenada actualizada. (Usa el constructor para ello)
        return Coordenada(self.x +  delta_x, self.y + delta_y)
    #Mide la distancia entre la posicion actual y la distancia objetivo
    #Donde queremos llegar o a donde vamos
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x 
        delta_y = self.y - otra_coordenada.y
        #Retornamos la medida de la distancia entre donde estoy y a donde 
        #quiero ir. Usando pitagoras
        return (delta_x**2 + delta_y**2)**0.5