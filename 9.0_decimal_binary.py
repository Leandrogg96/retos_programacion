"""
 * Crea un programa se encargue de transformar un numero decimal a binario.
 -  No utilizar funciones propias del lenguaje que lo hagan directamente
"""

def decimal_to_binary(number):
    if number == 0:
        return "0"
    
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    
    return binary

# Example of use

number = 43
number_binary = decimal_to_binary(number)
print(f'The number "{number}" in binary is: {number_binary}') 