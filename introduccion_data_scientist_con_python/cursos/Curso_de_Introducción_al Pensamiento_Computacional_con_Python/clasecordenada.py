from aproximacion import root


classCoordenada:

    def__init__(self,x,y):
        self.x = x
        self.y = y
    
    defdistancia(self,otra_coordenada):
        #print(f'Coord_1 = {self.x},{ self.y}')
        #print(f'Coord_2 = {otra_coordenada.x},{otra_coordenada.y}')
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
               
        return root(x_diff + y_diff)
        
       

if __name__ == '__main__':
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)
     
    
    print(coord_1.distancia(coord_2))
    print('Es coord_2 instancia de coordenada?', isinstance(coord_1,Coordenada))