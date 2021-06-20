################
# Agostina Biagini - @AgostinaB
# Ejercicio N°10: Factores Primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej9 import es_primo

def factores_primos(numero):
    """Esta función recibe un número entero y construye una tupla con
       sus factores primos (divisores primos).
    """
    divisores =[]
    primos=[]
    for i in range(1, numero+1):
        if (numero % i)==0 :
            if es_primo(i) == True:
                divisores.append(i)    
    return tuple(divisores)

def prueba():
    print('Ejercicio 10: Factores primos \n')
    numero = int (input("Ingrese un número entero: "))
    tupla = factores_primos(numero)    
    print(f'La tupla de factores primos de {numero} es: {tupla}')

if __name__ == "__main__":
    prueba() 