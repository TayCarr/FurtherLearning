from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map): 
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):
    quips = [
        'You died. You suck at this',
        'You and your mom stank.',
        'Ew...',
        'My dog is better at this...',
        'Anyways...',
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
                The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving
                member and your last mission is to get the neutron destruct bomb from the Weapons armory, put it in the bridge,
                and blow the ship up after getting into an escape pod.

                You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy
                teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the armory and about
                to pull a weapon to blast you. 
        """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                    Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing and moving
                    around his body, which throws off your aim. Your laser hits his costume but misses him entirely. This ruins his 
                    brand new silk costume his mother bought him! This sends him into a rampage, he throws his Gothon blaster at 
                    your head. The impact makes your head explode, he then eats the rest of your body.

            """))
            return 'death'
        elif action == 'dodge':
            print(dedent("""
                    Like a world class dodgeballer you are dodge ducking and weaving, the Gothon's blaster is flying past you unable 
                    to hit its mark. But you slip on an oil slick hit your head on the metal floor and pass out gaining concious long 
                    enough to see you are being eaten.
            """))
            return 'death'
        elif action == 'joke around':
            print(dedent("""
                    You think back to your emergency training in the academy and repeat the Gothon insults you learnt. You tell a joke
                    and the Gothon cracks up. While he is laughing you walk up and shoot him in the face allowing you to walk 
                    through the Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        elif action == ' ':
            print(dedent("""
                    You stare at the Gothon blankly as he prepares to blast you... but a steel beam falls on the Gothon crushing him, 
                    this makes the beam from his blaster shoot off in another direction. It happens to hit a critical fuse box and 
                    starts an explosion, you take this chance to run directly to the escape pod remembering the engineer told you 
                    earlier that only the third pod was in working condition while the others underwent maintenance. You safely 
                    escape and the ship blows up killing the space invaders.
            """))
            return 'finished'
        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                You dive roll into the armory, crouch and scan the room for more enemies. It is quiet... too quiet. You decide 
                to take your chances and run to the far side of the room to find the neutron bomb. There is a keypad on the 
                bomb's container, if you get the three digit code wrong 3 times the lock closes forever.
        """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 1
        #print(f"test: {code}")

        while guess != code and guesses < 3:
            print("BZZZZED")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                    The container clicks open and you grab the bomb running as fast as you can to the bridge where you must 
                    place it in the right spot. 

            """))
            return 'the_bridge'
        else:
            print(dedent("""
                    The lock buzzes one last time before you hear a series of clicks and the lock fuses to itself. A squad of 
                    Gothon's burst into the room and drag you away as you scream and cry for help.
            """))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
                You burst onto the Bridge with the neutron destruct bomb tucked under your arm and surprise 5 Gothon's who are 
                trying to take control of the ship. Each of them adorning an uglier clown costume than the last. They haven't 
                pulled out their weapons yet, as they see you are carrying the bomb and don't want to risk setting it off.
        """))

        action = input("> ")

        if action == "throw bomb":
            print(dedent("""
                    Without thinking you instinctively throw the bomb at the group and make a leap for the door, as soon as you
                    turn one a Gothon shoots you in the back paralyzing you, just as you slam on the ground the bomb goes off 
                    and turns the ship and everyone on it to dust. 

            """))
            return 'death'
        elif action == 'slowly place the bomb':
            print(dedent("""
                    Already starting the timer you point your blaster at it slowly backing towards the door, as you enter it you 
                    roll the bomb to the other side of the room causing the Gothons to rush to it as you take this chance to head 
                    towards the escape pods.
            """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                You rush through the halls desperate to make it off the ship before the bomb goes off. Luckily you do not encounter 
                any Gothons along the way. Once at the chamber you recall the ships engineer warning you of upcoming pod maintenance 
                for four of the five pods but you were focused on cleaning your blaster and shooed him away... what pod number did 
                he say was cleared... Time is running out you'll just have to guess...
        """))
        good_pod = randint(1,5)
        #print(f"test: {good_pod}")
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                    You jump into pod {guess} and hit the eject button. The pod releases into the void of space but the engines never 
                    activate and you slowly drift off until you die a horrible lonely death. 

            """))
            return 'death'
        else:
            print(dedent("""
                    You jump into pod {guess} and hit the eject button. The pod slides out into space and the control panel lights up 
                    before the engine roars to life. As it heads toward the planet you look back at your ship and see it implode then 
                    explode like a bright star, taking out the Gothon and their ship at the same time. 
            """))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won!")
        return 'finished'
            

class Map(object):
    scenes = {
        'laser_weapon_armory' : LaserWeaponArmory(),
        'central_corridor' : CentralCorridor(),
        'escape_pod' : EscapePod(),
        'the_bridge' : TheBridge(),
        'death' : Death(),
        'finished' : Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
print("Starting game...")
a_game.play()