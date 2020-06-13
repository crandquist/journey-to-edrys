inventory = []

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
            input("[enter]")

        else:
            print("\nJust read the parchment, we don't have all day.")
            input("[enter]")
        
        print("""\nYou pick up the parchment and read:
            \nWelcome to the forest of Wyverly, Adventurer!
            \nI am the Mage of this forest. I have brought you here because I need your help!
            \nA dear friend of mine has gone missing and I need your help to find her. Edrys is prone to wander off, but she has never been gone longer than an hour or two without word before. I am worried something terrible has happened to her.
            \nFollow the path to the west that leads through the forest. I will talk to you there.
            \nSigned,
            \nThe Mage of Wyverly Forest
            """)
        print("""
            \nLooking around the garden again, you notice the path to the west that The Mage mentioned in the note. There is something leaning against one of the trees to the side of the path.
            \nWould you like to take the path into the forest? Or examine the item against the tree?
            """)
        answer = input("> ")
        choice = answer.lower()

        if ("path" in choice) or ("forest" in choice):
            return 'forest'
        
        elif ("item" in choice) or ("tree" in choice) or ("examine" in choice):
            print("""\nAs you approach the path into the forest, you see that the item leaning against the tree is a sword with a blade the length of your arm. It is sheithed in dark brown leather and has a strap to go across your back.
                \nDo you take the sword?
                """)
            answer = input("> ")
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
        input("[enter]")
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
        answer = input("> ")
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
            answer = input("> ")
            choice = answer.lower()

            if choice == "yes":
                inventory.append("wolf")
                return 'well'

            return 'well'

        elif ("attack" in choice) or ("sword" in choice):
            
            if "sword" not in inventory:
                print("\nYou do not have a sword to attack the wolf with.")
                self.enter()
            else:
                print("\nYou pull the sword from the sheath at your back swinging it as you move toward the wolf. The wolf snarls and leaps toward you, knocking the sword out of your hands as you fall to the ground. You hit your head hard against the ground and all you know before you lose conciousness is the weight of the wolf on your chest and a large mouth full of teeth coming toward you.")
                input("[enter]")
                print("\nYou are gasping for breath as you sit up from your bed, hands coming to your neck. It must have been a nightmare, that wolf towering over you. You are drenched in sweat and you decide some food might be in order before you go back to bed. As you head toward the kitchen, you notice with some confusion that there seems to be a rather large bump on the back of your head.")
                input("[enter]")
                print("\nYou lost. Thank you for playing and better luck next time!")
                exit(1)

        elif ("lunge" in choice) or ("wrestle" in choice):
            print("""
                \nYou lunge toward the wolf, planning to wrestle him to the ground so that you can escape.
                \nIt's a stupid plan, really. The wolf is huge and easily overtakes you. Your hands skitter across the ground looking for anything to use as a weapon, you feel something cut through the skin of your right palm. He is standing over you, front paws against your chest, mouth open in a snarl as he lowers his face toward yours.
                \nDarkness creeps into your vision and everything is silent...
                """)
            input("[enter]")
            print("""
                \nThere is a pain in your hand as you wake up. You squint at it in the darkness of your bedroom, unsure where it came from. There is a small cut surrounded by dried blood on your palm. Vaguely, you remember the nightmare that has woken you. Something about a wolf standing over you, teeth bared. You get out of bed and head toward the kitchen, thinking that maybe a late night snack will help you go back to sleep.
                """)
            input("[enter]")
            print("\nYou lost. Thank you for playing and better luck next time!")
            exit(1)

        elif ("run" in choice) or ("garden" in choice):
            print("""
                \nYou turn and start running back the way you came. The garden isn't in sight but there is nowhere else to go. You don't know whether the wolf is following you as you run and you worry about tripping over a stray rock or tree root on the path.
                \nThere are leaves rustling in the forest to your right. Something clearly running alongside you. You tell yourself that it isn't the wolf. Something else must be running from the predator as well. Whatever it is, it's faster than you. You can hear it pulling ahead of you in the trees.
                \nThe wolf jumps out in front of you from the trees to your right. You stop mid-stride and turn to run the other direction but trip and fall as you do. Your hands break your fall and there is pain in your wrist. Broken or sprained, it doesn't seem to matter as there is suddenly a firey pain in your leg as the wolf bites down and begins to drag you into the trees.
                \nYou're screaming for help as the darkness creeps into your vision...
                """)
            input("[enter]")
            print("""
                \nYou wake up screaming, surging forward in bed with your hands behind you, you notice there is a pain in your wrist. 
                \nYou take a deep breath and decide to grab a snack out of the kitchen to clear your mind. Visions of a dark forest fill your head as you get out of bed.
                """)
            input("[enter]")
            print("\nYou lost. Thank you for playing and better luck next time!")
            exit(1)

        else:
            print("\nPlease pick an appropriate option.")
            self.enter()

class Well(Scene):
    
    def enter(self):

        print("""\nYou continue through the forest with the wolf walking beside you. As you walk, the trees on either side of you become more sparse and light begins to filter through the leaves once more. The path seems neverending ahead of you, but you can see that the forest is coming to an end.
            \nWith the forest behind you, you keep walking, unsure of your destination. There is a cabin up ahead on the left with a large brick well in front. It is the only noteable object in the surrounding area.
            \nYou and the wolf walk over to the cabin. The door is locked. You knock but there is no answer. You walk back over to the well and see that there is a raven perched on the edge. There is a structure built over the well with a rope wound around it that presumably has a bucket at the other end inside of the well. The well is too deep to see to the bottom of it, though.
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
        answer = input("> ")
        choice = answer.lower()

        if ("try" in choice) or ("crank" in choice):
            print("""
                \nYou attempt to pull on the crank to raise the bucket but it appears to be stuck. You look over at the raven who is tilting their head back and forth as they watch you.")
                \nThe raven squawks at you again before opening it's beak wide. You hear a man's voice coming from the Raven as though it were a speaker.
                \n"What is the healthiest kind of water?"
                """)
            answer = False
            while not answer:
                response = input("> ")
                response_lower = response.lower()

                if response_lower == "well water":
                    print("""
                        \nThe raven closes its mouth and rises into the air before swooping around you and down into the well. After a moment it returns with a key in its beak. The raven drops the key at your feet and flys away.
                        """)
                    print(inventory)
                    return 'cabin'
        
        elif ("climb" in choice) or ("well" in choice):
            print("""
                \nYou climb up on to the edge of the well and turn to face the outside. The wolf and the raven are staring at you with wide eyes. You begin to lower yourself into the well, grasping the side which is almost to thick to hold onto. Despite moving slowly and being extremely careful, your foot slips and you find yourself falling into the darkness. You can hear the wolf barking from above and you can see the light at the opening of the well growing smaller and smaller.
                \nThe air rushing passed you is cold. After about a minute of falling you see the bucket seeming to rise above you. That and the diminishing light are the only clues that you are falling and not that the world of blackness is simply rushing by. Eventually the light and the bucket are too far away for you to make out. You are surrounded by darkness and still falling...
                """)
            input("[enter]")
            print("\nYou bolt upright as you come awake in your bed. All you remember is falling through an unending darkness. That and the faces of a wolf and a bird looking at you like you're an idiot. You shake of the nightmare and decide to grab a snack out of the kitchen before going back to sleep.")
            input("\n[enter]")
            print("You lose. Thank you for playing! Make better choices next time.")
            exit(1)
        
        else:
            print("Please pick an available option.")
            self.enter()


class Cabin(Scene):

    def enter(self):
        print("""
            \nYou pick up the key and walk back over to the cabin, the wolf following behind you. You unlock the door and push it open, looking around before you step inside. It's a small cabin with only one room. Along one wall is a bed barely big enough for a single adult. The far wall has a fireplace with a cooking pot hanging over what you suspect are warm coals and a door in one corner that must lead to the back of the cabin. There is a round table with two chairs that is cluttered with dishes, parchment, and other items. Some of the items on the table are recognizable, but others are strange. There is a jar filled with a clear liquid and what looks to be organs from several small animals. There are herbs and twigs scattered across the table as well.
            \nThe wolf seems uneasy at your side. You look to him as you step into the cabin, but he makes no move to follow you. 
            \nYou shrug and turn to look closer around the room. The Mage had said that there would be new information about Edrys here, but nothing seems to stand out as something you are supposed to be looking at.
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
            print("""\nYou put the journal back on the table and look to the open front door to see that the wolf is still standing outside, sniffing the air and  looking weary. A silent exchange between you and the wolf has it coming inside slowly, turning and closing the door behind him.
                \nYou take another look around the room, checking for anything else that may help you find Edrys.
                \nThere is a small pile of gold coins on the table that you swear hadn't been there before, but otherwise there is nothing of note.
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
                    \nYou decide to ignore the shed and head back to the path. The wolf follows at your side.
                    \nWalking further away from the forest on the path, you reach a fork.
                    \nDo you go right or left?
                    """)
                answer = input("> ")
                choice = answer.lower()

                if choice == "right":
                    return 'bridge'
                
                elif choice == "left":
                    print("""\nYou take the left fork and find yourself walking away from the lush green lands that you had seen before. The foliage becomes more and more sparse as you go and the air becomes warmer with every step.
                        \nAfter an hour of walking you find yourself in a vast desert. The wolf is still at your side, panting with his tongue hanging out of his mouth in his ineffective attempt to keep cool. You keep walking and walking, losing track of time. The edges of your vision begin to blur and eventually everything goes dark.
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

        elif choice == "no":
            print("""\nThere is a small pile of gold coins on the table that you hadn't noticed there before, but otherwise there is nothing of note.
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
                    \nYou decide to ignore the shed and head back to the path. The wolf follows at your side.
                    \nWalking further away from the forest on the path, you reach a fork.
                    \nDo you go right or left?
                    """)
                answer = input("> ")
                choice = answer.lower()

                if choice == "right":
                    return 'bridge'
                
                elif choice == "left":
                    print("""\nYou take the left fork and find yourself walking away from the lush green lands that you had seen before. The foliage becomes more and more sparse as you go and the air becomes warmer with every step.
                        \nAfter an hour of walking you find yourself in a vast desert. The wolf is still at your side, panting with his tongue hanging out of his mouth in his ineffective attempt to keep cool. You keep walking and walking, losing track of time. The edges of your vision begin to blur and eventually everything goes dark.
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
                \nYou roll the map back up and look back at the wolf who is standing just inside the door. He cocks his head at you as you lead him out of the shed and back to the path.
                \nYou consult the map again when you get to the fork in the path.
                \nDo you go left or right?
                """)
            answer = input("> ")
            choice = answer.lower()

            if choice == "right":
                return 'bridge'
            
            elif choice == "left":
                print("""\nYou take the left fork and find yourself walking away from the lush green lands that you had seen before. The foliage becomes more and more sparse as you go and the air becomes warmer with every step.
                    \nAfter an hour of walking you find yourself in a vast desert. The wolf is still at your side, panting with his tongue hanging out of his mouth in his ineffective attempt to keep cool. You keep walking and walking, losing track of time. The edges of your vision begin to blur and eventually everything goes dark.
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
            print("\nThe wolf starts barking behind you as you lift the lid of the box on the left. You look back at him and startle as you feel something creeping up your arm. You jerk your hand away from the box on instinct and look back to find a spider the size of a grapefruit sinking its fangs into your wrist. There is blinding pain and the wolf behind you is whining. You shake your arm again and the spider drops to the floor, skittering quickly out of sigh. You stumble over to him as the spider's venom burns in your veins and your head starts to swim. You fall to your knees next to the wolf, leaning against him. You feel him licking your face as your vision goes black.")
            input("[enter]")
            print("\nThe veins in your arm are on fire and your face feels wet as you wake up in your bed. You remember dreaming about a large spider biting your arm and assume the pain must be from that. Thinking that a snack might help you get back to sleep, you get out of bed and head to the kitchen.")
            input("[enter]")
            print("\nYou lost. Thanks for playing! Better luck next time.")
            exit(1)

        elif choice == "right":
            print("""\nYou lift the lid of the box on the right slowly, prepared for anything. The box is full of mushrooms of all shapes and colors, some unfamiliar, others look like the onces you saw in the forest. They seem harmless, but maybe the wolf will know whether they are or not. If they're edible you might finally get that snack that you went to the fridge for in the first place.
                \nYou pick up the box and turn to carry it over to the wolf. You stub your toe on the table leg in the process and fall to the ground, letting go of the box to catch your fall.
                \nThe box tumbles in the air and mushrooms fall to the floor. A few of the bigger, purple mushrooms release spores that form in a cloud around you. The smell is sickeningly sweet. You hear the wolf sneeze from the doorway and the room starts to spin. You hold your breath and try to stand to leave the shed but your legs won't move. You're feeling suddenly drowsy and you yawn. You turn over to your side, thinking that a bit of a nap will help and then you can get up and move on with The Mage's so called "quest."
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
    
    def enter(self):
        print("""\nAfter walking for a little while, you and the wolf come to a large stone bridge crossing a wide river. Something about this bridge seems odd, but you can't tell if it's really that something is off or if you are just suspicious of this entire world at this point.
            \nDo you:
            \nTake the time to examine the area
            \nOR
            \nShake it off and cross the bridge
            """)
        answer = input("> ")
        choice = answer.lower()

        if ("time" in choice) or ("examine" in choice):
            print("""\nThe area on either side of the entrance to the bridge is covered in tall grasses that slope down toward the river. You walk into the grass, the wolf at your side, being sure to stay low and move as quietly as possible.
                \nThere is about six feet between the actual river and the base of the bridge. You see that there is what looks like a large troll sitting there under the bridge. There is a firepit here, the area just around it littered with small bones. The troll is leaning against the underside of the bridge, hands across her belly. Her eyes are closed and she is humming a tune that sounds almost like "Yankee Doodle." She seems nice enough.
                \nThe wolf barks softly to get the troll's attention. She opens her eyes slowly and smiles softly at the you and the wolf. "Well hello there, cuties. What brings you fine creatures to my bridge? It's very rare that I get visitors. Not that you aren't welcome, of course! What are your names?"
                """)
            name = input("> ")
            print("""\nThe wolf barks again after you tell the Troll your name. She continues to smile sweetly at you both.
                \n"Well it is so great to meet you, {name} and Mark. I would love to keep you here to chat, but I am sure that you are wanting to cross the bridge. So. On to business. Are you ready to pay the fee?"
                \nYou wonder what the fee could possibly be. All you know about bridge trolls is that they ask riddles and eat people.
                \nDo you:
                \nOffer to answer a riddle
                \nOR
                \nOffer the wolf as payment
                """.format(name = name))
            answer = input("> ")
            choice = answer.lower()

            if ("answer" in choice) or ("riddle" in choice):
                print("""\nThe troll laughs raucously. "Riddle. Where do you humans get these silly stereotypes? I don't even know any good riddles." She calms down after a moment and goes serious again. "No, no dear. There's a toll. After all, I am a bridge toll troll. Do you have the fee?"
                \nYou remember the coins from the cabin. Maybe The Mage had left them for you for this.
                """)
                if "gold coins" in inventory:
                    print("\nYou hand the coins over to the troll who beams that gracious smile at you once more before telling you and the wolf, Mark you remind yourself, to pass.")
                    return 'cave'
                else:
                    print("""\nWho would have guessed that you would live to regret not stealing money from someone? You tell the troll that you do not have the money to pay the toll and ask that she please let you cross anyway. You explain to her that you are on a quest for The Mage and that it is urgent.
                        \nnShe laughs again but it no longer sounds kind or welcoming. She turns to the wolf, "now tell me that a creature as gorgeous as you is not friends with this fool? I would hate to have to eat you both." The wolf whines softly at the troll. She sighs. "You know I can't do that. There are no exceptions to the rules. The human has erred greatly. I am able to spare you, however."
                        \nThe wolf barks and the troll reaches for something on her other side. 
                        \nThe troll pulls a large club from the ground beside her and before you even have time to think through what is about to happen, she clubs you over the head and everything goes dark.
                        """)
                    input("[enter]")
                    print("\nYou wake up in your bed with a raging headache after a nightmare about a bridge troll. Hoping it will help with your headache, you head to the kitchen for some water and a snack.")
                    input("[enter]")
                    print("\nYou lose. Thanks for playing! Remember not to anger the trolls in the future.")
                    exit(1)
            
            elif "wolf" in choice:
                print("""\nThe wolf barks in indignation and the troll's eyes widen. She glares furiously at you as she says "You really just offerred up your companion to me as payment? How self-serving and incredibly cruel of you! I think I will keep Mark here if you are so quick to get rid of him and he wants to stay. You, however, you we must get rid of.
                    \nThe wolf barks and the troll reaches for something on her other side. 
                    \nThe troll pulls a large club from the ground beside her and before you even have time to think through what is about to happen, she clubs you over the head and everything goes dark.
                    """)
                input("[enter]")
                print("\nYou wake up in your bed with a raging headache after a nightmare about a bridge troll. Hoping it will help with your headache, you head to the kitchen for some water and a snack.")
                input("[enter]")
                print("\nYou lose. Thanks for playing! Remember not to anger the trolls in the future.")
                exit(1)

        elif ("shake" in choice) or ("cross" in choice):
            print("""\n You assume that your bad feeling about the bridge is just because this whole place is so strange. You begin walking across the bridge and are a few yards across when you notice the wolf is not beside you. You look back at the wolf and put your hands up, wondering why he hasn't followed you. The wolf's eyes are wide and he barks quietly once and nods upward once to get you to turn around and look behind you.
                \nYou turn around to see a large troll standing behind you holding an equally large club. Without giving you a moment to defend yourself, the troll raises the club and brings it down on your head. There is a moment of intense pain before everything goes dark.
                """)
            input("[enter]")
            print("\nYou wake up in your bed with a raging headache after a nightmare about a bridge troll. Hoping it will help with your headache, you head to the kitchen for some water and a snack.")
            input("[enter]")
            print("\nYou lose. Thanks for playing! You might want to look for trolls the next time you try to cross a bridge.")
            exit(1)

        else:
            print("Please enter an available choice.")
            self.enter()

class Cave(Scene):
    
    def enter(self):
        print("""\nAfter crossing the bridge you continue to follow the path as it curves toward the mountains on the right side of the map, the wolf always at your side. There seems to be a cave marked at the end of the path. The path begins to slope as you reach the base of the mountain. There are pine trees all around you and it makes it hard to acurrately guage where you are. You are definitely not dressed for a hike and find yourself regretting ever walking into the garden in the first place, but according to the map, you should be coming up on the cave soon. The wolf seems amused by the effort this climb is taking you as he moves with ease.
            \nThe sun is on the other side of the mountain now and it's nearly too dark in this mountain forest to see where you're going, but finally you make out the outline of the cave. The glow of a fire comes from within the large entrance. You look to the wolf before heading into the cave to ensure that he is coming you. He huffs out a breath of confirmation and you walk into the cave together.
            """)
        input("[enter]")
        print("""The air around you grows warmer as you walk into the cave. The ceiling of the cave is high above you. The formation seems to be man made as there aren't any stalagtites or stalagmites around the cave. The air is somewhat damp.
            \nThe fire is near the back of the cave. There is no one else around, but against the back wall you see that there is a wooden hatch in the floor that has been left open.
            \nYou're looking for anything around the fire that will let you know Edrys has been her when you hear the wolf snarling behind you. You turn back toward the entrance of the cave to see the wolf facing of with two full grown grizzly bears. One is larger than the other, but they are both rounding on the wolf, teeth bared.
            \nDo you:
            \nMake a run for the hatch at the back of the cave
            \nOR
            \nPull the sword from the sheath at your back and fight the bears
            """)
        answer = input("> ")
        choice = answer.lower()

        if ("sword" in choice) or ("fight" in choice):
            print("""\nThe wolf looks in your direction and barks, head inclining toward the hatch. You know that he is telling you to run for it, but he has helped you get this far and you are going to do all you can to make sure that you both make it out of this moment alive. You pull the sword from the sheath at your back and move to stand next to the wolf, both hands around the hilt of the sword, at the ready.
                \nDo you go for the big bear or the smaller bear?
                """)
            answer = input("> ")
            choice = answer.lower()

            if "smaller" in choice:
                print("You run at the smaller of the two bears as the wolf attacks the larger bear. After a bit of a skirmish you sink the sword into the smaller bear's chest. It falls to the ground groaning. Beside you, the wolf is still fighting the bigger bear. He looks over at you and barks telling you again to run for the hatch. This time you listen.")
                return 'beach'
            
            elif "big" in choice:
                print("You run at the bigger of the two bears as the wolf goes for the smaller bear. The bear is nearly twice your size and after a few unsuccessful swipes at your face, the bear manages to knock you to the ground. You feel searing pain in your chest as the bear's claws rip into your skin. You turn your head to the side and see the wolf has managed to take down the smaller bear before everything goes dark.")
                input("[enter]")
                print("\nYou sit up as you come awake in your bed, hand to your chest which feels as though it is being ripped open. You remember the bear attack from your nightmare and take a deep breath. Thinking a snack may help you get back to sleep, you head to the kitchen.")
                input("[enter]")
                print("You lost. Thanks for playing. Maybe try taking on something closer to your own size next time.")
                exit(1)

            else:
                print("Please enter an available choice.")
                self.enter()
        
        elif ("run" in choice) or ("hatch" in choice):
            print("\nThe wolf looks in your direction and barks, head inclining toward the hatch. You know that he is telling you to run for it, so you do. You hear the sounds of the wolf wimpering and assume the bears managed to take him down. In your distraction you don't see a large rock between you and the hatch and you trip over it, feeling your ankle twist as you fall to the ground. You only barely register the sounds of the bears coming to you before they are on you, claws and teeth rip into your skin and everything goes dark.")
            input("[enter]")
            print("\nYour entire body hurts when you wake up in your bed. You remember being attacked by two bears in your nightmare. You get out of bed and stretch before heading to the kitchen for a snack before trying to get back to sleep.")
            input("[enter]")
            print("\nYou lost. Thanks for playing. Better luck next time!")
            exit(1)

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