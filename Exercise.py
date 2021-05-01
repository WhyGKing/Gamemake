import pygame
import random
import sys


### 함수선언
def playGame():
    global monitor

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    while True:
        # (pygame.time.Clock()).tick(50)
        monitor.fill((r, g, b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        pygame.display.update()

### 젼역변수
r,g,b = [0] * 3
swidth, sheight = 500, 600
monitor = None


### 메인코드
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))

playGame()


