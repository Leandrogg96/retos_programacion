"""
* Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
* - Los signos de puntuacion no forman parte de la palabra.
* - Una palabra es la misma aunque aparezca en mayusculas y minusculas.
* - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automaticamente.
"""

import string

def counter_words(text):
    # Delete signs of punctuation
    text_without_punctuation = ""
    for char in text:
        if char not in string.punctuation:
            text_without_punctuation += char

    # Convert text to lowercase
    text_without_punctuation = text_without_punctuation.lower()

    # Slice the text in words
    words = text_without_punctuation.split()

    # Counting words
    count_words = {}
    for word in words:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1

    # Showing final result of repetition words
    ordered_list = sort_dictionary_descending(count_words)

    for element in ordered_list:
        print(f"{element}")
    
    # Showing the number of words in the text
    print(f'# Total number of words: {len(ordered_list)}')

def sort_dictionary_descending(dictionary):
    # Convert the dictionary in one lista of tuples (key, value)
    items = list(dictionary.items())
    
    # Sort the list of tuples in descending order by value
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:
                # Swap if the value of the current element is less than the value of the next element
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items

# Example of use (1)
text = """
Fue una mañana que yo te encontré
Cuando la brisa besaba tu dulce piel
Tus ojos tristes que al ver adoré
La noche que yo te ame, eh

Azul, cuando el silencio por fin te bese
Azul, sentí muy dentro nacer este amor
Azul, hoy miro al cielo y en ti puedo ver
La estrella que siempre soñé

Azul, y es que este amor es azul como el mar
Azul, como de tu mirada nació mi ilusión
Azul como una lagrima cuando hay perdón
Tan puro y tan azul que embriagó el corazón

Es que este amor es azul como el mar
Azul, como el azul del cielo nació entre los dos
Azul, como el lucero de nuestra pasión
Un manantial azul
Que me llena de amor

Como el milagro que tanto espere
Eres la niña que siempre busque
Azul, es tu inocencia que quiero entender
Tu príncipe azul yo seré

Azul, es mi locura si estoy junto a ti
Azul, rayo de luna serás para mi
Azul, con la lluvia pintada de azul
Por siempre serás solo tu

Azul, y es que este amor es azul como el mar
Azul, como de tu mirada nació mi ilusión
Azul como una lagrima cuando hay perdón
Tan puro y tan azul que embriagó el corazón

Es que este amor es azul como el mar
Azul, como el azul del cielo nació entre los dos
Azul, como el lucero de nuestra pasión
Un manantial azul
Que me llena de amor

Azul, y es que este amor es azul como el mar
Azul, como de tu mirada nació mi ilusión
Azul como una lagrima cuando hay perdón
Tan puro y tan azul que embriagó el corazón

Es que este amor es azul como el mar
Azul, como el azul del cielo nació entre los dos
Azul, como el lucero de nuestra pasión
Un manantial azul
Que me llena de amor

Es que este amor es azul como el mar
Azul, como de tu mirada nació mi ilusión
Azul como una lagrima cuando hay perdón
Un manantial azul
Que me llena de amor
"""

counter_words(text)

print("---------------------------------------------------------------------------------------------")
# Example of use (2)

text1 = """
Tengo marcado en el pecho
Todos los días que el tiempo
No me dejó estar aquí

Tengo una fe que madura
Que va conmigo y me cura
Desde que te conocí

Tengo una huella perdida
Entre tu sombra y la mía
Que no me deja mentir, no, no

Soy una moneda en la fuente
Tú, mi deseo pendiente
Mis ganas de revivir

Tengo una mañana constante
Y una acuarela esperando
Verte pintado de azul

Tengo tu amor y tu suerte
Y un caminito empinado
Tengo el mar del otro lado
Tú eres mi norte y mi sur

Hoy voy a verte de nuevo
Voy a envolverme en tu ropa
Susúrrame en tu silencio
Cuando me veas llegar

Hoy voy a verte de nuevo
Voy a alegrar tus tristezas
Vamos a hacer una fiesta
Pa' que este amor crezca más

Sí, sí
Suena Valentino Merlo
Desde la casa de la cumbia
Capítulo 2

Tengo una frase colgada
Entre mi boca y mi almohada
Que me desnuda ante ti, oh-oh

Tengo una playa y un pueblo
Que me acompaña de noche
Cuando no estás junto a mí

Tengo una mañana constante
Y una acuarela esperando
Verte pintada de azul

Tengo tu amor y tu suerte
Y un caminito empinado
Tengo el mar del otro lado
Tú eres mi norte y mi sur

Hoy voy a verte de nuevo
Voy a envolverme en tu ropa
Susúrrame en tu silencio
Cuando me veas llegar

Hoy voy a verte de nuevo
Voy a alegrar tu tristeza
Vamos a hacer una fiesta
Pa' que este amor crezca más

Sí, sí
Argentina, Uruguay
Uruguay y Argentina
Desde la casa de la cumbia
Te traigo el sabor
"""

counter_words(text1)