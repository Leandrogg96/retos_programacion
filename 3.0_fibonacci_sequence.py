"""
 * Escribe un programa que imprima los 50 primeros numeros de la sucesion
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesion de numeros en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def function_fibonacci(range):
    fibo_sequence = [0,1]
    while len(fibo_sequence) < range:
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
    return fibo_sequence

def print_fibo_numbers(max):
    fibo_numbers = function_fibonacci(max)
    for number in fibo_numbers:
        print(number)
    return

print_fibo_numbers(50)