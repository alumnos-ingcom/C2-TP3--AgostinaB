################
# Agostina Biagini - @AgostinaB
# Ejercicio N°1: Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass
 
 
    
def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    
    try:
        entero = int(ingreso)
        
    except ValueError as err:
        entero = ingreso_entero_reintento(mensaje)
   
    return entero



def ingreso_entero_reintento(mensaje, cantidad_reintentos=4):
    """
    Esta funcion muestra un mensaje y agrega # para indicar el ingreso
    de un número entero. Permite reintentar el ingreso 5 veces.
    """
    ingreso = input(mensaje +",  te quedan: " +
                    str(cantidad_reintentos) + " reintentos #")    
    
    try:
        numero = int(ingreso)
        
    except ValueError as err:
        if cantidad_reintentos == 0: 
            raise IngresoIncorrecto("No es un número!") from err
        else:
            cantidad_reintentos = cantidad_reintentos - 1
            numero = ingreso_entero_reintento(mensaje, cantidad_reintentos)
    return numero
         
                  
         
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    """
    Esta funcion muestra un mensaje y agrega # para indicar el ingreso
    de un número entero. Establece un rango de valores válidos entre
    mínimo y máximo.
    """
    print(f'El rango de valores válidos es: {valor_minimo} - {valor_maximo}')
    numero = int(input(mensaje + " #"))
    
    if numero < valor_minimo:
        raise IngresoIncorrecto("Valor inválido. Es inferior al valor mínimo") 
    elif numero > valor_maximo:
        raise IngresoIncorrecto("Valor inválido. Es superior al valor máximo")
    else:            
        print(f'El número ingresado es válido')
    
    return numero
        
  
  
def prueba():
    
    mensaje = "Ingrese un número entero"
    ingreso = ingreso_entero(mensaje)
    print(f'El número ingresado es: {ingreso}')
    mensaje = "Ingrese un número entero entre 0 y 10"
    ingreso = ingreso_entero_restringido(mensaje)
    print(f'El número ingresado es: {ingreso}')    
   


if __name__ == "__main__":
    prueba()
 
    
