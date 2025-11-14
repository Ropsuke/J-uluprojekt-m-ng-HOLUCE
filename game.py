import pygame
import sys
import os
# Algväärtustame pygame
pygame.init()

# Ekraani suurus
WIDTH, HEIGHT = 1800, 1120
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nupud + blur taust")

# Laeme taustapildi

# Nuppude definitsioonid
button_font = pygame.font.Font(None, 60)
buttons = [
    {"rect": pygame.Rect(WIDTH/2 -200, 350, 400, 100), "text": "New Game"},
    {"rect": pygame.Rect(WIDTH/2 -200, 480, 400, 100), "text": "Continue"},
    {"rect": pygame.Rect(WIDTH/2 -200, 610, 400, 100), "text": "Settings"},
    {"rect": pygame.Rect(WIDTH/2 -200, 740, 400, 100), "text": "Game info"},
]

# Värvid
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

# Põhiline loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for b in buttons:
                if b["rect"].collidepoint(mouse_pos):
                    print(b["text"], "vajutatud!")

    # Joonistame bluritud tausta

    # Joonistame nupud
    for b in buttons:
        pygame.draw.rect(screen, RED, b["rect"])
        text_surface = button_font.render(b["text"], True, WHITE)
        # Teksti keskele
        text_rect = text_surface.get_rect(center=b["rect"].center)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()