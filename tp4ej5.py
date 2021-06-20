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
        resultado = -1
    elif numero == 0:
        resultado = 0
    else:
        resultado = 1
    
    return resultado
                    
    
def prueba():
    print('Ejercicio 5: Números positivos y negativos \n')
    numero = int (input("Ingrese un número entero: "))
    resultado = signo(numero)    
    print(f'\n El número ingresado es: {resultado} ')

    
if __name__ == "__main__":
    prueba()  