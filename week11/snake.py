import pygame, sys, random
from pygame.math import Vector2

class Snake():
    def __init__(self):
        self.body=[Vector2(5,10), Vector2(4,10)]
        self.direction=Vector2(1,0)
        self.add_block = False
    def draw_snake(self):
        for block in self.body:
            x_pos=int(block.x*sell_size)
            y_pos=int(block.y*sell_size)
            snake_rect=pygame.Rect(x_pos, y_pos, sell_size, sell_size)
            pygame.draw.rect(screen, (133, 113, 199), snake_rect)
    def move_snake(self):
        if self.add_block:
            body_copy = self.body[:]
            self.add_block = False
        else:
            body_copy = self.body[:-1]

        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

class Food:
    def __init__(self):
        self.randomize()
    def randomize(self):
        self.x = random.randint(0, sell_number - 1)
        self.y = random.randint(0, sell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.weight = random.choice([1, 2, 3])
        self.timer = pygame.time.get_ticks()
    def draw_food(self):
        color = {1: (224, 61, 80), 2: (255, 180, 50), 3: (90, 180, 255)}[self.weight]
        food_rect=pygame.Rect(int(self.pos.x*sell_size), int(self.pos.y*sell_size), sell_size, sell_size)
        pygame.draw.rect(screen, color, food_rect)
    def is_expired(self):
        return pygame.time.get_ticks() - self.timer > 5000

class Main:
    def __init__(self):
        self.snake=Snake()
        self.food=Food()
        self.score = 0
        self.level = 1
        self.speed = 150
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_food_timer()
        self.check_fail()
    def check_food_timer(self):
        if self.food.is_expired():
            self.food.randomize()
    def draw_elements(self):
        self.draw_grass()
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_score()
    def check_collision(self): #collision with food
        if self.food.pos == self.snake.body[0]:
            self.score += self.food.weight 
            self.snake.add_block = True
            self.food.randomize()
            if self.score // 5 + 1 > self.level:
                self.level += 1
                self.increase_speed()
    def check_fail(self): #collision with borders and itself
        if not 0 <= self.snake.body[0].x < sell_number or not 0 <= self.snake.body[0].y <sell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over() 
    def game_over(self):
        pygame.quit()
        sys.exit()
    def draw_grass(self):
        grass_color=(180, 214, 107)
        for row in range(sell_number):
            if row%2==0:
                for col in range(sell_number):
                    if col%2==0:
                        grass_rect= pygame.Rect(col*sell_size, row*sell_size, sell_size, sell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(sell_number):
                    if col%2!=0:
                        grass_rect= pygame.Rect(col*sell_size, row*sell_size, sell_size, sell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    def draw_score(self):
        score_text = f"Score: {self.score}  Level: {self.level}"
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(sell_size * sell_number - 120)
        score_y = int(sell_size * sell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)
    def increase_speed(self):
        self.speed = max(50, self.speed - 10)
        pygame.time.set_timer(SCREEN_UPDATE, self.speed)

pygame.init()
game_font=pygame.font.SysFont("'Verdana'", 25)
sell_size=40
sell_number=20
screen = pygame.display.set_mode((sell_number * sell_size, sell_number * sell_size))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

main_game=Main()

SCREEN_UPDATE=pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, main_game.speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction=Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction=Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction=Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction=Vector2(-1,0)
    screen.fill((193, 230, 115))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)