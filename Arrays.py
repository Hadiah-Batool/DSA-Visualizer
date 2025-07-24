import pygame, sys, math
from UIProperties import *
pygame.init()
from Data_Structures import *
from Buttons import Button
LEFT_MARGIN, TOP_MARGIN = 20, 200
SPACING = 5
CELL_HEIGHT = 100
class Array (DataStructure):
    def __init__(self):
        super().__init__()
        self.values = []
        self.dataType_Btns = [
            Button(50, 200, r'DSA_Visualizer\B_Pink.png', "Integer", 32, 200, 100),
            Button(300, 200, r'DSA_Visualizer\B_Purp.png', "Float", 32, 200, 100),
            Button(50, 300, r'DSA_Visualizer\B_DedBlu.png', "String", 32, 200, 100),
            Button(300, 300, r'DSA_Visualizer\B_Green.png', "Char", 32, 200, 100)
        ]
        self.dataType = None
        self.input_box_element= pygame.Rect(20, 80, 140, 40)
        self.input_box    = pygame.Rect(20, 80, 140, 50)
        self.color_active  = L_GREEN
        self.color_inactive= DED_GREEN
        self.color         = self.color_inactive
        #Boolean to track if the input box is active
        self.active1        = False
        self.active2        = False
        # Initialize the text(for values size) and input text(val)
        self.text          =''
        self.val=0
        self.input_text    =''
        self.current_Count = 0
        self.size=0
        self.InpComplete = False
        self.highlight_index=None
        self.highlight_start = 0
        self.interval=1500
        #values rects
        self.rects = []
        self.interface_Btns = [ Button(150, 50, r'DSA_Visualizer/B_Red.png', "Insert", 32, 200, 100),
                                Button(350, 50, r'DSA_Visualizer/B_Red.png', "Delete", 32, 200, 100),
                                Button(550, 50, r'DSA_Visualizer/B_Red.png',"Clear", 32, 200, 100) 

        ]
        self.data_Type_dict = {"Integer": int,
                             "Float": float,
                             "String": str,
                             "Char": str}

    def AskUser(self,event) -> None:
        """ Ask the user for the size of the values"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active1 = not self.active1
            else:
                self.active1 = False
        if self.active1:
            self.color = self.color_active
        else:
            self.color = self.color_inactive
        if event.type== pygame.KEYDOWN:
            if self.active1:
                if event.key == pygame.K_RETURN:
                    try:
                        size = int(self.text)
                        if size < 0:
                            raise ValueError("Size must be a non-negative integer.")
                        self.size = size
                        self.values = [None] * size  # Initialize the values with None
                        print(f"values size set to: {size}")
                        print("Initializing Shi")
                        self.InitializeRects()
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    def Take_input(self, event):
        """ Take input from the user for inserting or deleting an element"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box_element.collidepoint(event.pos):
                self.active2 = not self.active2
            else:
                self.active2 = False
        if self.active2:
            self.color = self.color_active
        if event.type == pygame.KEYDOWN:
            if self.active2:
                if event.key == pygame.K_RETURN:
                        self.val = self.data_Type_dict[self.dataType](self.input_text)
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode
            
            print(f"Input text: {self.input_text}")
            self.val = self.data_Type_dict[self.dataType](self.input_text)

    def insert(self, data: DataType) -> None:
    # only called when user clicks your “Insert” Button
        if (self.size) > self.current_Count:
            self.values[self.current_Count] = self.data_Type_dict[self.dataType](self.input_text)
            self.input_text = ''
            self.highlight_index = self.current_Count 
            self.current_Count += 1
            
            #Print the values
            for i, val in enumerate(self.values):
                print(f"values[{i}] = {val}")
            # start highlight animation…
            
            self.highlight_start = pygame.time.get_ticks()

            


    def delete(self, data: DataType) -> None:
        # Delete data from the values
        print(f"Deleting {data} from the values")
        self.values.remove(data)
        

    def Draw(self, screen) -> None:
        # draw the prompt
        txt = "Enter the size of the values:(Press Enter to confirm)"
        screen.blit(FONT_S3.render(txt, True, WHITE), (10, 20))
        # draw the current text
        txt_surf = FONT_S3.render(self.text, True, WHITE)
        self.input_box.w = max(200, txt_surf.get_width()+10)
        screen.blit(txt_surf, (self.input_box.x+5, self.input_box.y+5))
         # draw the box
        pygame.draw.rect(screen, self.color, self.input_box, 2)
        txt2 = "Choose the data type:"
        screen.blit(FONT_S2.render(txt2, True, WHITE), (10, 150))

    def drawInterface(self, screen) :
        if(self.text ==''):
            self.Draw(screen)
            return
        else:
         txt="Enter an element to insert/delete:"
         screen.blit(FONT_S2.render(txt, True, WHITE), (25, 10))
         txt_surf = FONT_S3.render(self.input_text, True, WHITE)
         screen.blit(txt_surf, (self.input_box_element.x+5, self.input_box_element.y+5))
         pygame.draw.rect(screen, self.color, self.input_box_element, 2)
         for btn in self.interface_Btns:
             btn.display(screen)
        now = pygame.time.get_ticks()
        i=0
        for i, rect in enumerate(self.rects):
            
            if (i == self.highlight_index and
                now - self.highlight_start < self.interval):
                color = D_RED
            else:
                color = D_GREEN

            pygame.draw.rect(screen, color, rect, 4)

            # draw stored value (if any) centered
            if self.values[i] is not None:
                txt = FONT_S2.render(str(self.values[i]), True, WHITE)
                txt_rect = txt.get_rect(center=rect.center)
                screen.blit(txt, txt_rect)

        # end the highlight after the duration
        if self.highlight_index is not None and \
           now - self.highlight_start >= self.interval:
            self.highlight_index = None
    def InitializeRects(self):
        """ Initialize the rects for the values elements"""
        avail_width = SCREEN_WIDTH - 2*LEFT_MARGIN
        cell_w = (avail_width - (self.size-1)*SPACING) / self.size
        self.rects = [
            pygame.Rect(
                LEFT_MARGIN + i*(cell_w+SPACING),
                TOP_MARGIN,
                cell_w,
                CELL_HEIGHT
            )
            for i in range(self.size)
        ]  