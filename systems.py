import numpy as np
from body import Body

G = 1.0

def make_solar_system(pos, vel, tag):
    star = Body(1000000, pos, vel, 15, "yellow", tag) # creates star
    bodies = [star] # creates a list of bodies starting with the star
    planet_params = [ # (distance from star, mass, color)
    (120, 1, 'deepskyblue'),
    (220, 2, 'tomato'),
    (340, 1, 'mediumpurple'),]
    for i in range(len(planet_params)): # loops through the planet parameters and creates a body for each one, adding it to the list of bodies
        bodies.append(Body(planet_params[i][1], [pos[0] + planet_params[i][0], pos[1]], [vel[0], vel[1] + np.sqrt(G * star.mass / planet_params[i][0])], 2, planet_params[i][2], tag))
    return bodies
