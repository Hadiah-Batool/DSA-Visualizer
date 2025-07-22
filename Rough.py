import pygame, sys, math

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# colors & font
GREY  = (217, 200, 191)
WHITE = (255, 247, 228)
DED_GREEN =(179, 227, 218)
PURPLE= (176,169, 228)
BLACK_1=(40, 40, 46)
MAROON=(108, 86, 113)
L_GREEN=(176, 235, 147)
D_GREEN=(135, 168,137 )
FONT_S1 = pygame.font.Font(r'DSA_Visualizer\BlockBlueprint.ttf', 75)
FONT_S2 = pygame.font.Font(r'DSA_Visualizer\BlockBlueprint.ttf', 40)
temp= pygame.image.load(r'D:\Hadia\Python\DSA_Visualizer\HomeScreen_Bg.png')
Bg_Start= pygame.transform.smoothscale(temp, (900, 600))
Bg_Rect= Bg_Start.get_rect(center=(450, 300))

def title_screen():
    prompt = "Press any key to continue"
    title  = "Welcome to DSA Visualizer"
    t0     = pygame.time.get_ticks()
    
    while True:
        for event in pygame.event.get():
            if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return            # any key/mouse → exit title screen
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        screen.fill((30, 30, 30))

        # --- draw the static title ---
        surf_title = FONT_S1.render(title, True, WHITE, L_GREEN)
        rect_title = surf_title.get_rect(center=(WIDTH//2, HEIGHT//3))
        screen.blit(Bg_Start, Bg_Rect)
        screen.blit(surf_title, rect_title)

        
        # Option A: smooth sinusoidal jitter
        elapsed = pygame.time.get_ticks() - t0
        dx = 5 * math.sin(elapsed * 0.008)
        dy = 3 * math.sin(elapsed * 0.012)
        surf = FONT_S2.render(prompt, True, WHITE, PURPLE)
        rect = surf.get_rect(center=(WIDTH//2 + dx, HEIGHT*2//3 + dy))
        screen.blit(surf, rect)

        pygame.display.flip()
        clock.tick(60)

def main_game():
    # your existing game‐loop here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        screen.fill((0,0,0))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    
    title_screen()
    main_game()
