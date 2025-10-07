#vigenere cipher dictionary hacker
#www.nostarch.com/crackingcodes/

import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
     #for this example it will show you a possible crack but if you continue to crack it will give a better crack after
    
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print('Copying hacked messaged')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack :(')

def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip() #remove new line
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)

        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            #check with user
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()

