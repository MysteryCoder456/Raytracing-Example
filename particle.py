import pygame
from math import cos, radians, atan2
from ray import Ray
from defs import dist


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
        self.dists = []
        self.hdg = 0
        self.fov = 34  # the angle for half of the field of view
        self.angle_step = 0.5

        # for angle in range(-self.fov, self.fov, self.angle_step):
        #     ray = Ray(self.pos, angle + self.hdg)
        #     self.rays.append(ray)

        # While loop for floating point angle steps
        angle = -self.fov
        while angle < self.fov:
            ray = Ray(self.pos, angle + self.hdg)
            self.rays.append(ray)
            angle += self.angle_step

    def get_dists(self):
        return self.dists

    def move(self, x, y):
        self.pos = (x + self.pos[0], y + self.pos[1])

    def rotate(self, angle):
        self.hdg += angle
        self.rays = []
        angle = -self.fov

        while angle < self.fov:
            ray = Ray(self.pos, angle + self.hdg)
            self.rays.append(ray)
            angle += self.angle_step

    def clean(self):
        self.lines = []
        self.dists = []

    def look_at(self, walls):
        for ray in self.rays:
            closest = None
            record = 2000
            for wall in walls:
                p = ray.collide_wall(wall)
                if p is not None:
                    d = dist(ray.pos, p)
                    a = ray.get_heading() - radians(self.hdg)
                    d *= cos(a)
                    if d < record:
                        record = d
                        closest = p
            
            self.lines.append((ray.pos, closest))
            self.dists.append(record)

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
        c_radius = 6
        pygame.draw.ellipse(
            window,
            (255, 255, 255),
            (self.pos[0] - c_radius, self.pos[1] -
             c_radius, c_radius * 2, c_radius * 2)
        )
