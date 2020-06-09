"""Importamos la libreria de unittest."""
import unittest

def suma (num_1, num_2):
    return (num_1+num_2)

"""Creamos una clase para los test, en este caso se llamara
CajaNegraTest, y como parámetro."""
class CajaNegraTest(unittest.TestCase):

    """Definimos la funcion que generara el test."""
    def test_suma_dos_positivos(self):

        "Para nuestro ejemplo usaremos 2 parametros."""
        num_1 = 10
        num_2 = 5

        """Y dentro de la variable resultado
        guardaremos lo que nos retornara la función suma."""
        resultado = suma(num_1, num_2)

        """Y para terminar definimos la variable resultado
        y cual es el valor esperado."""
        self.assertEqual(resultado, 15)


"""Para definir el módulo de Python escribimos lo siguiente."""
if __name__ == '__main__':
    unittest.main()