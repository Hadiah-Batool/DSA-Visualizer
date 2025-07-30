import pygame, math
pygame.init()
from Arrays import Array
from Linked_Lists import LinkedList
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


class Stack_LinkedList_Based(LinkedList):
    def __init__(self):
        super().__init__()
        self.indx_Circle=None
        self.indx_Rad=50
        self.interface_Btns=[
            Button(150, 0, r'DSA_Visualizer/B_Red.png', "Push", 32, 200, 100),
            Button(350, 0, r'DSA_Visualizer/B_Red.png', "Pop", 32, 200, 100),
            Button(550, 0, r'DSA_Visualizer/B_Red.png', "Clear",32, 200, 100)
        ]
        #1 boxes for  value 
        self.input_box= pygame.Rect(0, 40, 140, 80)
        self.top_Box = pygame.Rect(620, 100, 175, 100)

    def HandleInput(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active1 = True
            else:
                self.active1 = False


        if event.type == pygame.KEYDOWN:
            if self.active1:
                if event.key == pygame.K_RETURN:
                    
                    try:
                        self.val = self.data_Type_dict[self.dataType](self.text)
                        print(f"Value set to: {self.val}")
                    except ValueError as e:
                        print(f"Invalid value: {e}")
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    def Draw_Inp_Box(self, screen):
        
        """ Draw the input box for value"""
        Ins1="Press Enter "
        Ins2="to confirm"
        Ins3= "input"
        Ins1_surface = FONT_S3.render(Ins1, True, WHITE)
        Ins2_surface = FONT_S3.render(Ins2, True, WHITE)
        Ins3_surface = FONT_S3.render(Ins3, True, WHITE)
        screen.blit(Ins1_surface, (630, 110))
        screen.blit(Ins2_surface, (630, 130))
        screen.blit(Ins3_surface, (630, 150))
        r= pygame.Rect(620, 100, 175, 100)
        pygame.draw.rect(screen, YELLOW, r, 3)
        """ Draw the input box for value"""
        if self.active1:
            self.color = self.color_active
        else:
            self.color = self.color_inactive
        y="Input Value"
        pygame.draw.rect(screen, self.color, self.input_box, 3)
        txt_surface = FONT_S2.render(self.text, True, WHITE)
        y_surface = FONT_S3.render(y, True, WHITE)
        screen.blit(y_surface, (self.input_box.x, self.input_box.y + 80))
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        if self.active1:
            pygame.draw.rect(screen, self.color_active, self.input_box, 3)
    def Clear(self):
        self.nodes = []
        self.values = []        





