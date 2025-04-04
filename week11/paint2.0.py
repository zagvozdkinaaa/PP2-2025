import pygame
import sys
import math

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

# buttons
buttons = {
    "brush": pygame.Rect(10, 10, 80, 30),
    "rect": pygame.Rect(100, 10, 80, 30),
    "circle": pygame.Rect(190, 10, 80, 30),
    "eraser": pygame.Rect(280, 10, 80, 30),
    "square": pygame.Rect(370, 10, 80, 30),
    "right_triangle": pygame.Rect(460, 10, 80, 30),
    "eq_triangle": pygame.Rect(550, 10, 80, 30),
    "rhombus": pygame.Rect(640, 10, 80, 30),
    "black": pygame.Rect(10, 50, 30, 30),
    "yellow": pygame.Rect(50, 50, 30, 30),
    "green": pygame.Rect(90, 50, 30, 30),
    "blue": pygame.Rect(130, 50, 30, 30),
    "increase": pygame.Rect(170, 50, 30, 30),
    "decrease": pygame.Rect(210, 50, 30, 30)
}

# draw buttons
def draw_buttons():
    for name, rect in buttons.items():
        if name in ["black", "yellow", "green", "blue"]:
            pygame.draw.rect(screen, eval(name.upper()), rect)
        else:
            pygame.draw.rect(screen, GRAY, rect)
    font = pygame.font.Font(None, 24)
    screen.blit(font.render("Brush", True, BLACK), (20, 15))
    screen.blit(font.render("Rect", True, BLACK), (115, 15))
    screen.blit(font.render("Circle", True, BLACK), (200, 15))
    screen.blit(font.render("Eraser", True, BLACK), (290, 15))
    screen.blit(font.render("Square", True, BLACK), (375, 15))
    screen.blit(font.render("R-Tri", True, BLACK), (465, 15))
    screen.blit(font.render("Eq-Tri", True, BLACK), (555, 15))
    screen.blit(font.render("Rhomb", True, BLACK), (645, 15))
    screen.blit(font.render("+", True, BLACK), (175, 55))
    screen.blit(font.render("-", True, BLACK), (215, 55))

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
                    if btn in ["brush", "rect", "circle", "eraser", "square", "right_triangle", "eq_triangle", "rhombus"]:
                        mode = btn
                    elif btn in ["black", "yellow", "green", "blue"]:
                        color = eval(btn.upper())
                    elif btn == "increase":
                        brush_size += 2
                    elif btn == "decrease" and brush_size > 2:
                        brush_size -= 2
                    break
            else:
                drawing = True
                last_pos = event.pos
                if mode not in ["brush", "eraser"]:
                    start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if start_pos:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                w = x2 - x1
                h = y2 - y1
                
                if mode == "rect":
                    pygame.draw.rect(screen, color, (x1, y1, w, h), brush_size)
                elif mode == "circle":
                    radius = int(((w)**2 + (h)**2)**0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, brush_size)
                elif mode == "square":
                    side = min(abs(w), abs(h))
                    pygame.draw.rect(screen, color, (x1, y1, side * (1 if w >= 0 else -1), side * (1 if h >= 0 else -1)), brush_size)
                elif mode == "right_triangle":
                    points = [start_pos, (x1, y2), (x2, y2)]
                    pygame.draw.polygon(screen, color, points, brush_size)
                elif mode == "eq_triangle":
                    height = abs(h)
                    points = [((x1 + x2) // 2, y1), (x1, y2), (x2, y2)]
                    pygame.draw.polygon(screen, color, points, brush_size)
                elif mode == "rhombus":
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    dx = abs(w) // 2
                    dy = abs(h) // 2
                    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                    pygame.draw.polygon(screen, color, points, brush_size)
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