from sys import exit

class Scene(object):

    def __init__(self):
        self.name = "I am a scene."

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Kitchen(Scene):
    pass

class Garden(Scene):
    pass

class Forest(Scene):
    pass

class Well(Scene):
    pass

class Cabin(Scene):
    pass

class Shed(Scene):
    pass

class Bridge(Scene):
    pass

class Cave(Scene):
    pass

class Beach(Scene):
    pass

class Final(Scene):
    pass