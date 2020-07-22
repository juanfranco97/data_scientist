import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x,y):
    #n = np.size(x)
    #obteniendo los promedios de x y
    m_x, m_y = np.mean(x), np.mean(y)
    #calcular las sumas
    sumatoria_xy= np.sum((x-m_x)*(y-m_y))
    sumatoria_xx= np.sum(x*(x-m_x))
    
    #coeficientes de regrecion
    b_1= sumatoria_xy/sumatoria_xx
    b_0= m_y-b_1*m_x
    
    return(b_0, b_1)
    
#funcion de graficado
def plot_regression(x, y, b):
    plt.scatter(x, y, color = "g", marker= "o", s=30)
        
    y_predictions = b[0] + b[1]*x
    plt.plot(x,y_predictions, color ="b")
        
    #etiquetado
    plt.xlabel('x,independiente')
    plt.ylabel('y-dependiente')
    plt.show()
    
def run():
    #data_set
    x = np.array([1,2,3,4,5])
    y= np.array([2,3,5,6,5])
    
    #obtenemos b1 y b2
    b= estimate_b0_b1(x, y)
    print(f'los valores de b0 = {b[0]} , b1= {b[1]}')
    
    #graficamos nuestra linea de regrecion
    plot_regression(x, y, b)

if __name__ == '__name__' :
    run()
