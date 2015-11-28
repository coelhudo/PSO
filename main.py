__author__ = 'coelhudo'

from numpy import arange
import matplotlib.pyplot as plt
from particle import Particle
from random import random
from time import sleep

particles = [Particle(i) for i in range(0,10)]

xs,ys = zip(*[(p.position[0], p.position[1]) for p in particles])

plt.ion()

def utility_function(xy):
    return 1 - abs(0.5 - xy[0]) - abs(0.5 - xy[1])

plt.axis([0, 1, 0, 1])
for i in arange(0, 1, 0.1):
    plt.gcf().gca().add_artist(plt.Circle((0.5,0.5),i,color='black', fill=False))

particles_lines = [plt.plot(x, y, 'ro') for x, y in zip(xs,ys)]
#labels = [str(particle) for particle in particles]

def annotate(label, x, y):
    return plt.annotate(
                        label,
                        xy = (x, y), xytext = (-20, 20),
                        textcoords = 'offset points',
                        ha = 'right', va = 'bottom',
                        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

#annotates = [annotate(label, x, y) for label, x, y in zip(labels, xs, ys)]

for particle in particles:
    print(str(particle) + ' fitness {}'.format(utility_function(particle.position)))

for i in arange(1, 1000):
    #for annotate, particle_lines in zip(annotates, particles_lines):
    for particle_lines in particles_lines:
        factor = -1 if random() > 0.5 else 1
        x_delta = factor * random()/10
        y_delta = factor * random()/10
        new_x_position = particle_lines[0].get_xdata() + x_delta
        new_y_position = particle_lines[0].get_ydata() + y_delta
        current_utility = utility_function((particle_lines[0].get_xdata(), particle_lines[0].get_ydata()))
        new_utility = utility_function((new_x_position, new_y_position))
        if new_utility > current_utility:
            particle_lines[0].set_xdata(new_x_position)
            particle_lines[0].set_ydata(new_y_position)
        plt.draw()