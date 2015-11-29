__author__ = 'coelhudo'

from random import random
import utility_function


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Point(self.__x - other.__x, self.__y - other.__y)

    def scalar_mul(self, scalar):
        return Point(self.__x * scalar, self.__y * scalar)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Particle:
    def __init__(self, id):
        self.__id = id
        self.__position = Point(random(), random())
        self.__particle_best = self.__position
        self.__velocity = Point(0, 0)

    @property
    def position(self):
        return self.__position

    @property
    def p_best(self):
        return self.__particle_best

    def calculate_fitness(self, delta):
        candidate = self.position + delta
        if utility_function.f(candidate) > utility_function.f(self.__position):
            self.__particle_best = candidate

    def move(self, global_best):
        particle_op = (self.__particle_best - self.position).scalar_mul(2 * random()/10)
        global_op = (global_best - self.position).scalar_mul(2 * random()/10)
        self.__velocity += particle_op + global_op
        self.__position += self.__velocity
        self.update(self.__velocity)

    def subscribe(self, update):
        self.update = update

    def __str__(self):
        return 'Agent {}'.format(str(self.__id))

    def __repr__(self):
        return str(self)