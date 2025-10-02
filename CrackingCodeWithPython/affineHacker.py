#Affine Cipher Hacker
#www.nostarch.com/crackingcodes

import pyperclip, affineCipher, detectEnglish, cryptoMath

SILENT_MODE = False

def main():
    message = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    hackedMessage = hackAffine(message)

    if hackedMessage != None:
        print("Copying hacked message to clipboard")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print("Failed to hack encryption :(")

def hackAffine(message):
    print('Hacking....')

    #rem to force quit if needed
    print('Reminder to force quit if need to abort process, this could take awhile...')

    #brute force by looping through all possible keys
    for key in range(len(affineCipher.SYMBOLS) ** 2): #** is the exponent operator !! length^2 calculates the possible keys
        keyA = affineCipher.getKeyParts(key)[0]
        
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1: #is key rel prime?
            continue #if key is NOT rel prime then execute continue, we then jump back to start of the loop skipping below UNTIL gcd is 1 
        
        #once the right key is found below will finally execute and skip continue line
        decryptedText = affineCipher.decryptMessage(key, message)

        if not SILENT_MODE: #can switch silent mode to be true then it wont print out all the keys that are tried
            print('Tried key %s.... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            #check with the user if looks correct
            print('\nPossible encryption hack:')
            print('key: %s ' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print('\nEnter D for done, or press enter to continue hacking...')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None #gone through all keys no success return and notify failed to hack

if __name__ == '__main__':
    main()