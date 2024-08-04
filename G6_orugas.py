# ----------------------------------------------------------------------------------------
# PROGRAMA: G6_orugas.py
# ----------------------------------------------------------------------------------------
# Descripción: 
# Construya un programa que muestre, día a día, la posición de cada una de ellas hasta que ambas o bien
# alcanzan el fruto, lo comparten, o bien si mueren en el intento.
# a. [15%] Mostrar día a día (por pantalla) la posición acumulada recorrida por la oruga amarilla y la longitud
# de la rama. ¿Qué día alcanza la oruga amarilla el fruto o muere en su intento?
# b. [15%] Mostrar día a día (por pantalla) la posición acumulada recorrida por la oruga verde y la longitud
# de la rama. ¿Qué día alcanza la oruga verde el fruto o muere en su intento?
# Observaciones y Restricciones
# • Resuelva el ejercicio solo a partir de los temas visto en el curso.
# • Se tendrá en cuenta las precondiciones y la claridad del código.
# • Se tendrá en cuenta el orden y claridad de la información mostrada por pantalla.
# ----------------------------------------------------------------------------------------
# Autores:
# JONATAN SANTIAGO ARANDA NIEVES
# EDGAR SEBASTIAN FONSECA RODRIGUEZ
# CESAR GONZALEZ CORTES
# Version: 1.0
# [30.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES 
#----------------------------------------------------------------------------------------
# numero_in = Almacena el número ingresado por el usuario para su posterior validación
#----------------------------------------------------------------------------------------
# PRECONDICIONES
# ----------------------------------------------------------------------------------------
# 1. El Numero ingresado debe ser natural.
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# 1. El programa debe determinar si el número dado es primo o no.
# 2. El programa debe mostrar un mensaje indicando si el número es primo o no.
# 
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros
# Definimos las condiciones iniciales
# Simulación de las orugas amarilla y verde

# Definimos las condiciones iniciales
longitud_inicial_rama = 100  # 1 metro en centímetros
incremento_diario_rama = 10  # incremento de la longitud de la rama cada noche

# Oruga amarilla
posicion_amarilla = 0
distancia_diaria_amarilla = 1

# Oruga verde
posicion_verde = [0,0]
distancia_diaria_verde = 2  # Primeros dos días

# Definimos el límite de días que pueden sobrevivir sin comer
limite_dias = 10

print("Simulación del experimento con orugas")

# Simulación día a día
for dia in range(1, limite_dias + 1):

    if dia == 1:
        posicion_amarilla = distancia_diaria_amarilla
        posicion_verde[0] = distancia_diaria_verde
        
    elif dia == 2:
        distancia_diaria_amarilla *= 2
        posicion_amarilla = distancia_diaria_amarilla
        #print(str(posicion_verde[0]))
        posicion_verde[1] =  posicion_verde[0]
    else:
        distancia_diaria_amarilla *= 2
        posicion_amarilla = distancia_diaria_amarilla

        distancia_diaria_verde = posicion_verde[0]+posicion_verde[1]
        posicion_verde[1]=posicion_verde[0]
        posicion_verde[0]=distancia_diaria_verde
        

    
    # Incrementar la longitud de la rama cada noche
    longitud_rama = longitud_inicial_rama + (incremento_diario_rama * dia)

    # Mostrar el estado del día
    print(f"Día {dia}:")
    print(f"  Oruga amarilla - Posición: {posicion_amarilla} cm, Longitud de la rama: {longitud_rama} cm")
    print(f"  Oruga verde - Posición: {posicion_verde[0]+posicion_verde[1]} cm, Longitud de la rama: {longitud_rama} cm")

    # Verificar si alguna oruga ha alcanzado el fruto
    if posicion_amarilla >= longitud_rama and posicion_verde[0]+posicion_verde[1] >= longitud_rama:
        print("Ambas orugas han alcanzado el fruto y lo comparten.")
        break
    elif posicion_amarilla >= longitud_rama:
        print("La oruga amarilla ha alcanzado el fruto.")
        break
    elif posicion_verde[0]+posicion_verde[1] >= longitud_rama:
        print("La oruga verde ha alcanzado el fruto.")
        break

    
    if dia == limite_dias :
        print("Las orugas no han logrado alcanzar el fruto y han muerto en el intento.")
        break 

# ----------------------------------------------------------------------------------------
# Fin.
# ----------------------------------------------------------------------------------------

