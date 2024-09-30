class AbstractVisionModel():
    def __init__(self, vision):
        self.name = vision.name
        self.model = vision.model
        self.position = vision.position
        self.range = vision.range

    def view(self, vision):
        pass

    def scene(self, vision):
       pass
