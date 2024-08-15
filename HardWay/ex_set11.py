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