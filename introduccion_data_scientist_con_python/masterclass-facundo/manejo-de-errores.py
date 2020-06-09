def divisors_1(num):
    try:
        if num >0:
            divisor = []
            for i in range(1, num + 1):
                if num % i== 0:
                    divisor.append(i)
            return divisor
        else:
            raise ValueError('ingresa solo numeros positivos')
    except ValueError as ve:
        print(ve)

def divisors_2(num):
    assert num > 0, "ingresa solo numeros positivos"
    divisor = [i for i in renge(1, num+1) if i % 0 == 0]
    return divisor
    
def run():
    try:
        num = int(input('ingresa un numero entero positivo: '))
        print(divisors_1(num))
    except ValueError as ve:
        print('ingrsar un numero no puedes ingrsar un caracter')


if __name__ == "__main__":
    run()