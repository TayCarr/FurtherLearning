#Caesar Cipher
#nostarch.com/crackingcodes (but I changed up a little bit)
'''
Letters are asigned a number value A=0, B=1,...Z=25 the key is a given number and that is how many shifted the 
original letter to get the encrypted letter 
example if key=2 then the message THE -> VJG 
to retrieve the original message you shift backwards by the key
if a number is greater than 25 then it will wrap back around so 26=0 28=2 think of mod25
'''

import pyperclip #downloaded from the above site
import sys #grabbing argv

#Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' #can expand this to other symbols
#changing the order will change the encryption like A=0 right now but if i swapped this around and had ? where A is then ?=0

def caesarcipher(message, key, mode):
    translated = '' #to store the resulting string

    for symbol in message:
        #note only symbols in SYMBOLS string can be encrypted/decrypted
        if symbol in SYMBOLS:
            symbolindex = SYMBOLS.find(symbol) #find returns int index
            #perform ecryption/decryption
            if mode == 'encrypt':
                #print('mode encrypt')
                translatedindex = symbolindex + key
                if translatedindex >= len(SYMBOLS):
                    translatedindex = translatedindex - len(SYMBOLS)
            elif mode == 'decrypt':
                #print('mode decrypt')
                translatedindex = symbolindex - key
                if translatedindex < 0:
                    translatedindex = translatedindex + len(SYMBOLS)

            #here is where you need to handle the wrap around 
            #might move this up idk
            '''
            if translatedindex >= len(SYMBOLS):
                translatedindex = translatedindex - len(SYMBOLS)
            elif translatedindex < 0:
                translatedindex = translatedindex + len(SYMBOLS)
            '''

            translated = translated +SYMBOLS[translatedindex]

        else:
            #append without encrypting if it is not in the list of symbols
            translated = translated + symbol

    pyperclip.copy(translated) #this copies the message to your clipboard
    return translated


#check if arg given 
if len(sys.argv) > 1:
    print(f"String provided: {sys.argv[1]} and the key is {sys.argv[2]} mode: {sys.argv[3]}")

    message = sys.argv[1]
    key = sys.argv[2]
    mode = sys.argv[3] #either encrypt or decrypt
    print(caesarcipher(message, int(key), mode))
    
else:
    print("No arguments provided. I will give you one...")
    message = "This is my secret message."
    key = 13
    mode = 'encrypt'
    print(caesarcipher(message, key, mode))
    #print(caesarcipher(input("Enter a message: ")))



