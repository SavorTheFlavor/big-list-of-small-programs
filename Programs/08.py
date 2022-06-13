def ROT13(word):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for i in word:
        char = i.lower()
        
        # Checks if the character can be translated then decides whether to
        # add or subtract 13 from the index based on the string length
        if char in characters:
            if characters.index(char) + 13 < len(characters):
                char = characters[characters.index(char) + 13]
            else:
                char = characters[characters.index(char) - 13]

        # Checking for uppercase
        if i.isupper():
            char = char.upper()

        encrypted += char
    return encrypted

# Tests and functionality 
print(ROT13('rot13'))
print(ROT13('handles spaces'))
print(ROT13('HANDLES UPPERCASE'))
print(ROT13(ROT13('Encrypts, and decrypts with the same function')))