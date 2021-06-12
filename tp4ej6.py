################
# Agostina Biagini - @AgostinaB
# Ejercicio N°6: Máximo / Mínimo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def maximo (lista):
    """La función máximo recibe una lista de enteros y muestra el mayor valor.
    """ 
    mayor=lista[0]   
    for i in lista:
       if i > mayor:
           mayor = i
    return mayor
    
def minimo (lista_dos):
    """La función mínimo recibe una lista de enteros y muestra el menor valor.
    """ 
    menor=lista_dos[0]   
    for i in lista_dos:
       if i < menor:
           menor = i
    return menor
    

def prueba():
    print('Ejercicio 6: Máximo / Mínimo \n')
    lista = [1,2,3,4,5,10,50,100]
    print(f' La lista de trabajo es: {lista}')
    menor = minimo (lista)
    mayor = maximo (lista)
    print (f'El número menor es: {menor}')
    print (f'El número mayor es: {mayor}')

    
if __name__ == "__main__":
    prueba() 