import pygame, math
pygame.init()
from Arrays import Array
from UIProperties import *
from Buttons import Button  
LEFT_MARGIN, TOP_MARGIN = 20, 200
SPACING = 5
CELL_HEIGHT = 100
class stack:
    def __init__(self):

        self.Buttons=[Button(150, 150, r'DSA_Visualizer\B_Pink.png', " Array Based Stack", 42, 500, 250),
                      Button(150, 350, r'DSA_Visualizer\B_Sk_Blu.png', "  Linked List Based Stack", 42, 500, 250)]
    def display(self, screen):
        txt="Choose an implementation approach."
        screen.blit(FONT_S2.render(txt, True, WHITE, PURPLE),(10, 50))
        for b in self.Buttons:
            b.display(screen)
            
class Stack_Array_Based:
    def __init__(self):
        self.array= Array()
        self.top_idx= self.array.current_Count
        self.top_Rect = pygame.Rect(550, 150, 80, 80)
        self.array.interface_Btns= [ Button(150, 50, r'DSA_Visualizer/B_Red.png', "Push", 32, 200, 100),
                                Button(350, 50, r'DSA_Visualizer/B_Red.png', "Pop", 32, 200, 100),
                                Button(550, 50, r'DSA_Visualizer/B_Red.png',"Clear", 32, 200, 100) 

        ]
        self.array.top_Margin=350


    def Display(self, screen):
        self.top_idx= str(self.array.current_Count)
        txt_Surface=FONT_S1.render(self.top_idx, True, WHITE)
        heading="Top_Index"
        heading_Surafce= FONT_S2.render(heading, True, WHITE)
        pygame.draw.rect(screen, L_GREEN, self.top_Rect, 3)
        self.array.drawInterface(screen)
        screen.blit(txt_Surface, (570, 170))
        screen.blit(heading_Surafce, ( 500, 240))





