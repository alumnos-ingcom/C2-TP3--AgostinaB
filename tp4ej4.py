################
# Agostina Biagini - @AgostinaB
# Ejercicio N°4: Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara (numero_1,numero_2):
    """Esta función recibe dos números,los compara y retorna un resultado.
    Retorna -1 si el primer número es menor que el segundo.
    Retorna 0 si son números iguales.
    Retorna 1 si el primero es mayor que el segundo.
    """
    
    if numero_1 < numero_2:
        resultado = -1
        return resultado
    elif numero_1 == numero_2:
        resultado = 0
        return resultado
    elif numero_1 > numero_2:
        resultado = 1
        return resultado
                    
   
def prueba():
    pass
    print('Ejercicio 4: Comparación de números \n')
    num1 = int (input("Ingrese el primer número entero: "))
    num2 = int(input("\n Ingrese el segundo número entero: "))
    resultado = compara(num1,num2)
    print(f'El resultado de comparar los números {num1} y {num2} es: {resultado}')


    
if __name__ == "__main__":
    prueba()  