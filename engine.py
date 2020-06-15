from sys import exit
from random import randint
from textwrap import dedent

import scenes
import wolfscenes


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


class Map(object):
    
    wolf_scenes = {'well' : scenes.Well(),
            'cabin' : scenes.Cabin(),
            'shed' : scenes.Shed(),
            'bridge' : scenes.Bridge(),
            'cave' : scenes.Cave(),
            'beach' : scenes.Beach(),
            'final': scenes.Final(),
            'finished' : scenes.Finished()
    }
    non_wolf_scenes = {'kitchen' : scenes.Kitchen(),
                    'garden' : scenes.Garden(),
                    'forest' : scenes.Forest(),
                    'well' : wolfscenes.Well(),
                    'cabin' : wolfscenes.Cabin(),
                    'shed' : wolfscenes.Shed(),
                    'bridge' : wolfscenes.Bridge(),
                    'cave' : wolfscenes.Cave(),}

    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.wolf = None

    def has_wolf(self, inventory = scenes.inventory):
        if "wolf" in scenes.inventory:
            self.wolf = 'wolf'
            return self.wolf

    def next_scene(self, scene_name):
        self.has_wolf()
        if self.wolf == 'wolf':
            val = Map.wolf_scenes.get(scene_name)
            return val
        else:
            val = Map.non_wolf_scenes.get(scene_name)
            return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)