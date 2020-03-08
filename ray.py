from math import cos, sin, radians
import pygame


class Ray:
    def __init__(self, pos, angle):
        """
        Class to make a light ray
        
        Arguments:
            pos {tuple} -- starting position of ray
            angle {int} -- direction in degrees where the ray is pointing to
        """
        self.pos = pos

        # Direction in a normalized vector
        x = cos(radians(angle))
        y = sin(radians(angle))
        self.dir = (x, y)

    def collide_wall(self, wall):
        x1 = wall.pos1[0]
        y1 = wall.pos1[1]
        x2 = wall.pos2[0]
        y2 = wall.pos2[1]
        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if t > 0 and t < 1 and u > 0:
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            return (x, y)
        return None

    def point(self, angle):
        # Direction in a normalized vector
        norm = (cos(radians(angle)), sin(radians(angle)))
        self.dir = norm

    def draw(self, window):
        mult = 15
        pos2 = (self.pos[0] + self.dir[0] * mult,
                self.pos[1] + self.dir[1] * mult)
        pygame.draw.line(window, (255, 255, 255), self.pos, pos2)
