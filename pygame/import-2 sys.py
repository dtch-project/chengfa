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

    #pygame.display.flip()
    fpsClock.tick(fps)

    rightimg = pygame.image.load("C:\\Users\\Hannah\\Untitled-2\\right.png")
    screen.blit(pygame.transform.scale(rightimg, (100, 100)),(510,460))

    leftimg = pygame.image.load("C:\\Users\\Hannah\\Untitled-2\\left.png")
    screen.blit(pygame.transform.scale(leftimg, (100, 100)),(410,460))

    upimg = pygame.image.load("C:\\Users\\Hannah\\Untitled-2\\up.png")
    screen.blit(pygame.transform.scale(upimg, (100, 100)),(460,410))

    downimg = pygame.image.load("C:\\Users\\Hannah\\Untitled-2\\down.png")
    screen.blit(pygame.transform.scale(downimg, (100, 100)),(460,510))

    pygame.display.flip()
