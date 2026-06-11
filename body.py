import numpy as np

class Body:
    def __init__(self, mass, pos, vel, radius = 1.0, color = 'white', tag = 0):
        self.mass = mass
        self.pos = np.array(pos, dtype = float)
        self.vel = np.array(vel, dtype = float)
        self.radius = radius
        self.color = color
        self.tag = tag
        self.history = [self.pos.copy()]
    def record(self):
        self.history.append(self.pos.copy()) # Creates a copy of the starting position and saves it
