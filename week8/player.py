import pygame
import os 

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (196, 59, 11)
font = pygame.font.Font(None, 30)

background = pygame.image.load("/Users/zagvozdkinaaa/PP2/week8/media/cassette.tiff") 
background = pygame.transform.scale(background, (500, 300)) 

playlist=["/Users/zagvozdkinaaa/PP2/week8/media/track1.mp3", "/Users/zagvozdkinaaa/PP2/week8/media/track2.mp3", "/Users/zagvozdkinaaa/PP2/week8/media/track3.mp3"]
current_track=0
paused=False

def play_track():
    global paused
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    paused=False

buttons = {
"prev": pygame.Rect(70, 230, 80, 50),
"play": pygame.Rect(175, 230, 160, 50),
"next": pygame.Rect(360, 230, 80, 50),
}

play_track()

running = True
while running:
    screen.blit(background, (0, 0))
    track_name = os.path.basename(playlist[current_track])
    track_text = font.render(f"Playing: {track_name}", True, BLACK)
    screen.blit(track_text, (70, 50))

    for key, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)

    screen.blit(font.render("Prev", True, WHITE), (buttons["prev"].x + 20, buttons["prev"].y + 10))
    screen.blit(font.render("Play/Pause", True, WHITE), (buttons["play"].x + 25, buttons["play"].y + 10))
    screen.blit(font.render("Next", True, WHITE), (buttons["next"].x + 20, buttons["next"].y + 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["play"].collidepoint(event.pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
            elif buttons["next"].collidepoint(event.pos):  
                current_track = (current_track + 1) % len(playlist)
                play_track()
            elif buttons["prev"].collidepoint(event.pos): 
                current_track = (current_track - 1) % len(playlist)
                play_track()

    pygame.display.flip()

pygame.quit()
