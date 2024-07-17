"""
 * Escribe un programa que muestre por consola (con un print) los
 * numeros de 1 a 100 (ambos incluidos y con un salto de linea entre
 * cada impresion), sustituyendo los siguientes:
 * - Multiplos de 3 por la palabra "fizz".
 * - Multiplos de 5 por la palabra "buzz".
 * - Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz(num1, num2):
    if(num1 > num2):
        print("Ingresa un rango correcto, el primer ingreso debe ser mas chico que el segundo.")
        return
    for numero in range(num1, num2 + 1):
        if (numero % 3 == 0 and numero % 5 == 0):
            print("fizzbuzz.")
        elif (numero % 5 == 0):
            print("buzz.")
        elif(numero % 3 == 0):
            print("fizz.")
        else:
            print(numero)

fizz_buzz(1,100)

