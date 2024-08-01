# ----------------------------------------------------------------------------------------
# PROGRAMA: G6_mulRusa.py
# ----------------------------------------------------------------------------------------
# Descripción:
# Este programa multiplica dos número enteros mendiante al algoritmo de la multiplicación rusa.
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
# VARIABLES GLOBALES 
# ---------------------------------------------------------------------------------------
# A: Almacena el valor del multiplicador.
# B: Almacena el valor del multiplicando.
# pasos: Almacena los valores generados durante el proceso de multiplicación
# resultado: Almacena y acumula el resultado del proceso de la multiplicación
# ---------------------------------------------------------------------------------------
# PRECONDICIONES
# ----------------------------------------------------------------------------------------
# 1. El programa recibe dos numeros para realizar el procedimiento de la multiplicación rusa, 
# el multiplicador y el multiplicando .
# ---------------------------------------------------------------------------------------
# POSTCONDICIONES
# ---------------------------------------------------------------------------------------
# 1. El programa debe generar el resultado de la multiplicación mostrando en pantalla
# los números generados durante el proceso
# 2. El programa debe mostrar el resultado final de la multiplicación realizada a través del 
# método de multiplicación rusa.
# # ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

try:

    A = int(input("Ingrese el valor del multiplicando: "))
    B = int(input("Ingrese el valor del multiplicador: "))

    # <<Escriba desde aqui el código del programa...>>

    def Multiplicacion(multiplicando, multiplicador):
        resultado = 0
        pasos = []  # Para almacenar los valores generados en el proceso

        while multiplicador > 0:
            pasos.append((multiplicando, multiplicador))
            if multiplicador % 2 == 1:
                resultado += multiplicando
            multiplicando = multiplicando * 2
            multiplicador = multiplicador // 2

        return resultado, pasos

    resultado, pasos = Multiplicacion(A, B)

    print("Pasos del algoritmo:")

    for multiplicando, multiplicador in pasos:
        print(f"Multiplicando: {multiplicando}, Multiplicador: {multiplicador}")

    print(f"El producto de {A} y {B} por el método de la multiplicación rusa es: {resultado}")

except ValueError:
        print("Por favor, ingrese valores numéricos enteros válidos.")

# ----------------------------------------------------------------------------------------
# Fin.
# ----------------------------------------------------------------------------------------