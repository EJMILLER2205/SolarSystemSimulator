import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from systems import make_solar_system
from integrator import leapfrog_step

# -- Build the simulation --
bodies = make_solar_system([0, 0], [0, 0], 0) # creates a solar system with the star at the origin and no initial velocity

# -- Run the simulation --
dt = 0.1
steps = 5000

print("simualting...")
for _ in range(steps): # runs the simulation for 5000 steps, updating the positions and velocities of the bodies at each step
    leapfrog_step(bodies, dt)
print("Done. Rendering...")

# -- Animate --
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black') # creates a figure and axis for plotting, with a black background
ax.set_facecolor('black') # sets the background color of the axis to black
ax.set_xlim(-500, 500) # sets the limits of the x-axis to be from -500 to 500
ax.set_ylim(-500, 500) # sets the limits of the y-axis to be from -500 to 500
ax.set_aspect('equal') # sets the aspect ratio of the plot to be equal, so that circles look like circles and not ellipses

# draw tails
for b in bodies: # loops through each body and plots its history as a line, with the color of the body and some transparency
    hist = np.array(b.history) # converts the history list into an array
    ax.plot(hist[:, 0], hist[:, 1], color = b.color, alpha = 0.15, linewidth = 0.5) # hist[:, 0] grabs every rows x value, hist[:, 1] grabs every rows y value, alpha makes the trail faint, linewidth is witdth

# animated dots
# creates an array of line2D objects, that start at an empty position [][], and plots a single point 'o' with b.color and b.radius for all bodies and we scale by .6 to make the size better visually. [0] allows for storing objects instead of lists
dots = [ax.plot([], [], 'o', color = b.color, markersize = b.radius * 0.6)[0] for b in bodies]

def update(frame): # each frame (5000 frames) it updates hteb positions of the dots
    for i, b in enumerate(bodies):  # loops through all bodies
        dots[i].set_data([b.history[frame][0]], [b.history[frame][1]]) # gets history at step frame and updates the dot positon to match it
    return dots

# The ani line essentially does this:
# for frame in range(steps):
#  update(frame)
#  wait(interval)
#  redraw()
ani = animation.FuncAnimation(fig, update, frames = steps, interval = 20, blit = True)
plt.tight_layout() # adjusts padding and space around the plot
plt.show() # shows the display
