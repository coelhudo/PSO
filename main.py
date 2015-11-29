__author__ = 'coelhudo'

from numpy import arange
import matplotlib.pyplot as plt
from particle import Particle, Point
from random import random
import utility_function

print(utility_function)

plt.ion()

plt.axis([0, 1, 0, 1])
for i in arange(0, 1, 0.1):
    plt.gcf().gca().add_artist(plt.Circle((0.5, 0.5), i, color='black', fill=False))

particles = [Particle(i) for i in range(0, 50)]

xs, ys = zip(*[(p.position.x, p.position.y) for p in particles])
particles_lines = [plt.plot(x, y, 'ro') for x, y in zip(xs, ys)]

for particle, particle_line in zip(particles, particles_lines):
    def make_update_particle():
        def update_particle(current_delta, current_particle_line=particle_line[0]):
            current_particle_line.set_xdata(current_particle_line.get_xdata() + current_delta.x)
            current_particle_line.set_ydata(current_particle_line.get_ydata() + current_delta.y)
            plt.draw()
        return update_particle

    particle.subscribe(make_update_particle())

#labels = [str(particle) for particle in particles]

#def annotate(label, x, y):
#    return plt.annotate(
#                        label,
#                        xy = (x, y), xytext = (-20, 20),
#                        textcoords = 'offset points',
#                        ha = 'right', va = 'bottom',
#                        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
#                        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

#annotates = [annotate(label, x, y) for label, x, y in zip(labels, xs, ys)]

#for particle in particles:
#    print(str(particle) + ' fitness {}'.format(utility_function(particle.position)))

global_solution = None
for i in arange(1, 1000):
    #for annotate, particle_lines in zip(annotates, particles_lines):
    for particle in particles:
        factor = -1 if random() > 0.5 else 1
        delta = Point(factor * random()/100, factor * random()/100)
        particle.calculate_fitness(delta)

    global_best = max([(particle.p_best, utility_function.f(particle.p_best)) for particle in particles],
                      key=lambda x: x[1])
    global_solution = global_best[0]

    for particle in particles:
        particle.move(global_best[0])

print('Global solution {}'.format(global_solution))