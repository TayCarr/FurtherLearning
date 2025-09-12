#transposition cipher test
#www.nostrach.com/crackingcodes

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) #set the random seeds to a static value

    for i in range(20): #run 20 tests
        #generate random messages to test

        #message will have a random length 
        message = 'ABCDEFGHIJKLMNOPQRSTUVYXWZ' * random.randint(4, 40)

        #convert message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) #back to string

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        #check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print("Mismatch with key %s and message %s" % (key, message))
                print("Decrypted as: " + decrypted)
                sys.exit()
        print("Transposition tests passed")

if __name__ == '__main__':
    main()