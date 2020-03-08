import pygame
from math import atan2, cos, sin


class Ray:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir

    def point(self, pos):
        dx = pos[0] - self.pos[0]
        dy = pos[1] - self.pos[1]
        angle = atan2(dy, dx)

        # Direction in normalized form
        norm = (cos(angle), sin(angle))
        self.dir = norm

    def draw(self, window):
        mult = 10
        pos2 = (self.pos[0] + self.dir[0] * mult, self.pos[1] + self.dir[1] * mult)
        pygame.draw.line(window, (255, 255, 255), self.pos, pos2)
