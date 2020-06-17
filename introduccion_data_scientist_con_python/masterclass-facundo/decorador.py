from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs): #esta funcion es una nueva funcion conocida como envoltura que es la que resive  a la funcion a ser decorada y sus parametros
        initial_time = datetime.now()   #*args significa que extraiga todos los componentes de una tupla o lista
        func(*args, **kwargs)           #**kwargs significa que extraiga todos los componentes de un diccionario
        final_time = datetime.now()     #lo anterior se utiliza para que el decorador pueda funcionar sin parametros o con parametros ya sean explisitos(llave=clave) o no(locacional) 
        time_elapsed = final_time - initial_time
        print(f'pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper 


@execution_time
def random_func():
    for _ in range (1, 100000):
        print('.', end='')

@execution_time
def hola(nombre, apellido):
    print(f'hola {nombre} {apellido}')

def run():
    random_func():
    hola('jose', 'ramirez')


if __name__ =='__main__':
    run()