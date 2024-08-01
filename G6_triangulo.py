# ----------------------------------------------------------------------------------------
# PROGRAMA: G6_triangulo.py
# ----------------------------------------------------------------------------------------
# Descripción: 
# Este programa lee tres números correspondientes a los lados de un triángulo e indica 
# que tipo de triangulo forman (isósceles, equilátero, escaleno). 
# Adicionalmente, comprueba que los números ingresados conformen un triángulo, 
# en caso contrario emite un mensaje con esta novedad. 
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [31.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES 
#-----------------------------------------------------------------------------------------
#Lado1: Almacena el dato ingresado por el usuario referente al lado 1 del triangulo.
#Lado2: Almacena el dato ingresado por el usuario referente al lado 2 del triangulo. 
#Lado3: Almacena el dato ingresado por el usuario referente al lado 3 del triangulo. 
#tipo_triangulo: Almacena el tipo de triangulo resultante según la validación de los lados
#ingresados por el usuario
#----------------------------------------------------------------------------------------
# PRECONDICIONES
# ----------------------------------------------------------------------------------------
#1. El usuario debe ingresar solo numeros
#2. Los números ingresados deben ser mayores a cero
#------------------------------------------------------------------------------------------
# POSTCONDICIONES
#------------------------------------------------------------------------------------------
# 1. El programa debe determinar El tipo de triangulo formado
# 2. El programa debe mostrar un mensaje en caso que no se pueda conformar un triangulo 
# con los valores ingresasados
#3. En caso de que el usuario ingrese un valor no permitido, elsistema mostrará un mensaje 
#con la excepción generada
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

# <<Escriba desde aqui el código del programa...>>
def es_triangulo_valido(lado1, lado2, lado3):
    # Comprobamos si los lados forman un triángulo válido
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1

def clasificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

try:
    # Leer los lados del triángulo
    lado1 = float(input("Ingrese el primer lado del triángulo: "))
    lado2 = float(input("Ingrese el segundo lado del triángulo: "))
    lado3 = float(input("Ingrese el tercer lado del triángulo: "))

    if es_triangulo_valido(lado1, lado2, lado3):
        tipo_triangulo = clasificar_triangulo(lado1, lado2, lado3)
        print(f"\nEl triángulo es {tipo_triangulo}")
    else:
        
        print("Los números ingresados no forman un triángulo válido.")

except ValueError:
    print("\nPor favor, ingrese valores numéricos válidos.")

# ----------------------------------------------------------------------------------------
# Fin.
# ----------------------------------------------------------------------------------------