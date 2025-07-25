import pygame, math
pygame.init()
from Data_Structures import *
from UIProperties import *
from Buttons import Button  
class LinkedList(DataStructure):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0
        self.nodes = []
        #1 boxes for  value 
        self.input_box= pygame.Rect(200, 100, 140, 50)   
        #input index box
        self.index_input_box = pygame.Rect(500, 100, 100, 50)
        self.color_active = L_GREEN
        self.color_inactive = DED_GREEN
        self.color = self.color_inactive
        self.active1 = False # for value input
        self.active2 = False # for index input
        self.text = ''
        self.val = None
        self.idx = None
        self.idx_txt=''
        self.In_Indx = False
        self.inDisplayBoxes=False

        self.interface_Btns = [
            Button(5, 0, r'DSA_Visualizer/B_Red.png', "Insert", 28, 160, 80),
            Button(5, 50, r'DSA_Visualizer/B_Red.png', "Delete", 28, 160, 80),
            Button(5, 100, r'DSA_Visualizer/B_Red.png', "Search", 28, 160, 80)
        ]

        self.Go_Button= Button(500, 250, r'DSA_Visualizer\B_Sq.png', "GO", 32, 100, 100)
        self.data_Type_dict = {"Integer": int,
                             "Float": float,
                             "String": str,
                             "Char": str}
        self.dataType_Btns = [
            Button(50, 100, r'DSA_Visualizer\B_Pink.png', "Integer", 64, 300, 150),
            Button(400, 100, r'DSA_Visualizer\B_Purp.png', "Float", 64, 300, 150),
            Button(50, 250, r'DSA_Visualizer\B_DedBlu.png', "String", 64, 300, 150),
            Button(400, 250, r'DSA_Visualizer\B_Green.png', "Char", 64, 300, 150)
        ]
        self.Where_To_Buttons = [Button(150, 10, r'DSA_Visualizer\B_Ded_G_Sq.png', "At Head", 28,200, 70),
                                 Button(300, 10, r'DSA_Visualizer\B_Ded_G_Sq.png', "At Tail", 28, 200, 70),
                                 Button(450, 10, r'DSA_Visualizer\B_Ded_G_Sq.png', "At Index", 28, 200, 70)]

    def AskUser(self, screen) -> None:
        txt="Please select a data type:"
        screen.blit(FONT_S1.render(txt, True, WHITE, DED_GREEN), (20, 20))
        for btn in self.dataType_Btns:
            btn.display(screen)       
    def insert(self, data: DataType) -> None:
        print(f"Inserting {data} into the linked list.")
    def delete(self, data: DataType) -> None:
        print(f"Deleting {data} from the linked list.")
    def Draw(self, screen) -> None:
        print("Drawing the linked list.")
    def Draw_Buttons(self, screen):
        for btn in self.interface_Btns:
            btn.display(screen)
    def HandleInput(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active1 = True
            else:
                self.active1 = False
            if self.index_input_box.collidepoint(event.pos):
                self.In_Indx = True
                self.active2 = True
            else:
                self.active2 = False
                self.In_Indx = False

        if event.type == pygame.KEYDOWN:
            if self.active1:
                if event.key == pygame.K_RETURN:
                    self.active1 = False
                    try:
                        self.val = self.data_Type_dict[self.dataType](self.text)
                        print(f"Value set to: {self.val}")
                    except ValueError as e:
                        print(f"Invalid value: {e}")
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
            if self.In_Indx and self.active2:
                if event.key == pygame.K_RETURN:
                    self.active2 = False
                    try:
                        self.idx = int(self.idx_txt)
                        print(f"Index set to: {self.idx}")
                    except ValueError as e:
                        print(f"Invalid index: {e}")
                    self.idx_txt = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.idx_txt = self.idx_txt[:-1]
                else:
                    self.idx_txt += event.unicode
    def Draw_Where_To_Buttons(self, screen):
        """ Draw the Where To buttons"""
        for b in self.Where_To_Buttons:
            b.display(screen)
    def Draw_Inp_Box(self, screen):
        """ Draw the input box for value"""
        Ins1="Press Enter "
        Ins2="to confirm"
        Ins3= "input"
        Ins1_surface = FONT_S3.render(Ins1, True, WHITE)
        Ins2_surface = FONT_S3.render(Ins2, True, WHITE)
        Ins3_surface = FONT_S3.render(Ins3, True, WHITE)
        screen.blit(Ins1_surface, (630, 10))
        screen.blit(Ins2_surface, (630, 30))
        screen.blit(Ins3_surface, (630, 50))
        r= pygame.Rect(620, 10, 175, 80)
        pygame.draw.rect(screen, YELLOW, r, 3)
        """ Draw the input box for value"""
        if self.active1:
            self.color = self.color_active
        else:
            self.color = self.color_inactive
        y="Input Value"
        pygame.draw.rect(screen, self.color, self.input_box, 3)
        txt_surface = FONT_S2.render(self.text, True, WHITE)
        y_surface = FONT_S4.render(y, True, WHITE)
        screen.blit(y_surface, (self.input_box.x, self.input_box.y + 50))
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        if self.active1:
            pygame.draw.rect(screen, self.color_active, self.input_box, 3)
        """ Draw the input box for index if active"""
        clr=None

        if self.active2:
            clr = self.color_active
        else:
            clr = self.color_inactive
        if self.In_Indx:
            """ Draw the input box for index"""
            x="Input Index"
            pygame.draw.rect(screen, clr, self.index_input_box, 3)
            idx_surface = FONT_S2.render(self.idx_txt, True, WHITE)
            x_surface = FONT_S4.render(x, True, WHITE)
            screen.blit(x_surface, (self.index_input_box.x , self.index_input_box.y + 50))
            screen.blit(idx_surface, (self.index_input_box.x + 5, self.index_input_box.y + 5))
        if self.In_Indx:
            pygame.draw.rect(screen, clr, self.index_input_box, 3)
