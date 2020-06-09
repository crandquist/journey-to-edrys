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
        self.name = "I am a scene."

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Kitchen(Scene):
    
    def enter(self):
        print("""It's midnight and you've walked into your kitchen with the goal of obtaining a midnight snack. 
            \nYou go to the fridge and open the door. 
            \nYou blink once. 
            \nTwice. 
            \nThere is no food in your fridge. Instead, it looks as though you have opened a doorway looking into a small garden in the middle of a forest of towering maple trees. There is sunlight and warm air coming in through the door and you can see a stone path leading a few feet away into the center of the garden where there is an iron bench.
            """)
        print

class Garden(Scene):
    
    def enter(self):
        pass

class Forest(Scene):
    
    def enter(self):
        pass

class Well(Scene):
    
    def enter(self):
        pass

class Cabin(Scene):

    def enter(self):
        pass

class Shed(Scene):
    
    def enter(self):
        pass

class Bridge(Scene):
    
    def enter(self):
        pass

class Cave(Scene):
    
    def enter(self):
        pass

class Beach(Scene):
    
    def enter(self):
        pass

class Final(Scene):
    
    def enter(self):
        print("""
            You poke the boulder and notice that it is much warmer than a rock formation on this cool beach should be. Nothing happens at first. After a moment, though, the boulder seemns to shiver a bit. You poke it again, curiosity too much for you to resist. The boulder begins to expand... No. It is unravelling, revealing a small, black dragon. The wingspan is roughly twice your height. The dragon looks around for a moment, clearly looking for the source of the poking before it's eyes latch on to you. They narrow as the dragon begins to snarl, and you pull the sword from the shieth on your hip, prepared for battle...

            The Mage appears suddenly between you and the dragon, grinning maniacally. "Hello adventurer! It seems you have found my precious Edrys. What's that? I didn't tell you she was a dragon? Oh well. How terribly remiss of me." The dragon is nuzzling the Mage's hand now. "Thank you so much for your help with this quest! It seems your journey has come to an end and you have been victorious. Would you like me to send you home now?"
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