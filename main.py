import pygame
import sys


def logic():
    pass


def draw():
    pass


def main():
    width, height = 800, 800
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Raytracing")

    fps = 40
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        win.fill((0, 0, 0))

        logic()
        draw()

        pygame.display.update()


if __name__ == "__main__":
    main()
