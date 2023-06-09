
import sys
import pygame,random



pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
_width = 1080
_height = 720
score = 0
spawnSpeed = 80
screen = pygame.display.set_mode((_width,_height),32)
screen.fill((255,255,255))
gamee = True 
lose = False
endpoint = 0

arrowName=["right", "left", "up", "down"]
arrowList=[]

nInfo=pygame.display.Info()
full_screen_size = f_width,f_height = nInfo.current_w,nInfo.current_h


def show_screen():
    fpsClock.tick(fps)
    screen.fill((R,G,B))
    show_words(f"YOULOSE, SCORE {endpoint}",50,40)
    show_words(f"PRESS ESC TO END",50,60)
    pygame.display.flip()
    while True:
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: 
                pygame.quit()
            elif event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_ESCAPE: 
                    sys.exit() 


def show_words(words_str,width,height):
    font = pygame.font.SysFont("Castellar", 75)
    text = font.render(words_str, True, (180, 180, 180), (R,G,B))
    text_rect = text.get_rect(center=((f_width/100)*width, (f_height/100)*height))
    screen.blit(text, text_rect)

class arrow:
    global f_height, f_width
    def __init__(self,direction):
        self.type = direction
        self.img = pygame.image.load(direction+".png")
        self.img = pygame.transform.scale(self.img,(100,100))
        self.y = 50
        self.x = 50
        arrowList.append(self)
    def bilt_img(self,x,y):
        self.rect = self.img.get_rect(center=((f_width/100)*x, (f_height/100)*y))
        screen.blit(self.img, self.rect)
    def move(self,speed):
        if self.type=="left":
            self.x-=speed
        if self.type=="right":
            self.x+=speed
        if self.type=="up":
            self.y-=speed
        if self.type=="down":
            self.y+=speed
        self.bilt_img(self.x,self.y)
R=G=B=225
PUp=True
PDown=True
PRight=True
PLeft=True
speedUp=False
speed=0.25

while  gamee == True:
    fpsClock.tick(fps)
    show_words(f"SCORE {score}",20,20)
    pygame.display.flip()
    bgm = pygame.mixer.music.load("Canon_in_D.mp3")
    # bgm.play(loops=0, start=0.0, fade_ms = 0)
    screen.fill((R,G,B))
    if random.randint(1,spawnSpeed)==1:
        new = arrow(arrowName[random.randint(0,3)])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            show_screen()
            pygame.quit()
            
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                show_screen()
                pygame.quit()
    keys = pygame.key.get_pressed()
    if len(arrowList)>=1:
        if keys[pygame.K_UP] and arrowList[0].type=="up" and PUp==True:
            arrowList[0]= None
            arrowList.pop(0)
            R=random.randint(0,255)
            G=random.randint(0,255)
            B=random.randint(0,255)
            score+=1
            PUp=False
        elif not keys[pygame.K_UP] and PUp==False:
            PUp=True
        elif keys[pygame.K_DOWN] and arrowList[0].type=="down" and PDown==True:
            arrowList[0]= None
            arrowList.pop(0)
            R=random.randint(0,255)
            G=random.randint(0,255)
            B=random.randint(0,255)
            score+=1
            PDown=False
        elif not keys[pygame.K_DOWN] and PDown==False:
            PDown=True
        elif keys[pygame.K_RIGHT] and arrowList[0].type=="right" and PRight==True:
            arrowList[0]= None
            arrowList.pop(0)
            R=random.randint(0,255)
            G=random.randint(0,255)
            B=random.randint(0,255)
            score+=1
            PRight=False
        elif not keys[pygame.K_RIGHT] and PRight==False:
            PRight=True
        elif keys[pygame.K_LEFT] and arrowList[0].type=="left" and PLeft==True:
            arrowList[0]= None
            arrowList.pop(0)
            R=random.randint(0,255)
            G=random.randint(0,255)
            B=random.randint(0,255)
            score+=1
            PLeft=False
        elif not keys[pygame.K_LEFT] and PLeft==False:
            PLeft=True
    if score%20==0 and score!=0 and speedUp==False:
        spawnSpeed = int(spawnSpeed-(81-spawnSpeed))
        speed *= 1.2
        speedUp = True
    elif score%20==1 and score!=0 and speedUp==True:
        speedUp = False
    for i in arrowList:
        i.move(speed)
        if i.x<0 or i.x>100 or i.y>100 or i.y<0:
            print(f"score:{score}")
            endpoint = score
            lose = True
            gamee = False
            show_screen()
            pygame.quit()
