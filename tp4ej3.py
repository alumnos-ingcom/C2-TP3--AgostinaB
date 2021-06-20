################
# Agostina Biagini - @AgostinaB
# Ejercicio N°3: Conversión de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrenheit(centigrados):
    """Esta función transforma temperatura en grados centigrados a grado
    fahrenheit.
    """
    
    conversion=((centigrados*(9/5))+32)
    return conversion
        
def convertir_a_centigrados(fahrenheit):
    """Esta función transforma temperatura en grados fahrenheit a grado
    centigrados.
    """
    
    conversion=((fahrenheit +(-32))/(9/5))
    return conversion
          
def prueba():
    print('Ejercicio 3: Conversión de temperaturas \n')
    centigrados = float (input("Ingrese grados centígrados: "))
    resultado = convertir_a_fahrenheit(centigrados)
    print(f'\n La temperatura en grados fahrenheit es: {resultado}')
    fahrenheit = float(input("\n Ingrese grados fahrenheit: "))
    resultado_dos = convertir_a_centigrados(fahrenheit)
    print(f'\n La temperatura en grados centígrados es: {resultado_dos}')
    
    
if __name__ == "__main__":
    prueba()    



