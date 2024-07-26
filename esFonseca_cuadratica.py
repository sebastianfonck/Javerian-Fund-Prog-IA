import math

print("********** Ecuación cuadrática **********")

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

descriminante = b**2 - 4*a*c

if descriminante < 0:
    print("La ecuación no tiene soluciones reales")
else:
    x1 = (-b + math.sqrt(descriminante)) / (2*a)
    x2 = (-b - math.sqrt(descriminante)) / (2*a)
    print(f"Las soluciones son x1 = {x1} y x2 = {x2}") 
