import pygame
import sys
from wall import Wall
from ray import Ray


def main():
    width, height = 800, 800
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Raytracing")

    fps = 40
    clock = pygame.time.Clock()

    wall = Wall((600, 200), (600, 600))
    ray = Ray((200, 400), (1, 0))

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Logic
        mouse_pos = pygame.mouse.get_pos()

        ray.point(mouse_pos)

        # Rendering

        win.fill((0, 0, 0))

        ray.draw(win)

        wall.draw(win)

        pygame.display.update()


if __name__ == "__main__":
    main()
