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
        answer = input("\n> ")
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
        answer = input("\n> ")
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
        answer = input("\n> ")
        choice = answer.lower()

        if ("path" in choice) or ("forest" in choice):
            return 'forest'
        
        elif ("item" in choice) or ("tree" in choice) or ("examine" in choice):
            print("""\nAs you approach the path into the forest, you see that the item leaning against the tree is a sword with a blade the length of your arm. It is sheithed in dark brown leather and has a strap to go across your back.
                \nDo you take the sword?
                """)
            answer = input("\n> ")
            choice = answer.lower()
            if choice == "yes":
                inventory.append("sword")
                print("\nYou strap the sword to your back and follow the path into the forest.")
                return 'forest'
            else:
                print("\nLeaving the sword where it is, you walk into the forest.")
            return 'forest'
        
        else:
            print("\nPlease enter an available choice.")
            self.enter()

class Forest(Scene):
    
    def enter(self):
        print("""
            \nThe trees grow thicker around you as you walk deeper into the forest. Less and less sunlight is filtering through until you find yourself in semi darkness. The path is dirt with mushrooms of all shapes and colors popping up at the base of trees along the edges. There is sound of wildlife around you: leaves rustling as animals move through the trees, birds chirping.
            \nFor a moment everything grows louder as the sound of hundreds of birds taking flight at once echoes through the trees. Then the forest goes quiet. You look around, but it is hard to see any details off of the path with the trees as thick as they are. The path turns up ahead and there is no end to the forest in sight. 
            """)
        input("\n[enter]")
        print("""
            \nThere is a frantic rustling of leaves to your left and movement in the trees in front of you.
            \nYou hear deep and heavy panting ahead of you as a large grey wolf with black ears and paws stalks toward you.
            \nThe wolf stops a few yards from you and widens his stance, ready to strike.
            \nDo you:
            \nAttack the wolf with your sword
            \nLunge at the wolf and attempt to wrestle him to the ground
            \nWalk slowly toward the wolf, hand in front of you to suggest you mean it no harm
            \nTurn and run back to the garden
            """)
        answer = input("\n> ")
        choice = answer.lower()

        if ("hand" in choice) or ("walk" in choice) or ("no harm" in choice):
            print("""\nYou raise your hand, palm up, in front of you as you walk toward the wolf, each step slow and careful.
                \nThe wolf watches wearily. Gowing curious as you get closer, stance losening, head cocked to the side.
                \nYou stop a few feet away, allowing the wolf to come to you.
                \nThe wolf takes two cautious steps and leans his snout forward and down toward your hand, sniffing. After a moment the wolf nudges the back of your hand with his snout and licks your fingers once.
                \nYou raise your hand to the top of the wolf's head and scratch between his ears. The wolf chuffs and leans into your hand.
                \nAfter a few moments spent petting the wolf you decide that it is time to move on. You pat his head once and move to walk passed him and continue down the path, but the wolf nips at the sheath on your back to grab your attention.
                \nThe wolf cocks his head again as you turn back toward him and you're not sure why, but his intention is clear. The wolf wants to know if he can come with you.
                \nDo you allow the wolf to join you on your journey?
                """)
            answer = input("\n> ")
            choice = answer.lower()

            if choice == "yes":
                inventory.append("wolf")
            return 'well'

        elif ("attack" in choice) or ("sword" in choice):
            
            if "sword" not in inventory:
                print("\nYou do not have a sword to attack the wolf with.")
                self.enter()
            else:
                print("\nYou pull the sword from the sheath at your back swinging it as you move toward the wolf. The wolf snarls and leaps toward you, knocking the sword out of your hands as you fall to the ground. You hit your head hard against the ground and all you know before you lose conciousness is the weight of the wolf on your chest and a large mouth full of teeth coming toward you.")
                input("\n[enter]")
                print("\nYou are gasping for breath as you sit up from your bed, hands coming to your neck. It must have been a nightmare, that wolf towering over you. You are drenched in sweat and you decide some food might be in order before you go back to bed. As you head toward the kitchen, you notice with some confusion that there seems to be a rather large bump on the back of your head.")
                input("\n[enter]")
                print("\nYou lost. Thank you for playing and better luck next time!")
                exit(1)

        elif ("lunge" in choice) or ("wrestle" in choice):
            print("""
                \nYou lunge toward the wolf, planning to wrestle him to the ground so that you can escape.
                \nIt's a stupid plan, really. The wolf is huge and easily overtakes you. Your hands skitter across the ground looking for anything to use as a weapon, you feel something cut through the skin of your right palm. He is standing over you, front paws against your chest, mouth open in a snarl as he lowers his face toward yours.
                \nDarkness creeps into your vision and everything is silent...
                """)
            input("\n[enter]")
            print("""
                \nThere is a pain in your hand as you wake up. You squint at it in the darkness of your bedroom, unsure where it came from. There is a small cut surrounded by dried blood on your palm. Vaguely, you remember the nightmare that has woken you. Something about a wolf standing over you, teeth bared. You get out of bed and head toward the kitchen, thinking that maybe a late night snack will help you go back to sleep.
                """)
            input("\n[enter]")
            print("\nYou lost. Thank you for playing and better luck next time!")
            exit(1)

        elif ("run" in choice) or ("garden" in choice):
            pass

        else:
            print("Please pick an appropriate option.")
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