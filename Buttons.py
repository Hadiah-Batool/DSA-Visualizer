import pygame

WHITE = (255, 247, 228)
GREY  = (217, 200, 191)

class Button:
    def __init__(self, x, y, image_path, text, font_size, scale_x, scale_y):
        temp= pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(temp, (scale_x, scale_y))
        self.rect  = self.image.get_rect(topleft=(x, y))
        self.text = text
        # create a font at the right size
        self.font = pygame.font.Font(r'DSA_Visualizer\BlockBlueprint.ttf', font_size)
        self.text_surface = self.font.render(text, True, WHITE)
        self.text_rect   = self.text_surface.get_rect(center=self.rect.center)
        
    def is_hovered(self, event):
        if event.type == pygame.MOUSEMOTION and self.rect.collidepoint(event.pos):
            self.text_surface = self.font.render(self.text, True, GREY)
            return True
        else:
            self.text_surface = self.font.render(self.text, True, WHITE)
            return False

    def is_clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(event.pos))

    def display(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)
