#exercise 39 Dictionaries
'''
   intro to dict 
'''
def ex39():
    states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'Oregon': 'OR',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
    }

    cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
    }

    #add cities

    cities['NY'] = 'New York'
    cities['OR'] = 'Portland'

    print('-' * 10)
    print("NY State has: ", cities['NY'])
    print("OR State has: ", cities['OR'])

    print('-' * 10)
    print("Michigan's abreviation is: ", states['Michigan'])
    print("Florid's abreviation is: ", states['Florida'])

    print('-' * 10)
    print("Michigan has: ", cities[states['Michigan']])
    print("Florid's has: ", cities[states['Florida']])

    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"{state} is abbreviated {abbrev}")

    print('-' * 10)
    for state, abbrev in list(states.items()):
        print(f"{state} is abbreviated {abbrev}")
        print(f"and has city {cities[abbrev]}")

    print('-' * 10)
    #safely get a valie that might not be there
    state = states.get("Texas")

    if not state:
        print("Sorry, no Texas")
    
    #get with a default value
    city = cities.get('TX', "Does not exist")
    print(f"The city for the state of TX is: ", city)

#exercise 40 Modules, Classes, and Objects
'''
   uses mystuff.py to show modules 
'''
import mystuff

 #can create a class 
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

def ex40a():
    #getting things from things
    #dict style
    mydict = {'apple': "I AM APPLES!"}#i needed to change the name
    print(mydict['apple'])

    #module style
    mystuff.apple() #use a function that was imported 
    print(mystuff.tangerine) #use the variable
    
    #class style
    thing = MyStuff() #initiate 
    thing.apple()
    print(thing.tangerine)
   

def ex40():
    
    class Song(object):
        def __init__(self, lyrics):
            self.lyrics = lyrics

        def sing_me_a_song(self):
            for line in self.lyrics:
                print(line)
        
        #added a few other things...
        def first_line(self):
            print(self.lyrics[0])
        
        def last_line(self):
            print(self.lyrics[-1])

    happy_bday = Song(["Happy birthday to you",
                        "I don't want to get sued",
                        "So I'll stop it right there!"])

    bulls_on_parade = Song(["They rally round the family",
                            "With pockets full of shells"])

    happy_bday.sing_me_a_song()

    bulls_on_parade.sing_me_a_song()

    bulls_on_parade.first_line()

    happy_bday.last_line()

#exercise 41 Classes
'''
   asked to read code and memorize language used in OOP
'''

#exercise 42 Is-A, Has-A, Objects and Classes
'''
  
'''
#Animal is-a object (base class)
class Animal(object):
    pass

#dog is-a animal (inherits from animal)
class Dog(Animal):
    def __init__(self, name):
        self.name = name

#cat is-a animal (inherits from animal)
class Cat(Animal):
    def __init__(self, name):
        self.name = name

#person is-a class
class Person(object):
    def __init__(self, name):
        self.name = name
        #person is-a class and has-a pet
        self.pet = None #default is none later assign

#employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        #inherits the name from person
        super(Employee, self).__init__(name)
        #has-a salary
        self.salary = salary
#base class
class Fish(object):
    pass
#salmon is-a fish
class Salmon(Fish):
    pass
#halibut is-a fish
class Halibut(Fish):
    pass

def ex42():
    #delta is-a dog is-a animal
    delta = Dog("Delta")
    #mylo is-a cat is-a animal
    mylo = Cat("Mylo")
    #curtis is-a person
    curtis = Person("Curtis")
    #has-a pet which is-a cat which is-a animal
    curtis.pet = mylo
    #taylor is-a employee which is-a person
    taylor = Employee("Taylor", 120000)
    #has-a pet which is-a dog which is-a animal
    taylor.pet = delta
    #flipper is-a fish
    flipper = Fish()
    #is-a salmon which is-a fish
    crouse = Salmon()
    #harry is-a halibut which is-a fish
    harry = Halibut()
    

#run functions below

#ex39()
#ex40a()
#ex40()
ex42()
