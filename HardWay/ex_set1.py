#I havent decided if i want to skip these easy ones maybe for now i will just do them...
'''
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing")
print("I'd much rather you 'not'.")
print('I "said" do not touch this')
'''

#study drills -> asked to print another line, make script only print one of the lines and to use # for now i will skip these
#skipping ex2.py as it just shows comments and ya...
#study drills are asking to look for mistakes in the code and asking about the #

'''
#ex3.py
# i am just gonna continue to have these short drills in the same file 
#some of my own formatting thrown in here
print("I will now count my chickens: ")
print("\tHens: ", 25 + 30 / 6) # = 30 -> 30 / 6 = 5 + 25 = 30
print("\tRoosters: ", 100 - 25 * 3 % 4) # = 97 -> 25*3 = 75%4=3 100-3 = 97

print("Now I will count the eggs: ", end="")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
#4%2 = 0, 1/4=.25
#3+2+1-5+0-0.25+6 = 6.75

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh that is why it is False.")
print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is is greater than or equal to?", 5 >= -2)
print("Is it less than or equal to?", 5 <= -2)
'''

#ex4.py
#this introduces variables and their use
'''
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", car_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
'''

#ex 5 
# more variables and printing 
'''
name = 'Taylor C.'
age = 25
height = 65 #inches
weight = 140 #lbs
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"She's {height} inches tall.")
print(f"She's {weight} pounds heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")

total = age + height + weight
print(f"If I add {age} + {height} + {weight} I get {total}.")
'''

#ex 6
#practice with string variables and using the .format()
'''
type_people = 10
x = f"There are {type_people} types of people."

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said : '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = " a string with a right side."

print(w + e)'''

#ex 7
'''
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #will print . 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end= '-') #end=' ' leaves a - at the end of the concat string
print(end7 + end8 + end9 + end10 + end11 + end12)
'''

#ex 8 
#skipping this cause its more strings using .format()

#ex 9
#skipping most of this except for the last concept as I thought it was good to note the use of triple quotes when printing
#if using """ """ withing print you can do multiple lines and they will be printed in that format
'''
print("""
This is the first line
then the second 
and the third 
and you can keep going
    you can even tab and it will print it
""")
'''

#ex 10 
#goes over different escapes you can use  I will be skipping this too 