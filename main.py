import sys
import pygame
from random import randint
from wall import Wall
from particle import Particle


def main():
    width, height = 800, 800
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Raytracing")

    fps = 30
    clock = pygame.time.Clock()

    part = Particle((width / 2, height / 2))
    walls = []
    num_walls = 5

    # Add boundary walls
    walls.append(Wall((0, 0), (width, 0)))
    walls.append(Wall((width, 0), (width, height)))
    walls.append(Wall((width, height), (0, height)))
    walls.append(Wall((0, height), (0, 0)))

    # Add Walls randomly to the screen
    for i in range(num_walls):
        x1 = randint(0, width)
        y1 = randint(0, height)
        x2 = randint(0, width)
        y2 = randint(0, height)
        wall = Wall((x1, y1), (x2, y2))
        walls.append(wall)

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Logic
        part.clean()

        m_pos = pygame.mouse.get_pos()
        part.pos = m_pos

        part.update()
        part.look_at(walls)

        # Rendering
        win.fill((0, 0, 0))

        part.draw(win)

        for wall in walls:
            wall.draw(win)

        pygame.display.update()


if __name__ == "__main__":
    main()
