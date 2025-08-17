import pygame, math
pygame.init()
from Arrays import Array
from Linked_Lists import LinkedList
from UIProperties import *
from Buttons import Button  
LEFT_MARGIN, TOP_MARGIN = 20, 200
SPACING = 5
CELL_HEIGHT = 100
class Queue:
    def __init__(self):

        self.Buttons=[Button(150, 150, r'DSA_Visualizer\B_Pink.png', " Array Based Queue", 42, 550, 250),
                      Button(150, 350, r'DSA_Visualizer\B_Sk_Blu.png', "   Linked List Based Queue", 42, 550, 250)]
    def display(self, screen):
        txt="Choose an implementation approach."
        screen.blit(FONT_S2.render(txt, True, WHITE, PURPLE),(10, 50))
        for b in self.Buttons:
            b.display(screen)
            
class Queue_Array_Based:
    def __init__(self):
        self.array = Array()
        # pick a capacity (e.g., 12) and initialize the visual/values
        self.array.size = 12
        self.array.values = [None] * self.array.size
        self.array.current_Count = 0
        self.array.InitializeRects()

        self.Rear = 0
        self.Front = 0

        self.top_Rect   = pygame.Rect(150, 150, 80, 80)
        self.Front_rect = pygame.Rect(50, 150, 80, 80)

        # (use consistent path separators)
        self.array.interface_Btns = [
            Button(150, 50,  r'DSA_Visualizer\B_Red.png', "Enqueue", 32, 200, 100),
            Button(350, 50,  r'DSA_Visualizer\B_Red.png', "Dequeue", 32, 200, 100),
            Button(550, 50,  r'DSA_Visualizer\B_Red.png', "Clear",   32, 200, 100),
        ]
        self.array.top_Margin = 350

    def is_empty(self):
        return self.array.current_Count == 0

    def is_full(self):
        return self.array.current_Count == self.array.size

    def Enqueue(self, screen):
        if self.is_full():
            self._blit_message(screen, "Queue is full!", D_RED)
            return
        # write at Rear, highlight, advance
        self.array.values[self.Rear] = self.array.val
        self.array.highlight_index = self.Rear
        self.array.highlight_start = pygame.time.get_ticks()

        self.Rear = (self.Rear + 1) % self.array.size
        self.array.current_Count += 1
    def _blit_message(self, screen, msg, color, y=520):
        # reuse the same pattern you used in BST
        text = FONT_S1.render(msg, True, color)
        pad = 10
        r = text.get_rect()
        bg = pygame.Rect((SCREEN_WIDTH - r.width)//2 - pad, y - pad,
                         r.width + 2*pad, r.height + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, color, bg, 2)
        screen.blit(text, ((SCREEN_WIDTH - r.width)//2, y))
    def Display(self, screen):
        txt_Surface=FONT_S1.render(str(self.Rear), True, WHITE)
        heading="Rear"
        heading_Surface= FONT_S2.render(heading, True, WHITE)
        pygame.draw.rect(screen, L_GREEN, self.top_Rect, 3)

        txt_Surface1=FONT_S1.render(str(self.Front), True, WHITE)
        heading1="Front"
        heading_Surface1= FONT_S2.render(heading1, True, WHITE)
        pygame.draw.rect(screen, L_GREEN, self.Front_rect, 3)

        self.array.drawInterface(screen)
        screen.blit(txt_Surface1, (70, 170))
        screen.blit(heading_Surface1, (0, 240))

        screen.blit(txt_Surface, (170, 170))
        screen.blit(heading_Surface, ( 120, 240))
    def Dequeue(self, screen):
        if self.is_empty():
            self._blit_message(screen, "Queue is empty!", D_RED)
            return
      
        self.array.highlight_index = self.Front
        self.array.highlight_start = pygame.time.get_ticks()

        self.array.values[self.Front] = None
        self.Front = (self.Front + 1) % self.array.size
        self.array.current_Count -= 1

    def Clear(self):
        self.Front = 0
        self.Rear = 0
        self.array.Clear() 

class Queue_LinkedList_Based(LinkedList):
    def __init__(self):
        super().__init__()
        self.indx_Circle=None
        self.indx_Rad=50
        self.interface_Btns=[
            Button(150, 0, r'DSA_Visualizer/B_Red.png', "Enqueue", 32, 200, 100),
            Button(350, 0, r'DSA_Visualizer/B_Red.png', "Dequeue", 32, 200, 100),
            Button(550, 0, r'DSA_Visualizer/B_Red.png', "Clear",32, 200, 100)
        ]
        #1 boxes for  value 
        self.input_box= pygame.Rect(10, 10, 140, 80)
        self.Head_Box = pygame.Rect(10, 120, 140, 80)
        self.Tail_Box = pygame.Rect(600, 420, 140, 80)

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

        pygame.draw.rect(screen, D_GREEN, self.Head_Box, 3)
        pygame.draw.rect(screen, D_GREEN, self.Tail_Box, 3)
        Head_Surface= FONT_S2.render("Head", True, WHITE)
        Tail_Surface= FONT_S2.render("Tail", True, WHITE)
        if(len(self.values)==0):
            pygame.draw.line(screen, D_GREEN, (10, 120), (150, 195), 4)
        elif(len(self.nodes)!=0):
            x1, y1= 80, 160
            x2, y2= self.nodes[0].pos
            start = (x1, y1)
            end = (x2, y2 - self.nodes[0].radius)
            pygame.draw.line(screen, L_RED, start, end, 3)
            angle = math.atan2(y2 - y1, x2 - x1)
            arrow_size = 12
            left = (end[0] - arrow_size * math.cos(angle - math.pi/6),
                end[1] - arrow_size * math.sin(angle - math.pi/6))
            right = (end[0] - arrow_size * math.cos(angle + math.pi/6),
                 end[1] - arrow_size * math.sin(angle + math.pi/6))
            pygame.draw.polygon(screen, L_RED, [end, left, right])



        if(len(self.values)==0):
            pygame.draw.line(screen, D_GREEN, (600, 420), (740, 495), 4)
        elif(len(self.nodes)!=0):
            x1, y1= 670, 515
            x= (len(self.nodes))-1
            x2, y2= self.nodes[x].pos
            start = (x1, y1)
            end = (x2, y2 + self.nodes[x].radius)
            pygame.draw.line(screen, L_RED, start, end, 3)
            angle = math.atan2(y2 - y1, x2 - x1)
            arrow_size = 12
            left = (end[0] - arrow_size * math.cos(angle - math.pi/6),
                end[1] - arrow_size * math.sin(angle - math.pi/6))
            right = (end[0] - arrow_size * math.cos(angle + math.pi/6),
                 end[1] - arrow_size * math.sin(angle + math.pi/6))
            pygame.draw.polygon(screen, L_RED, [end, left, right])

        screen.blit(Head_Surface, (self.Head_Box.x, self.Head_Box.y+75))
        screen.blit(Tail_Surface, (self.Tail_Box.x, self.Tail_Box.y+75))
        
    def Clear(self):
        self.nodes = []
        self.values = []        





