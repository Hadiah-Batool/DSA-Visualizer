import pygame, math
pygame.init()
from Data_Structures import *
from UIProperties import *
from Buttons import Button  
class AnimatedNode:
    def __init__(self):
        self.value=0
        self.pos=(0, 0)
        self.color= WHITE
        self.radius = 20
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S4.render(str(self.value), True, WHITE)
        screen.blit(text_surface, (self.pos[0] - text_surface.get_width() // 2, self.pos[1] - text_surface.get_height() // 2))

class LinkedList:
    def __init__(self):
        # super().__init__()
        self.head = None
        self.tail = None
        self.size = 0
        self.nodes = []
        self.values = []
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
        self.dataType=''
        self.Screen_Height=800
        self.in_Search=False

        self.interface_Btns = [
            Button(5, 0, r'DSA_Visualizer\B_Red.png', "Insert", 28, 160, 80),
            Button(5, 60, r'DSA_Visualizer\B_Red.png', "Delete", 28, 160, 80),
            Button(5, 120, r'DSA_Visualizer\B_Red.png', "Search", 28, 160, 80)
        ]

        
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

    def Calculate_Node_Positions(self):
        """Update positions and values without destroying node objects/colors."""
        n = len(self.values)

        # Grow/shrink node list but preserve existing node objects (and their colors)
        while len(self.nodes) < n:
            self.nodes.append(AnimatedNode())
        while len(self.nodes) > n:
            self.nodes.pop()

        # Layout
        margin = 50
        y = self.Screen_Height // 2
        spacing = (SCREEN_WIDTH - 2 * margin) / (n - 1) if n > 1 else 0

        # Update each node's value/pos/radius only (leave color as-is)
        for i, node in enumerate(self.nodes):
            x = margin + i * spacing if n > 1 else SCREEN_WIDTH // 2
            node.value = self.values[i]
            node.pos = (int(x), int(y))
            node.radius = int(min(40, spacing / 2.5)) if n > 1 else 40

        


        
    def AskUser(self, screen) -> None:
        txt="Please select a data type:"
        screen.blit(FONT_S1.render(txt, True, WHITE, DED_GREEN), (20, 20))
        for btn in self.dataType_Btns:
            btn.display(screen)       
    def At_Head(self):
        
        if(self.interface_Btns[0].amClicked):
            self.insert_at_head(self.data_Type_dict[self.dataType](self.val))
            self.interface_Btns[0].amClicked=False

        elif(self.interface_Btns[1].amClicked):
            self.remove_At_Head()
            self.interface_Btns[1].amClicked=False
        print("Making input.\n")
        self.text = ''
        self.active1=False

    def At_Tail(self):
            
            if(self.interface_Btns[0].amClicked):
                self.insert_at_tail(self.data_Type_dict[self.dataType](self.val))
                self.interface_Btns[0].amClicked=False


            elif(self.interface_Btns[1].amClicked):
                self.remove_At_Tail()
                self.interface_Btns[1].amClicked=False
            

            elif(self.interface_Btns[2].is_clicked):
                print("Searching.")
            print("Making input.\n")
            self.text = ''
            self.active1=False

    def At_Indx(self):
            if(self.interface_Btns[0].amClicked):
                self.insert_at_index(self.data_Type_dict[self.dataType](self.val))
                self.interface_Btns[0].amClicked=False


            elif(self.interface_Btns[1].amClicked):
                self.remove_At_Index()
                self.interface_Btns[1].amClicked=False


            elif(self.interface_Btns[2].is_clicked):
                print("Searching.")
                self.interface_Btns[2].amClicked=False


    def remove_At_Head(self):
        x= self.values[0]
        self.values.remove(x)
        print(f"Removed{x}")
        self.Calculate_Node_Positions() 
        self.text = ''


    def remove_At_Tail(self):
        x=len(self.values)-1
        self.values.remove(self.values[x])
        self.Calculate_Node_Positions() 
        print(f"Removed value at  {x}")
        self.text = ''


    def remove_At_Index(self):
        x=self.idx
        self.values.remove(self.values[x])
        self.Calculate_Node_Positions() 
        self.text = ''


    def insert_at_head(self, data: DataType) -> None:
        self.values.insert(0, data)
        print(f"Inserting {data} at the head of the linked list.")
        self.Calculate_Node_Positions() 
        self.text = ''


    def insert_at_tail(self, data: DataType) -> None:
        self.values.append(data)
        print(f"Inserting {data} into the linked list.")
        self.Calculate_Node_Positions() 


    def insert_at_index(self, data: DataType) -> None:
        index= self.idx
        if index < 0:
            print(f"Index {index} is out of bounds for the linked list.")
            return
        self.values.insert(index, data)
        print(f"Inserting {data} at index {index} in the linked list.")
        self.Calculate_Node_Positions() 


    def delete(self, data: DataType) -> None:
        if data in self.values:
            self.values.remove(data)
            print(f"Deleted {data} from the linked list.")
        else:
            print(f"Value {data} not found in the linked list.")


    def search(self, data: DataType) -> bool:
        found = data in self.values
        if found:
            print(f"Value {data} found in the linked list.")
        else:
            print(f"Value {data} not found in the linked list.")
        return found
    
    def _reset_node_colors(self):
        self.Calculate_Node_Positions()
        for n in self.nodes:
            n.color = WHITE  


    def _blit_message(self, screen, msg, color, y=20):
        text = FONT_S1.render(msg, True, color)
        pad = 10
        r = text.get_rect()
        bg = pygame.Rect((SCREEN_WIDTH - r.width)//2 - pad, y - pad,
                        r.width + 2*pad, r.height + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, color, bg, 2)
        screen.blit(text, ((SCREEN_WIDTH - r.width)//2, y))
        

    def animate_search(self, screen, step_delay_ms=400,
                    base_color=WHITE, visit_color=YELLOW, found_color=L_GREEN):
        """
        Animates a linear search using the value already in self.val.
        1) If input empty OR list empty -> show one message and return -1
        2) Otherwise, color nodes one by one (visit_color)
        3) If match -> color that node found_color and show 'Found' at end
        else -> show 'Not Found' at end
        Returns index if found, else -1.
        """
        # Validate input
        if self.val is None or (isinstance(self.val, str) and self.val == ""):
            if Dark_Mode:
                screen.fill(BLACK_1)
            else: 
                screen.fill(CREAM)
            self.Draw(screen)
            self._blit_message(screen, "Enter a value first.", L_RED)
            pygame.display.flip()
            return -1

        if not self.values:
            if Dark_Mode:
                screen.fill(BLACK_1)
            else:
                screen.fill(CREAM)
            self.Draw(screen)
            self._blit_message(screen, "List is empty.", L_RED)
            pygame.display.flip()
            return -1

        # Ensure nodes align with values and reset colors
        self.Calculate_Node_Positions()
        for n in self.nodes:
            n.color = base_color
        found_idx = -1

        # Animate visiting each node
        for i, (node, value) in enumerate(zip(self.nodes, self.values)):
            node.color = visit_color
            if Dark_Mode:
                screen.fill(BLACK_1)
            else:
                screen.fill(CREAM)
            self.Draw(screen)
            pygame.display.flip()
            pygame.time.wait(step_delay_ms)

            if value == self.val:
                node.color = found_color
                found_idx = i
                # show final frame with found color
                if Dark_Mode:
                    screen.fill(BLACK_1)
                else:
                    screen.fill(CREAM)
                self.Draw(screen)
                pygame.display.flip()
                break

        # End message
        if Dark_Mode:
            screen.fill(BLACK_1)
        else:
            screen.fill(CREAM)
        self.Draw(screen)
        if found_idx != -1:
            self._blit_message(screen, f"Found {self.val} at index {found_idx}", L_GREEN)
        else:
            self._blit_message(screen, f"{self.val} not found", L_RED)

        # SHOW it now, then hold it briefly while pumping events
        pygame.display.flip()

        # keep UI responsive while holding the message
        t0 = pygame.time.get_ticks()
        while pygame.time.get_ticks() - t0 < 1000:  # 1000 ms = 1s
            pygame.event.pump()
            pygame.time.delay(10)

        self.in_Search = False
        self.interface_Btns[2].amClicked = False
        self.inDisplayBoxes = False
        self.text = ''
        self.active1 = False
        self._reset_node_colors()


    

    def Draw(self, screen) -> None:
        for n in self.nodes:
            x, y = n.pos
            pygame.draw.circle(screen, n.color, (x, y), n.radius)
            label = FONT_S3.render(str(n.value), True, L_RED)
            rect = label.get_rect(center=(x, y))
            screen.blit(label, rect)
        for i in range(len(self.nodes) - 1):
             n1 = self.nodes[i]
             n2 = self.nodes[i + 1]
             x1, y1 = n1.pos
             x2, y2 = n2.pos
             start = (x1 + n1.radius, y1)
             end = (x2 - n2.radius, y2)
             pygame.draw.line(screen, WHITE, start, end, 3)
             angle = math.atan2(y2 - y1, x2 - x1)
             arrow_size = 10
             left = (end[0] - arrow_size * math.cos(angle - math.pi/6),
                 end[1] - arrow_size * math.sin(angle - math.pi/6))
             right = (end[0] - arrow_size * math.cos(angle + math.pi/6),
                 end[1] - arrow_size * math.sin(angle + math.pi/6))
             pygame.draw.polygon(screen, WHITE, [end, left, right])








    def Draw_Buttons(self, screen):
        for btn in self.interface_Btns:
            btn.display(screen)
    def HandleInput(self, event,screen):
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
                    
                    try:
                        self.val = self.data_Type_dict[self.dataType](self.text)
                        print(f"Value set to: {self.val}")
                    except ValueError as e:
                        print(f"Invalid value: {e}")
                    if(self.in_Search):
                        self.animate_search(screen)
                    
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
        if not self.in_Search:
            """ Draw the input box for index"""
            x="Input Index"
            pygame.draw.rect(screen, clr, self.index_input_box, 3)
            idx_surface = FONT_S2.render(self.idx_txt, True, WHITE)
            x_surface = FONT_S4.render(x, True, WHITE)

            screen.blit(x_surface, (self.index_input_box.x , self.index_input_box.y + 50))
            screen.blit(idx_surface, (self.index_input_box.x + 5, self.index_input_box.y + 5))
            if self.In_Indx:
                pygame.draw.rect(screen, clr, self.index_input_box, 3)
