
import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,1000),pygame.FULLSCREEN,32)



while  True:
    screen.fill((110,123,139))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)
    
    rightimg = pygame.image.load("right.png")
    screen.blit(rightimg,(50,20))

    leftimg = pygame.image.load("left.png")
    screen.blit(leftimg,(50,20))

    upimg = pygame.image.load("up.png")
    screen.blit(upimg,(50,20))

    downimg = pygame.image.load("down.png")
    screen.blit(downimg,(50,20))

    pygame.display.flip()

