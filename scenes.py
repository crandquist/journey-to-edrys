from sys import exit

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