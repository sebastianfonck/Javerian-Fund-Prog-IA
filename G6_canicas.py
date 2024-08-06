# ----------------------------------------------------------------------------------------
# PROGRAMA: G6_canicas.py
# ----------------------------------------------------------------------------------------
# Descripción: 
#   Teniendo en cuenta esto, construya un algoritmo que permita clasificar un conjunto de N canicas cuyos
#   diámetros son dados uno a uno por el usuario. El programa debe mostrar la clasificación de cada canica.
#   De igual manera, el programa debe informar, antes de terminar, la cantidad de canicas de cada clase. Para
#   el ejemplo, de las N=6 canicas de la tabla, el programa debería imprimir los siguientes resultados:
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [05.08.2024]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES 
#----------------------------------------------------------------------------------------
# buenas                = Contador de canicas buenas
# malas                 = Contador de canicas mas
# potencialmente_buenas = Contador de canicas potencialmente_buenas
#----------------------------------------------------------------------------------------
# PRECONDICIONES
# ----------------------------------------------------------------------------------------
# 1. Tiene que ingresar un numero entre 3 y 10.
# 2. El numero tiene que ser entero.
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# 1. Clasificar la canica por su diametro.
# 2. Indicar la cantidad de canicas en sus diferentes calidades: Bueno, potencial mente bueno y Malo.
# 
# ----------------------------------------------------------------------------------------
def clasificar_canicas():
    # Solicitar la cantidad de canicas
    while True:
        N = int(input("Ingrese la cantidad de canicas (entre 3 y 10): "))
        if 3 <= N <= 10:
            break
        else:
            print("Por favor, ingrese un número entre 3 y 10.")

    # Inicializar contadores
    buenas = 0
    malas = 0
    potencialmente_buenas = 0

    # Clasificar cada canica
    for i in range(1, N + 1):
        diametro = int(input(f"Ingrese el diámetro de la canica {i}: "))
        if diametro % 2 == 0 and diametro % 3 == 0 and diametro % 5 == 0:
            print(f"Canica {i}: Buena")
            buenas += 1
        elif diametro % 2 == 0 or diametro % 3 == 0 or diametro % 5 == 0:
            print(f"Canica {i}: Potencialmente buena")
            potencialmente_buenas += 1
        else:
            print(f"Canica {i}: Mala")
            malas += 1

    # Mostrar el total de canicas de cada clase
    print("Total:")
    print(f"{buenas} buenas,")
    print(f"{malas} malas y")
    print(f"{potencialmente_buenas} potencialmente buenas.")

# Ejecutar la función
clasificar_canicas()

# ----------------------------------------------------------------------------------------
# Fin.
# ----------------------------------------------------------------------------------------