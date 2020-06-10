from sys import exit
from random import randint
from textwrap import dedent


inventory = []

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
        choice = answer.lower()

        if choice == "yes":
            #this part of function should include a call to start the game over
            pass
        elif choice == "no":
            print("\nThank you for playing!")
            exit(1)
        else:
            print("\nPlease enter yes or no.")
            self.try_again()

class Kitchen(Scene):
    
    def enter(self):
        print("\nWelcome to Journey of Edrys!")
        print("\nPress Enter to begin.")
        input()

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
        answer = input("> ")
        choice = answer.lower()

        if ("walk" in choice) or ("garden" in choice):
            return 'garden'

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
            \nYou step through the fridge and into the garden. The air is warm and sunlight is coming in through the trees. The rock path leading to the garden is uneven and you walk carefully, not knowing if this fridge-world is a halucination or a dream.
            \nWhen you reach the black iron bench you notice a piece of parchment sitting there with a curling scrawl written across it.
            """)
        print("\nWould you like to read the parchment?")
        answer = input("> ")
        choice = answer.lower()

        if choice == "yes":
            pass
        
        elif choice == "no":
            print("\nYou should probably just read the parchment. There's nothing else to do here.")
            input("\n[enter]")

        else:
            print("\nJust read the parchment, we don't have all day.")
            input("\n[enter]")
        
        print("""\nYou pick up the parchment and read:
            \nWelcome to the forest of Wyverly Adventurer!
            \nI am the Mage of this forest. I have brought you here because I need your help!
            \nA dear friend of mine has gone missing and I need your help to find her. Edrys is prone to wander off, but she has never been gone longer than an hour or two without word before. I am worried something terrible has happened to her.
            \nFollow the path to the west that leads through the forest. I will talk to you there.
            \nSigned,
            \nThe Mage of Wyverly
            """)
        print("""
            \nLooking around the garden again, you notice the path to the west that The Mage mentioned in the note. There is something leaning against one of the trees to the side of the path.
            \nWould you like to take the path into the forest? Or examine the item against the tree?
            """)
        answer = input("> ")
        choice = answer.lower()

        if ("path" in choice) or ("forest" in choice):
            return 'forest'
        
        elif ("item" in choice) or ("tree" in choice):
            print("""\nAs you approach the path into the forest, you see that the item leaning against the tree is a sword with a blade the length of your arm. It is sheithed in dark brown leather and has a strap to go across your back.
                \nDo you take the sword?
                """)
            answer = input("> ")
            choice = answer.lower()
            if choice == "yes":
                inventory.append("sword")
                print(inventory)
                print("You strap the sword to your back and follow the path into the forest.")
            else:
                print("Leaving the sword where it is, you walk into the forest.")
            return 'forest'
        
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

        elif "losing choice option" in choice:
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

        elif "losing choice option" in choice:
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

        elif "losing choice option" in choice:
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

        elif "losing choice option" in choice:
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

        elif "losing choice option" in choice:
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

        elif "losing choice option" in choice:
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

        elif "losing choice option" in choice:
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
    
    scenes = {'kitchen' : Kitchen(),
            'garden' : Garden(),
            'forest' : Forest(),
            'well' : Well(),
            'cabin' : Cabin(),
            'shed' : Shed(),
            'bridge' : Bridge(),
            'cave' : Cave(),
            'beach' : Beach(),
            'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.inventory = []

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)