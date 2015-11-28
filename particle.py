__author__ = 'coelhudo'

from random import random

class Particle:
    def __init__(self, id):
        self.__id = id
        self.particle_best = 0
        self.global_best = 0
        self.__position = [random(), random()]
        self.velocity = 0
        self.direction = 0

    def __iter__(self):
        return self.__position

    @property
    def position(self):
            return self.__position

    @property
    def position(self):
            return self.__position

    def __str__(self):
        return 'Agent {}'.format(str(self.__id))

    def __repr__(self):
        return str(self)