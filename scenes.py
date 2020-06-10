from sys import exit
from random import randint
from textwrap import dedent


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        pass

class Scene(object):

    def __init__(self):
        self.attempt = 1

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

    def try_again(self):
        print("\nWould you like to try again?")
        answer = input("> ")
        selection = answer.lower()

        if selection == "yes":
            #this part of function should include a call to start the game over
            pass
        elif selection == "no":
            print("\nThank you for playing!")
            exit(1)
        else:
            print("\nPlease enter yes or no.")
            self.try_again()

class Kitchen(Scene):
    
    def enter(self):

        print("""\nIt's midnight and you have walked into your kitchen with the goal of obtaining a midnight snack. 
            \nYou go to the fridge and open the door. 
            \nYou blink once. 
            \nTwice. 
            \nThere is no food in your fridge. Instead, it looks as though you have opened a doorway looking into a small garden in the middle of a forest of towering maple trees. There is sunlight and warm air coming in through the door and you can see a stone path leading a few feet away into the center of the garden where there is an iron bench.
            """)
        print("""*****
            \nYou can either:
            \nClose the fridge, assuming that you're just going a little crazy because you're so tired. 
            \nOR
            \nWalk into the garden.
            \nWhat do you do?
            """)
        choice = input("> ")
        
        if ("walk" in choice) or ("garden" in choice):
            print("\nYou approach the bench and notice a piece of parchment laying on it.")
            print("\nWould you like to read the parchment?")
            choice = input("> ")
            #add a return statement that changes the current_scene to the next scene.

        elif ("close" in choice) or ("fridge" in choice):
            print("\nYou close the fridge and decide to go back to bed without a midnight snack.")
            print("\nThere will be no adventure for you today.")
            self.try_again()
        
        else:
            print("\nPlease enter an available choice.")
            self.enter()

class Garden(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Forest(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Well(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Cabin(Scene):

    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Shed(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Bridge(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Cave(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Beach(Scene):
    
    def enter(self):
        print("""
            \nScene context will go here.
            """)
        choice = input("> ")

        if "choice option" in choice:
            print("\nConsequence goes here.")
            #return statement moving game forward

        elif "losing choice option" in choices:
            print("/nConsequence goes here.")
            print("Losing statement goes here.")
            self.try_again()

        else:
            print("Please enter an available choice.")
            self.enter()

class Final(Scene):
    
    def enter(self):
        print("""\nYou poke the boulder and notice that it is much warmer than a rock formation on this cool beach should be. Nothing happens at first. After a moment, though, the boulder seems to shiver a bit. You poke it again, curiosity too much for you to resist. The boulder begins to expand... No. It is unravelling, revealing a small, black dragon. The wingspan is roughly twice your height. The dragon looks around for a moment, clearly looking for the source of the poking before it's eyes latch on to you. They narrow as the dragon begins to snarl, and you pull the sword from the sheath on your hip, preparing for battle.

            \nThe Mage appears suddenly between you and the dragon, grinning maniacally. "Hello adventurer! It seems you have found my precious Edrys. What's that? I didn't tell you she was a dragon? Oh well. How terribly remiss of me." The dragon is nuzzling the Mage's hand now. "Thank you so much for your help with this quest! It seems your journey has come to an end and you have been victorious! Would you like me to send you home now?"
        """)

class Finished(Scene):

    def enter(self):
        print("FILL THIS IN WITH SOMETHING AT SOME POINT")

class Map(object):
    
    scenes = {'garden': Garden(),
            'forest' : Forest(),
            'well' : Well(),
            'cabin' : Cabin(),
            'shed' : Shed(),
            'bridge' : Bridge(),
            'cave' : Cave(),
            'beach' : Beach(),
            'finished' : Finished()
    }

    def __init__(self, starting_scene):
        self.starting_scene = starting_scene

    def next_scene(self):
        pass

    def opening_scene(self):
        pass