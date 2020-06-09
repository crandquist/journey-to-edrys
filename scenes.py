from sys import exit

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
        pass

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
        pass

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