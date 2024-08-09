# ----------------------------------------------------------------------------------------
# PROGRAMA: Grupo6_picasFijas
# ----------------------------------------------------------------------------------------
# Descripción: Un juego muy conocido para pasar el tiempo es “picas y fijas”, el cual consiste en tratar de adivinar
# un número en la menor cantidad de intentos posible. En cada intento, el jugador dice 4 dígitos (no
# repetidos) y el oponente le da pistas de cuántos aciertos tuvo, sin indicarle cuales fuero
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [31.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import random

# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------

# << aqui una explicación concreta >>

# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

def generadorNumeroSecreto():
    # Crea la lista
    NumeroSecreto = []
    while len(NumeroSecreto) < 4: #while para que se ejecute mientras la longitud de la lista sea menor a 4
        numero = random.randint(0, 9) # Genera un numero randomico       
        if numero not in NumeroSecreto: # condicion que valida que el numero no este en la lista
            NumeroSecreto.append(numero) # Agrega el dijito a la lista    
    return NumeroSecreto

def picas(numeroSecreto, juego):
    i=0
    contador =0
    for i in range(len(juego)):
        if numeroSecreto[i] in juego:
            #print(numeroSecreto[i])
            contador +=1
    return contador
        
# Generar el número secreto
numero_secreto = generadorNumeroSecreto()
juego = [4, 3, 2, 1]
total_picas = picas(numero_secreto,juego)

# Imprimir el número secreto
print("Número Secreto:", numero_secreto)
print("Número de picas:", total_picas)

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------