from sys import exit
from random import randint
from textwrap import dedent

import scenes
import wolfscenes

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


class Map(object):
    
    non_wolf_scenes = {'kitchen' : scenes.Kitchen(),
            'garden' : scenes.Garden(),
            'forest' : scenes.Forest(),
            'well' : scenes.Well(),
            'cabin' : scenes.Cabin(),
            'shed' : scenes.Shed(),
            'bridge' : scenes.Bridge(),
            'cave' : scenes.Cave(),
            'beach' : scenes.Beach(),
            'finished' : scenes.Finished()
    }
    wolf_scenes = {'well' : wolfscenes.Well(),
                    'cabin' : wolfscenes.Cabin(),
                    'shed' : wolfscenes.Shed(),
                    'bridge' : wolfscenes.Bridge(),
                    'cave' : wolfscenes.Cave(),}

    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.inventory = []
        self.wolf = False

    def has_wolf(self, inventory = inventory):
        if "wolf" in inventory:
            self.wolf = True

    def next_scene(self, scene_name):
        self.has_wolf()
        if self.wolf == False:
            val = Map.non_wolf_scenes.get(scene_name)
            return val
        elif self.wolf == True:
            val = Map.wolf_scenes.get(scene_name)
            return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)