################
# Agostina Biagini - @AgostinaB
# Ejercicio N°2: Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero,otro_numero):
    """Esta función realiza la suma lenta de dos numeros enteros.
    """
    
    for i in range(otro_numero+1):
        suma = numero+i    
    return suma        
    
def prueba():
    print('Ejercicio 2: Suma de dos números enteros \n')
    num1 = int(input("Ingrese un número entero: "))
    num2= int(input("\n Ingrese otro número entero: "))
    resultado = suma_lenta(num1,num2)
    print(f'\n El resultado de sumar lento {num1} y {num2} es {resultado}')
    

if __name__ == "__main__":
    prueba()    





     
