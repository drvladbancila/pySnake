import math
from random import randint


class Snake:
    def __init__(self, x, y, xvel, yvel, max_x, max_y, length=1, grid_size=10):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.max_x = max_x
        self.max_y = max_y
        self.length = length
        self.grid_size = grid_size
        self.past_position = [(x, y)]

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_velocity(self, xvel, yvel):
        self.xvel = xvel
        self.yvel = yvel

    def increment_length(self):
        self.length = self.length + 1

    def update_position(self):
        self.past_position[1:] = self.past_position[0:self.length - 1]
        self.past_position[0] = (self.x, self.y)
        self.x = self.x + self.xvel * self.grid_size
        self.y = self.y + self.yvel * self.grid_size

        if self.x >= self.max_x:
            self.x = 0
        elif self.x < 0:
            self.x = self.max_x

        if self.y >= self.max_y:
            self.y = 0
        elif self.y < 0:
            self.y = self.max_y

    def eaten_itself(self):
        for pos in self.past_position:
            if dist(self.x, self.y, pos[0], pos[1]) < self.grid_size:
                return True

    def die(self):
        self.length = 1
        self.past_position = [(self.x, self.y)]
        self.x = self.max_x / 2
        self.y = self.max_y / 2


class Fruit:
    def __init__(self, max_x, max_y, x=0, y=0, grid_size=10):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.grid_size = grid_size

    def generate(self):
        self.x = int(math.floor(randint(0, (self.max_x - self.grid_size) / self.grid_size) * self.grid_size))
        self.y = int(math.floor(randint(0, (self.max_y - self.grid_size) / self.grid_size) * self.grid_size))

    def eaten(self, snake):
        if dist(snake.x, snake.y, self.x, self.y) < self.grid_size:
            return True
        else:
            return False


def dist(x1, y1, x2, y2):
    squared_distance = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    distance = math.sqrt(squared_distance)
    return distance
