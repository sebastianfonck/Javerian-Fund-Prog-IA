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