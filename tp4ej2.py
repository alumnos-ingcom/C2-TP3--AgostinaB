################
# Agostina Biagini - @AgostinaB
# Ejercicio N°2: Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero,otro_numero):
    """Esta función realiza la suma lenta de dos numeros enteros.
    """
    if otro_numero > 0:
        for i in range(otro_numero):
            numero = numero + 1

    elif otro_numero < 0:
        otro_numero = otro_numero * (-1)
        for j in range(otro_numero):
            numero = numero - 1
    
    return numero        
    
def prueba():
    print('Ejercicio 2: Suma de dos números enteros \n')
    num1 = int(input("Ingrese un número entero: "))
    num2= int(input("\n Ingrese otro número entero: "))
    resultado = suma_lenta(num1,num2)
    print(f'\n El resultado de sumar lento {num1} y {num2} es {resultado}')
    

if __name__ == "__main__":
    prueba()    





     
