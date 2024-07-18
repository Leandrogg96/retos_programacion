"""
 * Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automatica.
 * - Si le pasamos "Hola mundo" nos retornaria "odnum aloH"
"""

def reversing_string(text):
    character = list(text)

    large = len(character)

    for i in range(large // 2):
        character[i], character[large-i-1] = character[large-i-1], character[i]
    
    reverse_string = ''.join(character)
    return reverse_string

example_string = "hello world"
example_reverse_string = reversing_string(example_string)

print(f'# Original string: {example_string}')
print(f'# Reversed string: {example_reverse_string}')