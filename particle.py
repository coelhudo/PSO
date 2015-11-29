__author__ = 'coelhudo'

from random import random

class Particle:
    def __init__(self, id):
        self.__id = id
        self.particle_best = 0
        self.global_best = 0
        self.__position = (random(), random())
        self.velocity = 0
        self.direction = 0

    @property
    def position(self):
        return self.__position

    def subscribe(self, update):
        self.update = update

    def move(self, delta):
        self.__position = tuple(map(sum,zip(self.__position,delta)))
        self.update(delta)

    def __str__(self):
        return 'Agent {}'.format(str(self.__id))

    def __repr__(self):
        return str(self)