# ----------------------------------------------------------------------------------------
# PROGRAMA: <<nombre del programa>>
# ----------------------------------------------------------------------------------------
# Descripción: <<breve descripción>>
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [30.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import random

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# arr_pool : Arreglo que simula el la psina
# El perimetro de la psina tiene que se 0
# la profundidad de la psina tiene que se entre 5 y 30
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# Se tiene que poder visaulizar el recorrido de la esfera
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros
def createPool():
    print("#########CREAR LA PSINA #############")
    # Pedir al usuario que ingrese el ancho y largo de la matriz
    ancho = int(input("Ingrese el ancho de la piscina: "))
    largo = int(input("Ingrese el largo de la piscina: "))
    
    # Imprimir los valores ingresados
    print(f"Ancho ingresado: {ancho}")
    print(f"Largo ingresado: {largo}")

    # Crear una matriz de ceros con las dimensiones especificadas
    matriz = [[0 for _ in range(ancho)] for _ in range(largo)]

    # Imprimir la matriz
    for fila in matriz:
        print(fila)
    
    return matriz

def fillPool(pool):
    print("########LLENAR LA PSINA#############")

    # Llenar la matriz con el número aleatorio
    for i in range(len(pool)- 1):
        for j in range(len(pool[i])- 1):
            # Generar un número aleatorio entre 5 y 30 en incrementos de 4
            numero_aleatorio = random.randrange(5, 31, 4)
            if i != 0 and j != 0 and i != -1:       
                pool[i][j] = numero_aleatorio
        
    # Imprimir la matriz llena
    for fila in pool:
        print(fila)

    return pool

    

arr_pool = createPool()
arr_pool = fillPool(arr_pool)



# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------