import numpy as np

G = 1.0

# Takes a list of all the bodies in the simulation and returns the acceleration of each one
def compute_acceleration(bodies):
    n = len(bodies) # counts how many bodies there are
    acc = np.zeros((n, 2)) # creatres a 2d array of zeros with shape (n, 2), one row per body, two columns for x and y acceleration
    # Loops through every pair of bodies
    for i in range(n):
        for j in range(n):
            # skips if they are the same
            if i == j:
                continue
            r = bodies[j].pos - bodies[i].pos # creates the vector pointing from body i to body j
            dist = np.linalg.norm(r) # calculates the straight line distnace between two bodies (pythagoras theorem)
            # softening required cause cause if bodies get very close then r gets close to 0and the force would shoot towards infinity, softening adds a small minimum distance
            softening = 5.0
            dist_soft = np.sqrt(dist**2 + softening**2)
            # calculates acceleration for body i
            acc[i][0] += G * bodies[j].mass / dist_soft**3 * r[0]  # x component
            acc[i][1] += G * bodies[j].mass / dist_soft**3 * r[1]  # y component
    return acc