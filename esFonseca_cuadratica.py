# ----------------------------------------------------------------------------------------
# PROGRAMA: esFonseca_cuadratica.py
# ----------------------------------------------------------------------------------------
# Descripción: Este programa resuelve una ecuación cuadrática de la forma ax^2 + bx + c = 0,
#              donde el usuario ingresa los coeficientes a, b y c. Luego, el programa calcula
#              las soluciones de la ecuación y las muestra en pantalla.
# ----------------------------------------------------------------------------------------
# Autor: Sebastian Fonseca Rodriguez
# Version: 1.0
# [29.07.2024]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import math
import datetime   # modulo de python para este ejemplo (se usara para mostrar la fecha)
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# PRE-CONDICIONES
# - Los coeficientes a, b y c deben ser números reales.
# - El coeficiente a no puede ser igual a cero, ya que eso convertiría la ecuación en lineal.
# - El discriminante (b^2 - 4ac) debe ser mayor o igual a cero para que la ecuación tenga soluciones reales.
# VARIABLES GLOBALES
a = None  # Coeficiente a de la ecuación cuadrática
b = None  # Coeficiente b de la ecuación cuadrática
c = None  # Coeficiente c de la ecuación cuadrática
descriminante = None  # Discriminante de la ecuación cuadrática
x1 = None  # Primera solución de la ecuación cuadrática
x2 = None  # Segunda solución de la ecuación cuadrática
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# - Si el discriminante es menor que cero, la ecuación no tiene soluciones reales.
# - Si el discriminante es mayor o igual a cero, la ecuación tiene soluciones reales.
# - Las soluciones de la ecuación cuadrática se calculan correctamente.
# ----------------------------------------------------------------------------------------
# PARAMETROS
# ----------------------------------------------------------------------------------------
# listar aqui los parámetros

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

descriminante = b**2 - 4*a*c

# <<Escriba desde aqui el código del programa...>>
print("*** Un programa para mostrar una plantila para la escritura del código *** ")
print(datetime.date.today())

if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
    print("Los coeficientes deben ser números reales.")
    exit()

if a == 0:
    print("El coeficiente 'a' no puede ser igual a cero, ya que eso convertiría la ecuación en lineal.")
    exit()

if descriminante < 0:
    print("La ecuación no tiene soluciones reales")
    exit()

else:
    x1 = (-b + math.sqrt(descriminante)) / (2*a)
    x2 = (-b - math.sqrt(descriminante)) / (2*a)
    print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
