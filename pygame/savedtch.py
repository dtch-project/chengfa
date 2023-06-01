
import sys
import pygame

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1080,720),pygame.FULLSCREEN,32)
screen.fill((255,255,255))


def bilt_img(imgname,width_level,height_level):
    img = pygame.image.load(imgname)
    img = pygame.transform.scale(img,(100,100))
    img_rect = img.get_rect(center=((f_width/100)*width_level, (f_height/100)*height_level))
    screen.blit(img, img_rect)





while  True:
    fpsClock.tick(fps)
    #now=n
    nInfo=pygame.display.Info()
    #full_screen=f
    full_screen_size = f_width,f_height = nInfo.current_w,nInfo.current_h    
    bilt_img("right.png",50,50)
    bilt_img("left.png",50,50)
    bilt_img("up.png",50,50)
    bilt_img("down.png",50,50)
    pygame.display.flip()
    screen.fill((255,255,255))


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
