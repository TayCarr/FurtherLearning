#www.nostarch.com/crackingcodes (added some changes)

'''
    How decryption of transposition ciphertext works
    If you send someone the encrypted message and they know the key then the steps are as follows
        1. calculate the number of columns needed by dividing the length of message by the key and round up to whole number
        2. draw boxes (number of rows is the key) key=row column=calculated
        3. calculate the number of boxes to shade by taking the total number (row x column) and subtract the length of the ciphertext
        4. shade in boxes
        5. fill in the chars of ciphertext starting at the top row and go left to right skipping shaded 
        6. get the plaintext by reading the leftmost column then the next column 
'''
import math, pyperclip

def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8

    plaintext = decryptMessage(key, message)

    #print with | at the end so if there is spaces you see them
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    #decryption function will simulate the columns and rows of the grid using a list of strings
    #first calculate the number of columns
    numColumns = int(math.ceil(len(message) / float(key)))
    #assign rows
    numRows = key
    #calculate num of shaded
    numShaded = (numColumns * numRows) - len(message)

    #each string is a column in the grid
    plaintext = [''] * numColumns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 

        #if no more columns or a shaded box go back to first column and next row
        if (column == numColumns) or ((column == numColumns - 1) and (row >= numRows - numShaded)):
            column = 0
            row += 1

    return ''.join(plaintext)

#if prog ran and not imported as module call main
if __name__ == '__main__':
    main()
