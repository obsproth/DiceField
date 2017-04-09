import pygame
import sys
from time import sleep

BLACK = (0,) * 3
WHITE = (255,) * 3

class XIField:
    def __init__(self, size):
        self.screen = pygame.display.set_mode(size)
        self.pos = [0, 0]
    def main(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, (*self.pos, 20, 20))
        pygame.display.flip()

def main():
    pygame.init()
    field = XIField((500, 500))
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

