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
        self.input_box= pygame.Rect(200, 80, 140, 50)   
        #input index box
        self.index_input_box = pygame.Rect(80, 80, 100, 50)
        self.color_active = L_GREEN
        self.color_inactive = DED_GREEN
        self.color = self.color_inactive
        self.active = False
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
                self.active = not self.active
            else:
                self.active = False
            if self.index_input_box.collidepoint(event.pos):
                self.In_Indx = not self.In_Indx
            else:
                self.In_Indx = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
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
            if self.In_Indx:
                if event.key == pygame.K_RETURN:
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
        pygame.draw.rect(screen, self.color, self.input_box, 2)
        txt_surface = FONT_S1.render(self.text, True, WHITE)
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        if self.active:
            pygame.draw.rect(screen, self.color_active, self.input_box, 2)
        if self.In_Indx:
            pygame.draw.rect(screen, self.color, self.index_input_box, 2)
            idx_surface = FONT_S1.render(self.idx_txt, True, WHITE)
            screen.blit(idx_surface, (self.index_input_box.x + 5, self.index_input_box.y + 5))
            if self.active:
                pygame.draw.rect(screen, self.color_active, self.index_input_box, 2)
