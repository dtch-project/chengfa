#####
#製作流程圖
#開始 -> 設置窗口大小和標題 -> 載入圖片和聲音 -> 定義遊戲物件 ->
#創建鳥、管道和地面 -> 創建精靈組 -> 設置計時器和分數 ->
#遊戲循環 -> 處理事件 -> 更新遊戲物件 -> 檢測碰撞 -> 檢測得分 ->
#繪製遊戲畫面 -> 更新屏幕 -> 循環
#####
import pygame

pygame.init()

# 2. 設置 Pygame 窗口
# 使用 Pygame 创建窗口，代码如下：

# 设置窗口大小和标题
size = (288, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

# 3. 載入圖片和聲音
# 將所有的圖片和聲音文件放在一個文件夾中，然後使用 Pygame 載入它們。在這個遊戲中，需要載入以下圖片和聲音：

# 載入圖片
background = pygame.image.load("assets/background.png").convert()
ground = pygame.image.load("assets/ground.png").convert()
bird = pygame.image.load("assets/bird.png").convert_alpha()
pipe = pygame.image.load("assets/pipe.png").convert_alpha()

# 載入聲音
flap_sound = pygame.mixer.Sound("assets/sounds/sfx_wing.wav")

# 4. 定義遊戲物件
# 定義幾個遊戲物件，包括鳥、管道和地面。在這個遊戲中，需要定義以下物件：

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 200
        self.velocity = 0

    def flap(self):
        self.velocity = -10
        flap_sound.play()

    def update(self):
        self.velocity += 0.5
        self.rect.y += self.velocity

class Pipe(pygame.sprite.Sprite):
    def __init__(self, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pipe
        self.rect = self.image.get_rect()
        self.rect.x = 288
        self.rect.y = height

    def update(self):
        self.rect.x -= 3

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 450

    def update(self):
        self.rect.x -= 3
        if self.rect.x < -288:
            self.rect.x = 0

# 5. 定義遊戲循環
# 定義遊戲循環，包括遊戲的主要邏輯和事件處理。在這個遊戲中，需要定義以下循環：

# 創建鳥、管道和地面
bird = Bird()
pipe1 = Pipe(250)
pipe2 = Pipe(100)
ground = Ground()

# 創建精靈組
pipes = pygame.sprite.Group()
pipes.add(pipe1, pipe2)

# 設置計時器和分數
clock = pygame.time.Clock()
score =

# 遊戲循環
while True:
    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # 更新遊戲物件
    bird.update()
    pipes.update()
    ground.update()

    # 檢測碰撞
    if pygame.sprite.collide_rect(bird, ground):
        print("Game over!")
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollide(bird, pipes, False):
        print("Game over!")
        pygame.quit()
        sys.exit()

    # 檢測得分
    if bird.rect.x > pipe1.rect.x and not pipe1.passed:
        pipe1.passed = True
        score += 1
        print("Score:", score)

    if bird.rect.x > pipe2.rect.x and not pipe2.passed:
        pipe2.passed = True
        score += 1
        print("Score:", score)

    # 繪製遊戲畫面
    screen.blit(background, (0, 0))
    pipes.draw(screen)
    screen.blit(ground, (0, 450))
    screen.blit(bird.image, bird.rect)

    # 更新屏幕
    pygame.display.flip()
    clock.tick(60)


