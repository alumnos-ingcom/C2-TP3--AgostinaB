################
# Agostina Biagini - @AgostinaB
# Ejercicio N°1: Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    pass
    """Esta es la Excepcion para el ingreso incorrecto"""
    
    
def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta funcion muestra un mensaje y agrega # para indicar el ingreso
    de un número entero. Permite reintentar el ingreso 5 veces.
    """
    ingreso = input(mensaje + " #")    
    try:
        numero = int(ingreso)
        print(f'Cantidad de reintentos: {cantidad_reintentos}')
    except ValueError as err:
        cantidad_reintentos = cantidad_reintentos -1        
        if cantidad_reintentos == 0:
            raise IngresoIncorrecto("Valor inválido. Cantidad de reintentos:0") from err
        else:
            print(f'Cantidad de reintentos: {cantidad_reintentos}. Ingrese un número entero')
            numero = ingreso_entero_reintento(mensaje, cantidad_reintentos)
    return numero


def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    """
    Esta funcion muestra un mensaje y agrega # para indicar el ingreso
    de un número entero. Establece un rango de valores válidos entre
    mínimo y máximo.
    """
    print(f'El rango de valores válidos es: {valor_minimo} - {valor_maximo}')
    ingreso = input(mensaje + " #")    
    try:
        numero = int(ingreso)      
    except ValueError as err:              
        if numero < valor_minimo:
            raise IngresoIncorrecto("Valor inválido. Es inferior al valor mínimo") from err
        elif numero > valor_maximo:
            raise IngresoIncorrecto("Valor inválido. Es superior al valor máximo") from err
        else:            
            print(f'El número ingresado es válido')
        return numero
  
  
def prueba():
    mensaje = "Ingrese un número entero"
    ingreso = ingreso_entero(mensaje)
    ingreso = ingreso_entero_reintento(mensaje)
    ingreso = ingreso_entero_restringido(mensaje)


if __name__ == "__main__":
    prueba()
 
    
