# ----------------------------------------------------------------------------------------
# PROGRAMA: <<nombre del programa>>
# ----------------------------------------------------------------------------------------
# Descripción: 
# Este programa tiene como objetivo implementar un conjunto de funciones para resolver las
# siguientes tareas: crear dos listas de 10 valores enteros cada una, donde la primera 
# lista, denominada listaUno, debe ser generada de manera aleatoria, y la segunda lista, 
# denominada listaDos, se debe generar a partir de 10 valores enteros que serán pedidos al 
# usuario uno por uno. Además, se crearán dos listas inicialmente vacías: listaClonada y 
# listaSuma. El programa principal presentará un menú con opciones para llevar a cabo 
# las tareas indicadas.
# ----------------------------------------------------------------------------------------
# Autor: 
# Version: 2.0
# [18.07.2020]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import datetime   # modulo de python para este ejemplo (se usara para mostrar la fecha)
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

def main():
    # Crear las listas listaUno y listaDos
    listaUno = generar_lista_aleatoria(10)
    listaDos = generar_lista_usuario(10)
    
    # Crear las listas listaClonada y listaSuma
    listaClonada = []
    listaSuma = []
    
    # Mostrar el menú y realizar las tareas indicadas
    while True:
        print("----- MENÚ -----")
        print("1. Mostrar Valores (listaUno y listaDos")
        print("2. Clonar listaUno")
        print("3. Sumar listas")
        print("4. Salir")
        
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            mostrar_valores(listaUno, listaDos)
        elif opcion == 2:
            listaClonada = clonar_lista(listaUno)
            print("Lista clonada:", listaClonada)
        elif opcion == 3:
            listaSuma = sumar_listas(listaUno, listaDos)
            print("Lista suma:", listaSuma)
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    
    print("Fin del programa.")

# Función para generar una lista aleatoria de tamaño n
def generar_lista_aleatoria(n):
    return [random.randint(1, 100) for _ in range(n)]

# Función para generar una lista ingresada por el usuario de tamaño n
def generar_lista_usuario(n):
    lista = []
    for i in range(n):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        lista.append(valor)
    return lista

# Función para mostrar los valores de listaUno y listaDos
def mostrar_valores(listaUno, listaDos):
    print("Valores de listaUno:", listaUno)
    print("Valores de listaDos:", listaDos)

# Función para clonar una lista
def clonar_lista(lista):
    return lista.copy()

# Función para sumar dos listas elemento a elemento
def sumar_listas(lista1, lista2):
    return [x + y for x, y in zip(lista1, lista2)]

# Llamar a la función main
if __name__ == "__main__":
    main()
# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------