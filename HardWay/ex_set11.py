'''
Starting a new file for next group of exs don't want the other to get too long
    it is hard to stick with this very very basic new stuff get kinda bored I just quickly read through it and skip over...
'''
#ex 11 ASKING QUESTIONS
#finally getting user input woo 
'''
print("How old are you?", end=' ') #end= specify to use a space instead of new line at the end of print
age = input() #read from standard input by default new line is stripped 
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
'''

#ex 12 PROMPTING PEOPLE
#shows how to prompt for input directling in your input() call
'''
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
'''

#ex 13 
#introduces another way to run scripts i guess uses comand line args 
'''
from sys import argv #need to import this module in order to use argv command line stuff 
#note: read the WYSS section for how to run this 
script, first, second, third = argv

print("The script is called: ", script) #first variable passed will be the script that is called
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
#here wont be able to hit run in vsc will have to actually run from terminal..
#   in the terminal: python3 ex_set11.py first second third 
#   -->python3 to run, ex_set11.py being the script name, first second third can be replaced with whatver 

#additional study drill combine argv and user input
#here I will pass some numbers and ask user to calculate 
answer = input(f"{first} + {second} = ")
print(f"You answered: {answer}, the correct answer is {third}!")
'''
#ex 14
'''
from sys import argv
script, user_name = argv
prompt = '>'
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
'''

#ex 15
'''
from sys import argv
script, filename = argv
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()
'''

#ex 16 Reading and Writing Files
'''
Various commands that are good to know 
-> close, closes the file
-> read, reads the contents of a file you can assign them to a variable
-> readline, reads one line of the text file 
-> truncate, empties the file 
-> write("stuff"), writes the "stuff" string to file 
-> seek(0), moves the read/write location to the start of the file 

below uses some
'''
'''
from sys import argv

script, filename = argv #pull filename from arg

print(f"We're going to erase {filename}.") #print filename
print("If you do not want that hit CTRL-C (^C).") #close program
print("If you do want that, hit RETURN.") 

input("?") #get input will acept anything not save it 

print("Opening the file...")
target = open(filename, 'w') #open file in write

print("Truncating the file. Goodbye!")
target.truncate() #empties file

print("Now I am going to ask you for three lines.")

line1 = input("Line 1: ") #get lines from user input save to var
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1) #write each line to file 
target.write("\n") #write a new line to go to next
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() #make sure to close the file 
'''

#ex 17 More Files
'''
copy one file to another
'''

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()