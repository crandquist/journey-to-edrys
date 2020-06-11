from scenes import Scene
from scenes import inventory

class Well(Scene):
    
    def enter(self):

        print("""
            \nYou continue through the forest with the wolf walking beside you. As you walk, the trees on either side of you become more sparse and light begins to filter through the leaves once more. The path seems never ending ahead of you, but you can see that the forest is coming to an end.
            \nWith the forest behind you, you keep walking, unsure of your destination. There is a cabin up ahead on the left with a large brick well in front. It is the only notable object in the surrounding area.
            \nYou walk over to the cabin. The door is locked. You knock, but there is no answer. You walk back over to the well and see that there is a raven perched on the edge. There is a structure built over the well with a rope wound around it that presumably has a bucket at the other end inside of the well. The well is too deep to see to the bottom of it, though.
            \nThere is a rock sitting on the ledge of the well with a familiar looking piece of parchment on it. You move the rock and pick up the parchment to read:
            \nHello again Adventurer!
            \nIt seems you have made it through the forest of Wyverly! I hope it didn't cause you too much trouble and that you found the sword that I left for you in the garden! 
            \nThe cabin you see before you belongs to me. The door is locked, but the spare key is located in the bucket in the well. Pull up the bucket and get the key and then head into the cabin. I have left more information about Edrys and her potential whereabouts inside.
            \nThank you for your help, brave Adventurer!
            \nThe Mage of Wyverly Forest
            \n
            \nOn one side of the well is a crank that looks as though it should raise the bucket.
            \nDo you: 
            \nTry the crank?
            \nOR
            \nClimb into the well to get the key yourself?
            """)
        answer = input("\n> ")
        choice = answer.lower()

        if ("try" in choice) or ("crank" in choice):
            print("""
                \nYou attempt to pull on the crank to raise the bucket but it appears to be stuck. You look over at the raven who is tilting their head back and forth as they watch you.")
                \nThe raven squawks at you again before opening it's beak wide. You hear a man's voice coming from the Raven as though it were a speaker.
                \n"What is the healthiest kind of water?"
                """)
            answer = False
            while not answer:
                response = input("\n> ")
                response_lower = response.lower()

                if response_lower == "well water":
                    print("""
                        \nThe raven closes its mouth and rises into the air before swooping around you and down into the well. After a moment it returns with a key in its beak. The raven drops the key at your feet and flys away.
                        """)
                    return 'cabin'
        
        elif ("climb" in choice) or ("well" in choice):
            print("""
                \nYou climb up on to the edge of the well and turn to face the outside. The raven is staring at you with wide eyes. You begin to lower yourself into the well, grasping the side which is almost to thick to hold onto. Despite moving slowly and being extremely careful, your foot slips and you find yourself falling into the darkness. You can hear the wolf barking from above and you can see the light at the opening of the well growing smaller and smaller.
                \nThe air rushing passed you is cold. After about a minute of falling you see the bucket seeming to rise above you. That and the diminishing light are the only clues that you are falling and not that the world of blackness is simply rushing by. Eventually the light and the bucket are too far away for you to make out. You are surrounded by darkness and still falling...
                """)
            input("\n[enter]")
            print("\nYou bolt upright as you come awake in your bed. All you remember is falling through an unending darkness. That and the face of a bird looking at you like you're an idiot. You shake of the nightmare and decide to grab a snack out of the kitchen before going back to sleep.")
            input("\n[enter]")
            print("You lose. Thank you for playing! Make better choices next time.")
            exit(1)
        
        else:
            print("Please pick an available option.")
            self.enter()


class Cabin(Scene):
    pass


class Shed(Scene):
    pass


class Bridge(Scene):
    pass


class Cave(Scene):
    pass