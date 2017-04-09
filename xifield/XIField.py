import pygame
import numpy as np
import sys
from time import sleep

WHITE = (255,) * 3

class XIField:
    def __init__(self, size, grid, bg_color, grid_color):
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.bg_color = bg_color
        self.grid = grid
        self.grid_color = grid_color
        self.pos = [0, 0]
    def main(self):
        self.screen.fill(self.bg_color)
        for x in range(self.grid[0]):
            pos_x = x * self.size[0] // self.grid[0]
            pygame.draw.line(self.screen, self.grid_color, (pos_x, 0), (pos_x, self.size[1]))
        for y in range(self.grid[1]):
            pos_y = y * self.size[1] // self.grid[1]
            pygame.draw.line(self.screen, self.grid_color, (0, pos_y), (self.size[0], pos_y))
        pygame.draw.rect(self.screen, WHITE, (*self.pos, 20, 20))
        pygame.display.flip()

def main():
    pygame.init()
    field = XIField((500, 500), (5, 5), (0,) * 3, (255,) * 3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    field.pos[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    field.pos[0] += 1
                elif event.key == pygame.K_UP:
                    field.pos[1] -= 1
                elif event.key == pygame.K_DOWN:
                    field.pos[1] += 1
            elif event.type == pygame.QUIT:
                sys.exit()
        field.main()
        sleep(0.01)

if __name__ == '__main__':
    main()

