#exercise 26 Test
'''
   Take badly written code and fix it
   this is from a previous exercise that was made poorly this will be how i fixed it
'''
#need to import for argv use
from sys import argv
script, filename = argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
#forgot to make variable
height = input()
print("How much do you weigh?", end=' ') #missing )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#moved to top under import

txt = open(filename) #mispelled

print("Here's your file {filename}:")
print(txt.read()) #mispelled

print("Type the filename again:")
file_again = input() # removed "> " from input

txt_again = open(file_again)

print(txt_again.read()) #.read() not _read()

#missing escape
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') #need to move to one line or use """

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #closing "
print(poem)
print("--------------") #opening "


five = 10 - 2 + 3 - 6 #need to input last number to make it 5 10-2 = 8+3 = 11-x = 5 -> 11-5 = 6
print(f"This should be five: {five}") #closing bracket

def secret_formula(started): #missing :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 #missing math operator, just did / cause thats what other did
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #missing crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #missing _ in var
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 #cats not cates
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") #missing ()

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: #missing :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #missing :
    print("People are less than or equal to dogs.") #missing "


if people == dogs: # == not = 
    print("People are dogs.")

