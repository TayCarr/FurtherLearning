#vigenere cipher (polyalphabetic substitution cipher)
#www.nostarch.com/crackingcodes/

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    #copy message from the site
    #message = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    message = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf."""
    key = 'ASIMOV'
    #mode = 'encrypt' #encrypt or decrypt
    mode = 'decrypt'

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)

    print('%sed message:' % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('\nThe message has been copied to the clipboard.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []

    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1: #-1 means not found
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS) #handle wrap around

            #add symbol to end of translated
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        
        else:
            #append sybol
            translated.append(symbol)
    
    return ''.join(translated)

if __name__ == '__main__':
    main()