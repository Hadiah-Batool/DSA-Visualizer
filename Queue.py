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

        self.Buttons=[Button(150, 150, r'DSA_Visualizer\B_Pink.png', " Array Based Queue", 42, 500, 250),
                      Button(150, 350, r'DSA_Visualizer\B_Sk_Blu.png', "  Linked List Based Queue", 42, 500, 250)]
    def display(self, screen):
        txt="Choose an implementation approach."
        screen.blit(FONT_S2.render(txt, True, WHITE, PURPLE),(10, 50))
        for b in self.Buttons:
            b.display(screen)
            
class Queue_Array_Based:
    def __init__(self):
        self.array= Array()
        self.Rear= 0
        self.Front=0
        self.top_Rect = pygame.Rect(250, 150, 80, 80)
        self.Front_rect= pygame.Rect(50, 150, 80, 80)
        self.array.interface_Btns= [ Button(150, 50, r'DSA_Visualizer/B_Red.png', "Enqueue", 32, 200, 100),
                                Button(350, 50, r'DSA_Visualizer/B_Red.png', "Dequeue", 32, 200, 100),
                                Button(550, 50, r'DSA_Visualizer/B_Red.png',"Clear", 32, 200, 100) 

        ]
        self.array.top_Margin=350


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

        screen.blit(txt_Surface, (270, 170))
        screen.blit(heading_Surface, ( 220, 240))
    def Dequeue(self):
        if self.array.current_Count == 0:
            print("Queue is empty!")
            return
        else:
            self.array.delete(self.array.values[self.Front])
            self.Front= (self.Front+1)%self.array.size

    def Enqueue(self):
      if self.array.current_Count == self.array.size:
            print("Queue is full!")
            return
      else:
          self.array.highlight_index= self.Rear
          self.array.highlight_start = pygame.time.get_ticks()
          self.array.values[self.Rear]= self.array.val
          self.Rear = (self.Rear + 1) % self.array.size
          self.array.current_Count += 1
    def Clear(self):
        self.Front=0
        self.Rear=0
        self.array.Clear()
class Queue_LinkedList_Based(LinkedList):
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
        self.input_box= pygame.Rect(10, 10, 140, 80)
        self.top_Box = pygame.Rect(10, 120, 140, 80)

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

        pygame.draw.rect(screen, D_GREEN, self.top_Box, 3)
        Top_Surface= FONT_S2.render("Top", True, WHITE)
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

        screen.blit(Top_Surface, (self.top_Box.x, self.top_Box.y+75))
    def Clear(self):
        self.nodes = []
        self.values = []        





