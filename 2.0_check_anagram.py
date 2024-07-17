"""
 * Escribe una funcion que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) segun sean o no anagramas.
 * - Un Anagrama consiste en formar una word reordenando TODAS las letras de otra word inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def are_anagrams(word1: str, word2: str) -> bool:
    """
    Checks if two words are anagrams.

    Args:
    word1 (str): The first word.
    word2 (str): The second word.

    Returns:
    bool: "True" if they are anagrams, "False" otherwise.
    """
    if word1 == word2:
        print("They're de same word. They aren't anagrams.")
        return False
    return sorted(word1) == sorted(word2)

def is_vailid_word(word: str) -> bool:
    """
    Checks if a word is valid.

    A word is valid if it is not empty, does not contain spaces
    and only has alphabetic characters.
    
    Args:
    word (str): The word to check.
    
    Returns:
    bool: "True" if valid, "False" otherwise.
    """
    return word.isalpha() and ' ' not in word and word.strip() != ""

def ask_words() -> tuple[str, str]:
    """
    Prompts the user to enter two valid words.

    Returns:
    tuple: A pair of valid words.
    """
    while True:
        word1 = input("Enter the first word: ").strip()
        word2 = input("Enter the second word: ").strip()
        
        if is_vailid_word(word1) and is_vailid_word(word2):
            if word1 != word2:
                return word1, word2
            else:
                print("The words should not be exactly the same. Please, try again.")
        else:
            print("Both words must be valid and not empty. They must not contain spaces or non-alphabetic characters. Please try again.")

def main():
    """
    Main function that the program executes.
    """
    word1, word2 = ask_words()
    if are_anagrams(word1, word2):
        print(f'"{word1}" y "{word2}" are anagrams.')
    else:
        print(f'"{word1}" y "{word2}" they are not anagrams.')

if __name__ == "__main__":
    main()
        