"""
 * Crea una unica funcion (importante que solo sea una) que sea capaz de calcular y retornar el area de un poligono.
 * - La funcion recibira por parametro solo UN poligono a la vez.
 * - Los poligonos soportados seran Triangulo, Cuadrado y Rectangulo.
 * - Imprime el calculo del area de un poligono de cada tipo.
"""
import math

def area_polygon(polygon):
    if isinstance(polygon, Triangle):
        return [(polygon.base * polygon.height) / 2]
    elif isinstance(polygon, Rectangle):
        return [polygon.base * polygon.height]
    elif isinstance(polygon, Square):
        return [polygon.side * polygon.side]
    else:
        return ValueError("Polygon not supported.")
    
# Definition of supported polygon classes

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

class Square:
    def __init__(self, side):
        self.side = side

class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

# Static polygon assignment

triangle_1 = Triangle(3,4)
square_1 = Square(4)
rectangle_1 = Rectangle(2,9)

# Calculate and display of polygon areas

print(f'Area of triangle 1: {area_polygon(triangle_1)}')
print(f'Area of square 1: {area_polygon(square_1)}')
print(f'Area of rectangle 1: {area_polygon(rectangle_1)}')
