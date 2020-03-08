import pygame


class Wall:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def draw(self, window):
        pygame.draw.line(window, (255, 255, 255), self.pos1, self.pos2, 3)
