#transposition encrypt/decrypt file
#www.nostarch.com/crackingcodes (few changes i made)

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    #check if arg given 
    #if doing it this way need file name key size and mode type
    if len(sys.argv) > 1:
        print(f"Filename provided: {sys.argv[1]} and the key is {sys.argv[2]} mode is {sys.argv[3]}")

        inputFilename = sys.argv[1]
        key = sys.argv[2]
        mode = sys.argv[3]
        outputFilename = 'encrypted_' + inputFilename
    
    else: #will run the example text
        print("running example")
        inputFilename = 'example.txt'
        print(inputFilename)
        key = 10
        mode = 'encrypt'
        outputFilename = 'encrypted_example.txt'

    if not os.path.exists(inputFilename):
        print("File does not exist")
        sys.exit()
    if os.path.exists(outputFilename):
        print("A file with the name %s already exists and will be overwritten. (C)ontinue or (Q)uit" % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    #read in the file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (mode.title()))

    #see how long process takes
    startTime = time.time()
    if mode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(int(key), content)
    elif mode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(int(key), content)
        outputFilename = 'decrypted_' + inputFilename

    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s' % (mode.title(), totalTime))

    outputFileobj = open(outputFilename, 'w')
    outputFileobj.write(translated)
    outputFileobj.close()

    print('Done %sing %s (%s characters)' % (mode, inputFilename, len(content)))
    print('%sed file is %s' % (mode.title(), outputFilename))

if __name__ == '__main__':
    main()