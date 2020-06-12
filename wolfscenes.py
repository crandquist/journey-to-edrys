from scenes import Scene
from scenes import inventory

class Well(Scene):
    
    def enter(self):

        print("""
            \nYou continue through the forest. As you walk, the trees on either side of you become more sparse and light begins to filter through the leaves once more. The path seems never ending ahead of you, but you can see that the forest is coming to an end.
            \nWith the forest behind you, you keep walking, unsure of your destination. There is a cabin up ahead on the left with a large brick well in front. It is the only notable object in the surrounding area.
            \nYou walk over to the cabin. The door is locked. You knock, but there is no answer. You walk back over to the well and see that there is a raven perched on the edge. There is a structure built over the well with a rope wound around it that presumably has a bucket at the other end inside of the well. The well is too deep to see to the bottom of it, though.
            """)
        input("[enter]")
        print("""\nThere is a rock sitting on the ledge of the well with a familiar looking piece of parchment on it. You move the rock and pick up the parchment to read:
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
                \nYou climb up on to the edge of the well and turn to face the outside. The raven is staring at you with wide eyes. You begin to lower yourself into the well, grasping the side which is almost to thick to hold onto. Despite moving slowly and being extremely careful, your foot slips and you find yourself falling into the darkness. You can see the light at the opening of the well growing smaller and smaller.
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
    def enter(self):
        print("""
            \nYou pick up the key and walk back over to the cabin. You unlock the door and push it open, looking around before you step inside. It's a small cabin with only one room. Along one wall is a bed barely big enough for a single adult. The far wall has a fireplace with a cooking pot hanging over what you suspect are warm coals and a door in one corner that must lead to the back of the cabin. There is a round table with two chairs that is cluttered with dishes, parchment, and other items. Some of the items on the table are recognizable, but others are strange. There is a jar filled with a clear liquid and what looks to be organs from several small animals. There are herbs and twigs scattered across the table as well.
            \nYou turn to look closer around the room. The Mage had said that there would be new information about Edrys here, but nothing seems to stand out as something you are supposed to be looking at.
            \nThe parchment scattered across the table is blank. There is a quill and ink pot there as well. Likely used to write the notes you have found already. There is a small side table next to the bed with a leatherbound book on it. You pick up the book and open it to the first page. It appears to be a journal, written in The Mage's handwriting.
            \nDo you read the journal?
            """)
        answer = input("> ")
        choice = answer.lower()

        if choice == "yes":
            print("""
                \nHarvest 30, 325
                \nI met the most delightful creature today, followed me out of the forest. I didn't even realize anyone was behind me until I hit the edge of the wards around the cabin. She is graceful and fierce. She thought me an intruder in the forest and followed me to ensure that I stayed away in the future.
                \nIt was a minor misunderstanding and I was able to explain to her that I am here to protect the forest and all of its inhabitants. She was willing to listen and allowed me close enough to her to see that she had an injury on her right leg. 
                \nI healed the injury for her as a show of good faith and she stayed in the cabin with me while I prepared dinner. She left not too long after.
                \nHopefully this will not be the last I see of her. I only now realized that I didn't get her name.
                """)
            input("[enter]")
            print("""
                \nHarvest 39, 325
                \nMy friend from the forest followed me home again today. She found me as I was finishing up the process of getting rid of a group of poachers who had been hunting the cestrals on the East side.
                \nI appologized to her for my bad manners the other day and asked for her name. She let me know that I could call her Edrys. What a lovely name.
                """)
            input("[enter]")
            print("""\nThere are many entries along these same lines mentioning Edrys through the first two thirds of the journal. You flip through them but do not     spend the time to read them in their entirety. You stop toward the end of the journal on a longer entry.
                \n
                \nGrowth 3, 326
                \nEdrys has been living in the cabin with me for a few weeks now. We have settled into a routine. She helps me gather food and herbs and other potions ingredients in the morning and accompanies me on my patrols of the forest.
                \nI had been worried that she would not be able to cope with the destruction of her home in the forest. I was even more worried that she would resent me for not being quick enough to save it. I admit, I had been too focused on worrying about her unnecessarily instead of working with her as a team like we do now. She has certainly scolded me in the past weeks for not seeing that she is more than capable of protecting herself, maybe even moreso than anything I could do to protect her.
                \nI have told her that she can have the shed in the back to herself, but she refuses to use it. She let me know that she prefers to be in the cabin with me. She likes the smells and the warmth and the company.
                \nShe likes to wander in the evenings. While I do my reading and correspondence she has been exploring parts of the valley that she had never known existed while she was living in the forest. She's never gone long. I think she is growing as fond of me as I am of her.
                \nI am shocked to find how much brighter my life is with Edrys. I have never begrudged the solitary job of watching over the forest. I love the creatures under my protection and find pride in the work I do.
                \nStill.
                \nIt is so nice not to be alone.
                """)
            input('[enter]')
            print("""\nYou put the journal back on the table and look around the room, checking for anything else that may help you find Edrys.
                \nThere is a small pile of gold coins on the table that you hadn't been there before, but otherwise there is nothing of note.
                \nDo you take the coins?
                """)
            answer = input("> ")
            choice = answer.lower()

            if choice == "yes":
                inventory.append("gold coins")
                print("\nYou take the coins and put them in the pocket of your pajamas. These may be useful later, and if not they can be payment for this ridiculous quest.")
            else:
                print("You decide not to take the coins.")

            print("""\nYou go to the back door to the cabin and open it to reveal a small cleared area similar to the front of the cabin. To the right you can see the path that brought you here. Ahead is a shed, smaller than the cabin.
            \nDo you enter the shed?
            """)
            answer = input("> ")
            choice = answer.lower()

            if choice == "yes":
                return 'shed'

            elif choice == "no":
                print("""
                    \nYou decide to ignore the shed and head back to the path. 
                    \nWalking further away from the forest on the path, you reach a fork.
                    \nDo you go right or left?
                    """)
                answer = input("> ")
                choice = answer.lower()

                if choice == "right":
                    return 'bridge'
                
                elif choice == "left":
                    print("""\nYou take the left fork and find yourself walking away from the lush green lands that you had seen before. The foliage becomes more and more sparse as you go and the air becomes warmer with every step.
                        \nAfter an hour of walking you find yourself in a vast desert. You keep walking and walking, losing track of time. The edges of your vision begin to blur and eventually everything goes dark.
                        """)
                    input("[enter]")
                    print("""\nYou are sweating profusely when you come awake in your bed, exhausted. Your mouth is dry and your tongue is swollen. You head to the kitchen for a glass of water and maybe some ice cream to cool you down before you try to sleep again.
                        """)
                    input("[enter]")
                    print("You lost. Thank you for playing! Better luck next time!")
                    exit(1)
                
                else:
                    print("Please pick an available choice.")
                    self.enter()
            
            else:
                    print("Please pick an available choice.")
                    self.enter()


class Shed(Scene):
    def enter(self):
        print("""\nYou walk over to the shed and pull on the door handle. It sticks, but after a few tugs you are able to pull the door open. The shed is sparse, with only a table along the wall on the left with three wooden boxes the size of a loaf of bread.
            \nThe boxes all have identical, hinged lids and are set out across the table in a line.
            \nDo you open the box on the left, in the middle, or on the right?
            """)
        answer = input("> ")
        choice = answer.lower()

        if choice == "middle":
            print("""\nYou lift the lid on the box to reveal a scroll of parchment tied with a leather cord. You untie the cord and unroll the parchment to discover a map. 
                \nAcross the top of the map The Mage has written "Adventure Awaits, Edrys". The map is of a valley, with mountains marked on all sides. At the bottom of the map is the forest with the garden and the path through it clearly visible. You are able to locate the cabin and the shed. 
                \nThere is a fork further up the path. To the left is a seemingly barren land labled "Desert of Ashes". To the right is a bridge that leads across a wide river toward the mountains on the right side of the valley.
                \nYou roll the map back up and leave the shed, heading back to the path that led you out of the forest.
                \nYou consult the map again when you get to the fork in the path.
                \nDo you go left or right?
                """)
            answer = input("> ")
            choice = answer.lower()

            if choice == "right":
                return 'bridge'
            
            elif choice == "left":
                print("""\nYou take the left fork and find yourself walking away from the lush green lands that you had seen before. The foliage becomes more and more sparse as you go and the air becomes warmer with every step.
                    \nAfter an hour of walking you find yourself in a vast desert. You keep walking and walking, losing track of time. The edges of your vision begin to blur and eventually everything goes dark.
                    """)
                input("[enter]")
                print("""\nYou are sweating profusely when you come awake in your bed, exhausted. Your mouth is dry and your tongue is swollen. You head to the kitchen for a glass of water and maybe some ice cream to cool you down before you try to sleep again.
                    """)
                input("[enter]")
                print("You lost. Thank you for playing! Better 9luck next time!")
                exit(1)

            else:
                print("Please enter an available choice.")
                self.enter()

        elif choice == "left":
            print("\nYou lift the lid of the box on the left. You look back at him and startle as you feel something creeping up your arm. You jerk your hand away from the box on instinct and look back to find a spider the size of a grapefruit sinking its fangs into your wrist. There is blinding pain from the bite. You shake your arm again and the spider drops to the floor, skittering quickly out of sigh. You stumble over to him as the spider's venom burns in your veins and your head starts to swim. You fall to your knees next to the door, leaning against it as your vision goes black.")
            input("[enter]")
            print("\nThe veins in your arm are on fire  as you wake up in your bed. You remember dreaming about a large spider biting your arm and assume the pain must be from that. Thinking that a snack might help you get back to sleep, you get out of bed and head to the kitchen.")
            input("[enter]")
            print("\nYou lost. Thanks for playing! Better luck next time.")
            exit(1)

        elif choice == "right":
            print("""\nYou lift the lid of the box on the right slowly, prepared for anything. The box is full of mushrooms of all shapes and colors, some unfamiliar, others look like the onces you saw in the forest. They seem harmless, and maybe if they're edible you could finally get that snack that you went to the fridge for in the first place.
                \nYou pick up the box and turn to leave the shed. You stub your toe on the table leg in the process and fall to the ground, letting go of the box to catch your fall.
                \nThe box tumbles in the air and mushrooms fall to the floor. A few of the bigger, purple mushrooms release spores that form in a cloud around you. The smell is sickeningly sweet. The room starts to spin. You hold your breath and try to stand to leave the shed but your legs won't move. You're feeling suddenly drowsy and you yawn. You turn over to your side, thinking that a bit of a nap will help and then you can get up and move on with The Mage's so called "quest."
                """)
            input("[enter]")
            print("\nThere is a sickly sweet smell in your room when you wake up. You yawn and think about going back to sleep, but you are so hungry. You head to the kitchen to get something to eat. Anything but mushrooms.")
            input("[enter]")
            print("\nYou lost. Thank you for playing! Better luck next time!")
            exit(1)

        else:
            print("Please enter an available choice.")
            self.enter()


class Bridge(Scene):
    pass


class Cave(Scene):
    pass