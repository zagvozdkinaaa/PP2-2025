import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (62, 88, 148)
GREEN = (152, 186, 87)
YELLOW = (224, 191, 101)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')

screen.fill(WHITE)
clock = pygame.time.Clock()

drawing = False
last_pos = None
color = BLACK
brush_size = 5
mode = "brush"
start_pos = None

buttons = {
    "brush": pygame.Rect(10, 10, 80, 30),
    "rect": pygame.Rect(100, 10, 80, 30),
    "circle": pygame.Rect(190, 10, 80, 30),
    "eraser": pygame.Rect(280, 10, 80, 30),
    "black": pygame.Rect(370, 10, 30, 30),
    "yellow": pygame.Rect(410, 10, 30, 30),
    "green": pygame.Rect(450, 10, 30, 30),
    "blue": pygame.Rect(490, 10, 30, 30),
    "increase": pygame.Rect(530, 10, 30, 30),
    "decrease": pygame.Rect(570, 10, 30, 30)
}

def draw_buttons():
    pygame.draw.rect(screen, GRAY, buttons["brush"])
    pygame.draw.rect(screen, GRAY, buttons["rect"])
    pygame.draw.rect(screen, GRAY, buttons["circle"])
    pygame.draw.rect(screen, GRAY, buttons["eraser"])
    pygame.draw.rect(screen, BLACK, buttons["black"])
    pygame.draw.rect(screen, YELLOW, buttons["yellow"])
    pygame.draw.rect(screen, GREEN, buttons["green"])
    pygame.draw.rect(screen, BLUE, buttons["blue"])
    pygame.draw.rect(screen, GRAY, buttons["increase"])
    pygame.draw.rect(screen, GRAY, buttons["decrease"])
    
    font = pygame.font.Font(None, 24)
    screen.blit(font.render("Brush", True, BLACK), (20, 15))
    screen.blit(font.render("Rect", True, BLACK), (115, 15))
    screen.blit(font.render("Circle", True, BLACK), (200, 15))
    screen.blit(font.render("Eraser", True, BLACK), (290, 15))
    screen.blit(font.render("+", True, BLACK), (540, 15))
    screen.blit(font.render("-", True, BLACK), (580, 15))

draw_buttons()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for btn, rect in buttons.items():
                if rect.collidepoint(x, y):
                    if btn in ["brush", "rect", "circle", "eraser"]:
                        mode = btn
                    elif btn == "black":
                        color = BLACK
                    elif btn == "yellow":
                        color = YELLOW
                    elif btn == "green":
                        color = GREEN
                    elif btn == "blue":
                        color = BLUE
                    elif btn == "increase":
                        brush_size += 2
                    elif btn == "decrease" and brush_size > 2:
                        brush_size -= 2
                    break
            else:
                drawing = True
                last_pos = event.pos
                if mode in ["rect", "circle"]:
                    start_pos = event.pos
        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rect" and start_pos:
                end_pos = event.pos
                pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), brush_size)
            elif mode == "circle" and start_pos:
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, radius, brush_size)
            start_pos = None
        
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.line(screen, color, last_pos, event.pos, brush_size)
                last_pos = event.pos
            elif mode == "eraser":
                if not any(rect.collidepoint(event.pos) for rect in buttons.values()):
                    pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size)
                    last_pos = event.pos
    
    draw_buttons()
    pygame.display.flip()
    clock.tick(60)
