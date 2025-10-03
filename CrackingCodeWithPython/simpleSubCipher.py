#Simple Substitution Cipher
#www.nostarch.com/crackingcodes/
'''
    We choose a random letter to encrypt each letter of the alphabet, using each letter only once. The key for the simple
    sub cipher is always a string of 26 letters of the alphabet in random order. there are a lot A LOT of possible key orderings
    for the simple sub cipher. this number is so large that it is impossible to brute force
    short example for the key and how to code with it
        if the start of our key is VHTGFYSJ....
        then we align it like such (if we were doing by hand)
            ABCDEFGH...
            VHTGFYSJ...
        to encrypt find the letter of the plaintext and encrypt that letter as the aligned letter in the key A->V
'''

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = 'Once again here I am writing my message that I need to be encrypted. There really is nothing of worth in this message I am just trying to make it long and have a variety of letters, even punctuation. If this is decoded and there is spelling mistakes just know it is likely my inability to spell... -T'
    message = 'Ghet quqoh itst O qj vsozohu jn jtaaqut ziqz O httr zg wt thesnfztr. Zitst stqkkn oa hgziohu gy vgszi oh zioa jtaaqut O qj pxaz zsnohu zg jqlt oz kghu qhr iqct q cqsotzn gy ktzztsa, tcth fxhezxqzogh. Oy zioa oa rtegrtr qhr zitst oa aftkkohu joazqlta pxaz lhgv oz oa koltkn jn ohqwokozn zg aftkk... -Z'
    #Here the key can be whatever order (i typed the order of the keyboard...)
    key = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    #mode = 'encrypt' #set mode encrypt or decrypt
    mode = 'decrypt'

    if not validKey(key):
        sys.exit('There is an error in the key/symbol set')
    
    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)
    
    print("Using key %s" % (key))
    print("The %sed message is: " % (mode))
    print(translated)
    pyperclip.copy(translated)
    print("\nMessage has been copied to clipboard")

def validKey(key):
    keylist = list(key)
    letterlist = list(LETTERS)

    keylist.sort()
    letterlist.sort()

    return keylist == letterlist

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        #swap key and letters around
        charsA, charsB = charsB, charsA
    
    #look at each letter in the message
    for symbol in message:
        if symbol.upper() in charsA:
            #encrypt/decrypt symbol
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symbolIndex].upper()
            else:
                translated += charsB[symbolIndex].lower()
        else:
            #symbol not in key set so dont change
            translated += symbol

    return translated

def getRandKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()