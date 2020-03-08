import pygame
from ray import Ray


class Particle:
    """
    Make a Particle that emits light

    Arguments:
        pos {tuple} -- starting position of particle
    """
    def __init__(self, pos):
        self.pos = pos
        self.rays = []
        self.lines = []

        for angle in range(0, 359, 10):
            ray = Ray(self.pos, angle)
            self.rays.append(ray)

    def look_at(self, wall):
        for ray in self.rays:
            p = ray.collide_wall(wall)
            self.lines.append((ray.pos, p))

    def update(self):
        for ray in self.rays:
            ray.pos = self.pos

    def draw(self, window):
        # Render ray lines
        for line in self.lines:
            if line[1] is not None:
                pygame.draw.line(window, (255, 255, 255), line[0], line[1])

        # Render particle center
        c_radius = 8
        pygame.draw.ellipse(
            window,
            (255, 255, 255),
            (self.pos[0] - c_radius, self.pos[1] -
             c_radius, c_radius * 2, c_radius * 2)
        )
