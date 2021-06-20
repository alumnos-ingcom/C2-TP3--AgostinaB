################
# Agostina Biagini - @AgostinaB
# Ejercicio N°8: Ordenar tres valores
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ordenar_mayor_a_menor (num1,num2,num3):
    """Esta función recibe tres números enteros y los ordena de mayor a menor.
    """
    if num1 >= num2 :
        if num1 >= num3 :
            if num2 >= num3 :
                tupla= (num1,num2,num3)
            else :
                tupla= (num1,num3,num2)
        else :
            tupla= (num3,num1,num2)
    elif num2 >= num3 :
        if num1 >= num3 :
            tupla= (num2,num1,num3)
        else :
            tupla= (num2,num3,num1)
    else :
        tupla= (num3,num2,num1)
        
    print(f'La tupla ordenada de mayor a menor es: {tupla} ')
    
            
def ordenar_menor_a_mayor (num1,num2,num3):
    pass
    """Esta función recibe tres números enteros y los ordena de menor a mayor.
    """
    
    if num1<= num2 :
        if num1 <= num3 :
            if num2 <= num3 :
                tupla= (num1,num2,num3)
            else :
                tupla= (num1,num3,num2)
        else :
            tupla= (num3,num1,num2)
    elif num2 <= num3 :
        if num1 <= num3 :
            tupla= (num2,num1,num3)
        else :
            tupla= (num2,num3,num1)
    else :
        tupla= (num3,num2,num1)
        
    print(f'La tupla ordenada de menor a mayor es: {tupla} ')
                

def prueba():
    print('Ejercicio 8: Ordenar tres valores \n')
    num1 = int (input("Ingrese número uno: "))
    num2 = int (input("Ingrese número dos: "))
    num3= int (input("Ingrese número tres: "))
    ordenar_menor_a_mayor (num1,num2,num3)  
    ordenar_mayor_a_menor (num1,num2,num3)
    
    
if __name__ == "__main__":
    prueba() 