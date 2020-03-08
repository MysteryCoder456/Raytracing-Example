import pygame
import sys
from wall import Wall


def main():
    width, height = 800, 800
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Raytracing")

    fps = 40
    clock = pygame.time.Clock()

    wall = Wall((600, 200), (600, 600))

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        win.fill((0, 0, 0))

        wall.draw(win)

        pygame.display.update()


if __name__ == "__main__":
    main()
