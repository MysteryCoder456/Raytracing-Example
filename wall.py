import pygame


class Wall:
    def __init__(self, pos1, pos2):
        """
        Class to make a Wall
        
        Arguments:
            pos1 {tuple} -- position of first point
            pos2 {tuple} -- position of second point
        """
        self.pos1 = pos1
        self.pos2 = pos2

    def draw(self, window):
        pygame.draw.line(window, (255, 255, 255), self.pos1, self.pos2, 3)
