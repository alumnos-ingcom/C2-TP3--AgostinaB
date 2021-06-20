################
# Agostina Biagini - @AgostinaB
# Ejercicio N°9: Números Primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    """Esta función recibe un número entero e indica True si es primo,
       False si no es primo.
    """
    contador=0    
    if numero >= 1 :
        for i in range(1,numero+1) :
            if (numero%i)==0 :
                contador= contador+1        
        if contador ==2 :
            return True
        else:
            return False
    else:
        raise ValueError ("No es un número válido") 

def prueba():
    print('Ejercicio 9: Números primos \n')
    numero = int (input("Ingrese un número: "))
    resultado= es_primo(numero)
    print(f'El resultado es: {resultado}')
        
    
if __name__ == "__main__":
    prueba() 