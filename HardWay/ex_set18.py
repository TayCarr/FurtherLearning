#example 18 Names, Variables, Code, Functions
'''
finally getting to functions 
    functions do three things:
        name pieces of code the way variables name strings and number
'''

#def declares the function
def print_two(*args):
    arg1, arg2 = args #i didnt know you could do *argument for multi
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2): #just doing it again 
    print(f"arg1: {arg1}, arg2: {arg2}")

#then there is one just taking one arg
#then the one showing dont need to pass arg
def print_none(): #just doing it again 
    print("Nothing passed!")

#now call the functions
#print_two("first", "second")
#print_two_again("first", "second")
#print_none()

#example 19 Functions and Variables 
'''
    an exercise on how the vars in a funct are not connected to ones outside of it 
    local vs global stuff
'''

def cheese_and_crackers(cheese_int, crackers_int):
    print(f"You have {cheese_int} cheeses!")
    print(f"You have {crackers_int} boxes of crackers!")
    print(f"That is {cheese_int + crackers_int}") #i did this instead of the two print statements about a picnic
'''
print("Give numbers directly to the function 20, 10")
cheese_and_crackers(20, 10)

print("Or we can give values to a variable and pass the variable to the function")
cheese = 15
cracker = 11
cheese_and_crackers(cheese, cracker)

print("We can do math inside too")
cheese_and_crackers(20+12, 20-10)

print("We can also do a combination")
cheese_and_crackers(cheese+3, 22-cracker)
'''

#example 20 Functions and Files
'''
    example of how functions and files work together 
    i didnt make a new txt file for this i just used ones already made 
'''
'''
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First print the whole file:\n")
print_all(current_file)

print("Now let's rewind and go back to the start.")
rewind(current_file)

print("Let's print three lines:")

curr_line = 1 
print_a_line(curr_line, current_file)
curr_line += 1
print_a_line(curr_line, current_file)
curr_line += 1
print_a_line(curr_line, current_file)

current_file.close()
'''

#example 21 Functions Can Return Something
'''
    example of how functions can return something and you can assign it to a var
'''

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
'''
print("Let's do some math with functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#extra puzzle 
print("Here is a puzzle:")
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) 
#goes to add but then hits sub then hits mult then hits divide
#goes into divide first 50/2
#mult 180 * 25
#sub 74 - 4500
#add 35 + -4426
print("That becomes: ", what, "Can you do it by hand?")
'''

#exercise 22
'''
    This one just asks you go through and write out words and characters of importance 
    I will skip this since my years in school kinda already have this down...
'''

#exercise 23 Strings Bytes and Character Encoding
'''
    Going to skip this one, it is takeing bytes and encoding decoding, requires a txt off of the books site
    meh
    goes through each line in a file decodes then encodes prints out each step 
    "Decode Bytes Encode Strings
'''

#exercise 24 More Practice 
'''
   Long review exercise sort of, touches on previous 
'''

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do: ')
print("\n newlines and \t tabs")

poem = """
\tThe lovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation 
\n\twhere there is none
"""

print("----------------------------------")
print(poem)
print("----------------------------------")

five = 10 -2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

#another way to format a string
print("With a starting point of: {}".format(start_point))
#or use f print
print(f"We'd have {beans} beans, {jars} jars, {crates} crates.")

start_point = start_point / 10
print("We can also do it this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, {} crates.".format(*formula))

