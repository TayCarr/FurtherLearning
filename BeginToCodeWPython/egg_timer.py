'''Using the sleep function to make an egg timer program
    - select type of egg soft or hard
    - program warns when almost ready
    - a recipe can be viewed for egg types 

    - could make a site or a window that this displays in 
'''
import time

def soft_egg():
    print("Soft Boiled! The egg will need to boil for 7 minutes I will warn you at 30 seconds left to get ready to take it out!")
    start = input("Are you ready? ")
    while start != 'yes':
        start = input("Are you ready? ")
    print("Starting timer!")
    time.sleep(20) #for now 20 seconds cause im not waiting that long...
    print("30 seconds remaining! Get ready!")
    time.sleep(10)
    print("Your eggs are ready!")
    recipe = input("Would you like to see a recipe? ")
    if recipe == 'yes':
        print("Here is my recipe: ") #maybe fill later
    return

def hard_egg():
    print("Hard Boiled! The egg will need to boil for 10 minutes I will warn you at 30 seconds left to get ready to take it out!")
    start = input("Are you ready? ")
    while start != 'yes':
        start = input("Are you ready? ")
    print("Starting timer!")
    time.sleep(20) #for now 20 seconds cause im not waiting that long...
    print("30 seconds remaining! Get ready!")
    time.sleep(10)
    print("Your eggs are ready!")
    recipe = input("Would you like to see a recipe? ")
    if recipe == 'yes':
        print("I don't have one, I don't like hard boiled...")
    return

def main():
    type = input("Which type of egg would you like to make? 1. Soft Boiled or 2. Hard boiled: ")

    if type == '1':
        soft_egg()
    elif type == '2':
        hard_egg()
    else:
        print("There is no timer for that.")

    return

main()