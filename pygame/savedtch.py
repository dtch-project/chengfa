
import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1920,1080
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)


rightimg = pygame.image.load("right.png")
screen.blit(rightimg,(500,200))

leftimg = pygame.image.load("left.png")
screen.blit(leftimg,(500,200))

upimg = pygame.image.load("up.png")
screen.blit(upimg,(500,200))

downimg = pygame.image.load("down.png")
screen.blit(downimg,(500,200))

pygame.display.flip()

while  True:
    screen.fill((110,123,139))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    fpsClock.tick(fps)


