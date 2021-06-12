################
# Agostina Biagini - @AgostinaB
# Ejercicio N°5: Números Positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo (numero):
    """Esta función recibe un número entero y retorna si éste es
    positivo, negativo o cero.
    """
    
    if numero < 0:
        resultado = ('negativo')
        return resultado
    elif numero == 0:
        resultado = ('cero')
        return resultado
    else :
        resultado = ('positivo')
        return resultado
                    
    
def prueba():
    print('Ejercicio 5: Números positivos y negativos \n')
    numero = int (input("Ingrese un número entero: "))
    resultado = signo(numero)    
    print(f'\n El número ingresado es: {resultado} ')

    
if __name__ == "__main__":
    prueba()  