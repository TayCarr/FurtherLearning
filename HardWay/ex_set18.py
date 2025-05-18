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