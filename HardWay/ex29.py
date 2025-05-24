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

#exercise 30 Else and If
'''
    else and elif introduced
'''

def ex30():
    people = 30
    cars = 40
    trucks = 15 

    if cars > people:
        print("We should take the cars.")
    elif cars < people:
        print("We should not take the cars.")
    else:
        print("We can't decide.")

    if trucks > cars:
        print("That's too many trucks.")
    elif trucks < cars:
        print("Maybe we should take the trucks.")
    else:
        print("We still can't decide.")

    if people > trucks:
        print("Alright, lets just take the trucks.")
    else:
        print("Fine, let's just stay home then.")

#exercise 31 Making Decisions
'''
    diffrent logic branches a "game"
'''
def ex31():
    print("""You enter a dark room with two doors.
    Do you go through door #1 or #2?
    """)

    door = input("> ")

    if door == "1":
        print("There's a giant bear here eating a cheesecake.")
        print("What do you do...?")
        print("1. Take the cake.")
        print("2. Scream at the bear.")

        bear = input("> ")

        if bear == "1":
            print("The bear eats your face off.")
        elif bear == "2":
            print("The bear eats your legs off.")
        else:
            print(f"Well doing {bear} is probably better.")
            print("The bear runs away")

    elif door == "2":
        print("You stare into the endless abyss at Cthulu's retina.")
        print("1. Blueberries.")
        print("2. Yellow Wallpaper.")
        print("Understanding the revolvers melodies.")

        insanity = input("> ")

        if insanity == "1":
            print("Your body survives but it is powered by a mind of jello.")
        else:
            print("The insanity rots your eyes into a pool of muck.")

    else:
        print("You stumble around in the dark and fall on a knife and die.")

    print("Play again? y/n")
    again = input("> ")
    if again == "y":
        ex31()
    return

#exercise 32 Loops and Lists
'''
    build lists using for loops
'''
def ex32():
    the_count = [1,2,3,4,5]
    fruits = ['apples', 'oranges', 'pears', 'apricots']
    change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

    for number in the_count:
        print(f"This is the count {number}")

    for fruit in fruits:
        print(f"A fruit of type: {fruit}")

    for i in change:
        print(f"I got {i}")

    #build a list
    elements = []

    for i in range(0,6):
        print(f"Adding {i} to the list...")
        elements.append(i)
    for i in elements:
        print(f"Element was {i}")

#exercise 33 While Loops
'''
    introducing while loop
'''
def ex33():
    i = 0
    numbers = []

    while i < 6:
        print(f"At the top i is: {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

#exercise 34 Accessing Elements of Lists
'''
   just a pen and paper tracing of lists 
'''

#exercise 35 Branches and Functions
'''
    mixing of the two
'''
from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if type(int(choice)) == int:
        how_much = int(choice)
    else:
        dead("learn to type a number...")

    if how_much < 50:
        print("You're not greedy! You win!")
        exit(0)
    else:
        dead("You are greedy...")

def bear_room():
    print("There is a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door...")
    print("How are you going to move the bear...?")

    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear slaps your face off...")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door...")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("You pissed the bear off and he ate your legs...")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't know what that means...")

def cthulhu_room():
    print("Here you see the great evil Cthulhu...")
    print("It stares at you, and you feel your mind melting")
    print("Do you flee for your life or eat your hand...?")

    choice = ("> ")

    if "flee" in choice:
        start()
    elif "hand" in choice:
        dead("Hope that was at least tasty...")
    else:
        cthulhu_room()

def dead(why):
    print(why)
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door on your right and a door on your left.")
    print("Which do you take...?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around and fall into pit and die...")

def ex35():
    start()

#exercise 36 Design and Debugg
'''
    asks to make your own of the previous I will skip
'''
#exercise 37 Symbol Review
'''
    review logic and keywords and so on... on paper
'''

#exercise 38 Doing Things to Lists
'''
    
'''
def ex38():
    ten_things = "Apples Oranges Crows Telephone Light Sugar"

    print("Wait there are not 10 things in that list. Let's fix that.")

    stuff = ten_things.split(" ")
    more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

    while len(stuff) != 10:
        next_one = more_stuff.pop()
        print("Adding: ", next_one)
        stuff.append(next_one)
        print(f"There are {len(stuff)} items now")

    print("There we go: ", stuff)
    print("Doing some things with stuff:")

    print(stuff[1])
    print(stuff[-1])
    print(stuff.pop())
    print(' '.join(stuff))
    print('#'.join(stuff[3:5]))

    
#run functions below

#ex29()
#ex30()
#ex31()
#ex32()
#ex33()
#ex35()
ex38()