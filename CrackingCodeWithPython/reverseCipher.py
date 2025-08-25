#Reverse Cipher
#https://www.nostarch.com/crackingcodes/ (BSD Licensed)

#i changed it a wee bit
#if supply a string when running as an arg will reverse that else will ask for message string (did this for testing idk)
#can give an unreversed message to be reversed OR can give a string already been reversed and unreverse it 

import sys

def reverse(message):
    i = len(message) - 1
    translated = ''
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    return translated

#check if arg given 
if len(sys.argv) > 1:
    print(f"String provided: {sys.argv[1:]}")

    message = sys.argv[1]
    print(reverse(message))
else:
    #print("No arguments provided. I will give you one...")
    #print(reverse("I forgot how to run this program"))
    print(reverse(input("Enter a message: ")))

