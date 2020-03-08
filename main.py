import sys
import pygame
from wall import Wall
from particle import Particle


def main():
    width, height = 800, 800
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Raytracing")

    fps = 45
    clock = pygame.time.Clock()

    wall = Wall((600, 200), (600, 600))
    part = Particle((width / 2, height / 2))

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Logic
        part.update()
        part.look_at(wall)

        # Rendering
        win.fill((0, 0, 0))

        part.draw(win)
        wall.draw(win)

        pygame.display.update()


if __name__ == "__main__":
    main()
