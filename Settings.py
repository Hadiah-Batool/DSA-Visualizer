import pygame
pygame.init()
from UIProperties import *
from Buttons import Button

class CheckBox:
    def __init__(self, x, y):
        self.size=50
        self.Rect=pygame.Rect(x, y, self.size, self.size)
        self.is_Clicked= False
    def Handle_Collision(self, event):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Rect.collidepoint(event.pos):  # Check if click is inside checkbox
                        self.is_Clicked = not self.is_Clicked   # Toggle state


    def Display(self, screen):
         pygame.draw.rect(screen, WHITE, self.Rect, 2)  
         if self.is_Clicked:
            # Calculate key points relative to the checkbox rectangle
            start_point = (self.Rect.x + int(self.size * 0.15), self.Rect.y + int(self.size * 0.5))
            mid_point = (self.Rect.x + int(self.size * 0.4), self.Rect.y + int(self.size * 0.8))
            end_point = (self.Rect.x + int(self.size * 0.85), self.Rect.y + int(self.size * 0.2))

            # Draw the first segment of the checkmark (the short part)
            pygame.draw.line(screen, GREEN, start_point, mid_point, 5)

            # Draw the second segment of the checkmark (the long part)
            pygame.draw.line(screen, GREEN, mid_point, end_point, 5)


class Setting_Object:
     def __init__(self):
          self.Grid_Box= CheckBox(500, 200)
          self.Bg_Music_Box= CheckBox(500, 300)
          self.Color_Mode_Box= CheckBox(500, 400)
          self.OK_Button= Button(500, 450, r'DSA_Visualizer\B_Pink.png', "OK", 48, 200, 100)
     def Handle_Events(self, event):
          
          self.Grid_Box.Handle_Collision(event)
          self.Bg_Music_Box.Handle_Collision(event)
          self.Color_Mode_Box.Handle_Collision(event)
          self.OK_Button.is_hovered(event)
          if self.OK_Button.is_clicked(event):
               print("OK Button Clicked")
               return True
          
          else:
               return False
     def Display(self, screen):
          setting_txt= "Settings"
          GR_Txt= "Grid"
          BG_Txt= "Background Music"
          CM_Txt= "!Light Mode"

          text1= FONT_S2.render(GR_Txt, True, WHITE)
          text2= FONT_S2.render(BG_Txt, True, WHITE)
          text3= FONT_S2.render(CM_Txt, True, WHITE)
          text4= FONT_S1.render(setting_txt, True, WHITE, PURPLE)
          screen.blit(text1, (100, self.Grid_Box.Rect.y ))
          screen.blit(text2, (100, self.Bg_Music_Box.Rect.y ))
          screen.blit(text3, (100, self.Color_Mode_Box.Rect.y ))
          screen.blit(text4, (300, 50 ))   
          self.Grid_Box.Display(screen)
          self.Bg_Music_Box.Display(screen)
          self.Color_Mode_Box.Display(screen)
          self.OK_Button.display(screen)
