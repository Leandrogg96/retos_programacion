"""
 * Escribe un programa que se encargue de comprobar si un numero es o no primo.
 * Hecho esto, imprime los numeros primos entre 1 y 100.
"""
import math

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = int(math.sqrt(number)) + 1

    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    
    return True

def print_prime_number(max):
    print(f'Prime numbers from 1 to {max}')
    for number in range(1, max+1):
        if is_prime(number):
            print(f'# {number}')


print_prime_number(100)