#Affine Cipher
#www.nostarch.com/crackingcodes/ (some changes made)

import sys, pyperclip, cryptoMath, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' 

def main():
    message = """This is my message that I am wanting to encrypt. It is a message with different ummm words and letters and ya things. 
    - Me..."""
    message = """PXAiQAiQocQoaii1uaQLX1LQEQ1oQI1RLARuQL9QaRG6clLNQELQAiQ1Qoaii1uaQIALXQxADDa6aRLQ3oooQI96xiQ1RxQ!aLLa6iQ1RxQc1QLXARuiNQ
QQQQ-QsaNNN"""

    key = 2894
    #mode = 'encrypt' #encrypt or decrypt 
    mode = 'decrypt'

    if mode == 'encrypt':
        translated = encryptMessage(key, message)

    elif mode == 'decrypt':
        translated = decryptMessage(key, message)
    
    print('Key: %s' % (key))
    print('%sed text: ' % (mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied' % (mode))

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)

    return(keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak with keyA = 1, choose different key value.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak with keyB = 0, choose different key value.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('keya must be greater than 0 and key b must be between 0 and %s' % (len(SYMBOLS) - 1))
    if cryptoMath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('keyA (%s) and the symbol set size (%s) are not relatively prime, choose a differetn key.' % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            #encrypt symbol
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol #append without encryption
    return ciphertext

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseKeyA = cryptoMath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            #decrypt
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol #dont decrypt

    return plaintext  

def getRandKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))

        if cryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
    main()