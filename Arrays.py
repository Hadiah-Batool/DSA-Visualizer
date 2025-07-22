import pygame, sys, math
from UIProperties import *
pygame.init()
from Data_Structures import *
from Buttons import Button
class Array (DataStructure):
    def __init__(self):
        super().__init__()
        self.array = []
        self.dataType_Btns = [
            Button(50, 200, r'DSA_Visualizer\B_Pink.png', "Integer", 32, 200, 100),
            Button(300, 200, r'DSA_Visualizer\B_Purp.png', "Float", 32, 200, 100),
            Button(50, 300, r'DSA_Visualizer\B_DedBlu.png', "String", 32, 200, 100),
            Button(300, 300, r'DSA_Visualizer\B_Green.png', "Char", 32, 200, 100)
        ]
        self.input_box     = pygame.Rect(20, 100, 140, 32)
        self.color_active  = L_GREEN
        self.color_inactive= DED_GREEN
        self.color         = self.color_inactive
        self.active        = False
        self.text          =''
    def AskUser(self,event) -> None:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_inactive
        if event.type== pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    try:
                        size = int(self.text)
                        print(f"Array size set to: {size}")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                   # self.text = ''  # Clear the input after setting size
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def insert(self, data: DataType) -> None:
        # Insert data into the array
        print(f"Inserting {data} into the array")
        self.array.append(data)

    def delete(self, data: DataType) -> None:
        # Delete data from the array
        print(f"Deleting {data} from the array")
        self.array.remove(data)
        

    def Draw(self, screen) -> None:
        # draw the prompt
        txt = "Enter the size of the array:"
        screen.blit(FONT_S2.render(txt, True, WHITE), (10, 20))
        # draw the current text
        txt_surf = FONT_S4.render(self.text, True, WHITE)
        self.input_box.w = max(200, txt_surf.get_width()+10)
        screen.blit(txt_surf, (self.input_box.x+5, self.input_box.y+5))
         # draw the box
        pygame.draw.rect(screen, self.color, self.input_box, 2)
        txt2 = "Enter the data type:"
        screen.blit(FONT_S2.render(txt2, True, WHITE), (10, 150))
        # draw your data‐type buttons
        for btn in self.dataType_Btns:
            btn.display(screen)
