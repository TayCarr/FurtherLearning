#exercise 27 
'''
   Just memorizing a truth table
   *skipped* cause i do know it...
'''

#exercise 28 
'''
   Just working through different logics and if it results in True or False
   did it quickly for fun little practice 
'''

#exercise 29 What If
'''
    introduction of if statement 
    here i started to put them into functions cause ya..
'''

def ex29():
    people = 20
    cats = 30
    dogs = 15 

    if people < cats:
        print("Too many cats! The world is doomed!")

    if people > cats:
        print("Not may cats! The world is saved!")

    if people < dogs:
        print("The world is drooled on!")

    if people > dogs:
        print("The world is dry!")

    dogs += 5

    if people >= dogs:
        print("People are greater than or equal to dogs.")

    if people <= dogs:
        print("People are less than or equal to dogs.")

    if people == dogs:
        print("People are dogs.")

#run functions below

#ex29()