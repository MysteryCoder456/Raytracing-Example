import pygame
from ray import Ray
from dist import dist


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

        # for angle in range(0, 360, 0.5):
        #     ray = Ray(self.pos, angle)
        #     self.rays.append(ray)

        angle = 0
        while angle < 360:
            ray = Ray(self.pos, angle)
            self.rays.append(ray)
            angle += 0.5

    def clean(self):
        self.lines = []

    def look_at(self, walls):
        for ray in self.rays:
            closest = None
            record = 2000
            for wall in walls:
                p = ray.collide_wall(wall)
                if p is not None:
                    d = dist(ray.pos, p)
                    if d < record:
                        record = d
                        closest = p
            self.lines.append((ray.pos, closest))

    def update(self):
        for ray in self.rays:
            ray.pos = self.pos

    def draw(self, window):
        # Render ray lines
        alpha = 75
        color = pygame.Color(255 - alpha, 255 - alpha, 255 - alpha)
        for line in self.lines:
            if line[1] is not None:
                pygame.draw.line(window, color, line[0], line[1])

        # Render particle center
        c_radius = 8
        pygame.draw.ellipse(
            window,
            (255, 255, 255),
            (self.pos[0] - c_radius, self.pos[1] -
             c_radius, c_radius * 2, c_radius * 2)
        )
