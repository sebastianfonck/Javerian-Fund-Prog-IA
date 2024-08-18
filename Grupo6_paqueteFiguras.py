class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimetro(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado


class Rectangulo(Figura):
    def __init__(self, base, altura, color):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio
    
    class Menu:
        def __init__(self):
            self.figuras = []

        def agregar_figura(self, figura):
            self.figuras.append(figura)

        def mostrar_figuras(self):
            for figura in self.figuras:
                print(f"Figura: {type(figura).__name__}")
                print(f"Color: {figura.color}")
                print(f"Área: {figura.area()}")
                print(f"Perímetro: {figura.perimetro()}")
                print()

    # Example usage:
    menu = Menu()
    cuadrado = Cuadrado(5, "rojo")
    rectangulo = Rectangulo(4, 6, "azul")
    #circulo = Circulo(3, "verde")

    menu.agregar_figura(cuadrado)
    menu.agregar_figura(rectangulo)
    #menu.agregar_figura(circulo)

    menu.mostrar_figuras()