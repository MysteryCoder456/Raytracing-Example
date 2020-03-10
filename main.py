import sys
import pygame
from math import cos, sin, radians, sqrt
from random import randint
from wall import Wall
from particle import Particle
from defs import dist, map_val


def main():
    width, height = 1000, 500
    win_main = pygame.display.set_mode((width, height))
    win1 = pygame.Surface((width / 2, height))
    win2 = pygame.Surface((width / 2, height))
    pygame.display.set_caption("Raytracing")

    fps = 30
    clock = pygame.time.Clock()

    part = Particle((width / 4, height / 2))
    walls = []
    scene = []
    num_walls = 5

    # Add boundary walls
    walls.append(Wall((0, 0), (width/2, 0)))
    walls.append(Wall((width/2, 0), (width/2, height)))
    walls.append(Wall((width/2, height), (0, height)))
    walls.append(Wall((0, height), (0, 0)))

    # Add Walls randomly to the screen
    for i in range(num_walls):
        x1 = randint(0, width/2)
        y1 = randint(0, height)
        x2 = randint(0, width/2)
        y2 = randint(0, height)
        wall = Wall((x1, y1), (x2, y2))
        walls.append(wall)

    # Game Loop
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Input
        keys = pygame.key.get_pressed()
        rot_speed = 2
        move_speed = 5

        if keys[pygame.K_LEFT]:
            part.rotate(-rot_speed)
        if keys[pygame.K_RIGHT]:
            part.rotate(rot_speed)

        if keys[pygame.K_UP]:
            x_vel = cos(radians(part.hdg)) * move_speed
            y_vel = sin(radians(part.hdg)) * move_speed
            part.move(x_vel, y_vel)

        if keys[pygame.K_DOWN]:
            x_vel = cos(radians(part.hdg)) * -move_speed
            y_vel = sin(radians(part.hdg)) * -move_speed
            part.move(x_vel, y_vel)

        # Logic
        part.clean()

        scene = part.get_dists()

        m_pos = pygame.mouse.get_pos()
        # part.pos = m_pos

        part.update()
        part.look_at(walls)

        # Rendering
        win1.fill((0, 0, 0))
        win2.fill((0, 0, 0))

        part.draw(win1)

        for wall in walls:
            wall.draw(win1)

        for i in range(len(scene)):
            color = map_val(scene[i] ** 2, 0, (width / 2) ** 2, 255, 0)
            w = (width/2) / len(scene)
            h = map_val(scene[i], 0, width / 2, height, 0)
            x = (i * w) - (w / 2)
            y = height / 2 - h / 2
            pygame.draw.rect(win2, (color, color, color), (x, y, w+1, h))

        # Render surfaces to main window
        win_main.blit(win1, (0, 0))
        win_main.blit(win2, (width / 2 + 1, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
