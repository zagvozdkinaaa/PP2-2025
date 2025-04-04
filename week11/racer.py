import pygame, sys
from pygame.locals import *
import time, random
pygame.init()
pygame.mixer.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SPEED = 5
SCORE = 0
COINS_SCORE = 0
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image and music
background = pygame.image.load('/Users/zagvozdkinaaa/PP2/week11/media/AnimatedStreet.png')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

pygame.mixer.music.load('/Users/zagvozdkinaaa/PP2/week11/media/background.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/zagvozdkinaaa/PP2/week11/media/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/zagvozdkinaaa/PP2/week11/media/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

# Coin class with weight
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice([1, 2, 3])  # Different coin values
        self.image = pygame.image.load('/Users/zagvozdkinaaa/PP2/week11/media/coinimg.png')
        size = 20 + 5 * self.weight  # Different sizes for different weights
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED - 2)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.weight = random.choice([1, 2, 3])
        size = 20 + 5 * self.weight
        self.image = pygame.image.load('/Users/zagvozdkinaaa/PP2/week11/media/coinimg.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

E1 = Enemy()
P1 = Player()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)  # Timer to gradually increase speed

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    coin_score = font_small.render(f"Coins: {COINS_SCORE}", True, BLACK)
    screen.blit(coin_score, (SCREEN_WIDTH - 100, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('/Users/zagvozdkinaaa/PP2/week11/media/crash.wav').play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision with coin
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            COINS_SCORE += coin.weight
            pygame.mixer.Sound('/Users/zagvozdkinaaa/PP2/week11/media/coin.wav').play()
            coin.reset_position()

            # Increase enemy speed based on coin score threshold
            if COINS_SCORE % 5 == 0:
                SPEED += 1

    pygame.display.update()
    FramePerSec.tick(FPS)