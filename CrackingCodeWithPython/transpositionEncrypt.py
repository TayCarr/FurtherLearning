#www.nostarch.com/crackingcodes (with some changes of my own)

'''
    How transposition cipher works, this cipher rearranges the message symbols into an order that makes the original
    message unreadable, each key creates a different permutation of the characters
    steps for encryption (by hand):
        1. count the # of chars in the message and the key
        2. draw a row of a number of boxes equal to the key (ex key = 8 then there is 8 boxes in a row)
        3. start filling in the boxes from left to right, one char / box
        4. add another row if you run out of boxes
        5. when you get to the last char shade in the remaining boxes
        6. starting from top left corner go down the column writing out each character once at the bottom go to the next column and go down
            skipping any shaded boxes, this will result in the ciphertext

    picking a key it is typically from 2 up to half the size of the message, longer the message the more possible keys
'''

import pyperclip
import sys

def main():
    #check if arg given 
    if len(sys.argv) > 1:
        print(f"String provided: {sys.argv[1]} and the key is {sys.argv[2]}")

        message = sys.argv[1]
        key = sys.argv[2]
        
        ciphertext = encryptMessage(key, message)
        print(ciphertext + '|') #print with pipe at the end incase there are spaces at the end of the text
        pyperclip.copy(ciphertext)
    
    else:
        print("No arguments provided. I will give you one...")
        message = "Common sense is not so common."
        key = 8
        ciphertext = encryptMessage(key, message)
        print(ciphertext + '|') #print with pipe at the end incase there are spaces at the end of the text
        pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    #each string in ciphertext represents a column in the grid
    ciphertext = [''] * key
    #loop through each column in the ciphertext
    for column in range(key):
        currIndex = column
        #print("currindex/column", currIndex)

        #loop until currindex goes past the length of the message 
        while currIndex < len(message):
            #print(ciphertext[column])
            #print(message[currIndex])
            #place char at currindex in message at the end of the curr column in ciphertext list
            ciphertext[column] += message[currIndex]
            #print(ciphertext[column])

            #go to next
            currIndex += key
            #print("new index", currIndex)
    return ''.join(ciphertext)

#if prog ran and not imported as module call main
if __name__ == '__main__':
    main()