#caesar cipher hacker (brute force)
#www.nostarch.com/crackingcodes (some changes i made)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.' 

def brutecaesar(message):
    #loop through all possible keys
    for key in range(len(SYMBOLS)):
        translated = '' #want to set the string to be blank so that with each new iteration it is a blank string to build on

        #loop through each symbol in the message
        for symbol in message:
            if symbol in SYMBOLS:
                symbolindex = SYMBOLS.find(symbol)
                translatedindex = symbolindex - key

                #for the wrap around
                if translatedindex < 0:
                    translatedindex = translatedindex + len(SYMBOLS)

                #append the translated symbols to the string
                translated = translated + SYMBOLS[translatedindex]

            else:
                #append without encryption/decryption
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))
