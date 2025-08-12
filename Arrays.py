import pygame
from UIProperties import *
pygame.init()
from Data_Structures import *
from Buttons import Button
LEFT_MARGIN = 20
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
        self.top_Margin = 200
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
        self.id_rects=[]
        self.interface_Btns = [ Button(150, 50, r'DSA_Visualizer/B_Red.png', "Insert", 32, 200, 100),
                                Button(350, 50, r'DSA_Visualizer/B_Red.png', "Delete", 32, 200, 100),
                                Button(550, 50, r'DSA_Visualizer/B_Red.png',"Clear", 32, 200, 100) 

        ]
        # linear-search state
        self.search_active = False
        self.search_target = None
        self.search_i = 0
        self.search_step_ms = 600      # time on each cell
        self.flash_all_until = 0       # brief "all red" flash at start
        self.message = ''              # status text (Found / Not found)
        self.message_until = 0         # show message for a short time
        self.delete_pending = False
        self.delete_target = None


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
                self.active2 = True
            else:
                self.active2 = False
        if event.type == pygame.KEYDOWN:
            if self.active2:
                if event.key == pygame.K_RETURN:
                    if self.input_text == '' or self.input_text is None:
                        print("Please enter a value to insert/delete")
                        return
                    else:
                        self.val = self.data_Type_dict[self.dataType](self.input_text)
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode
            
            print(f"Input text: {self.input_text}")
    def step_linear_search(self):
        """
        Advance the animated linear search by one 'tick'.
        Call this every frame (e.g., inside drawInterface) to animate.
        If delete_pending is True and a match is found, the element is deleted
        and the used prefix is compacted (shift-left).
        """

        if not getattr(self, "search_active", False):
            return

        now = pygame.time.get_ticks()

        # Initial "flash all" phase
        if now < self.flash_all_until:
            return

        # Only scan the used portion of the array; fall back to size if not present
        limit = getattr(self, "current_Count", getattr(self, "size", len(self.values)))

        # Done scanning -> not found
        if self.search_i >= limit:
            self.search_active = False
            self.highlight_index = None
            self.message = "Not found"
            self.message_until = now + 2000
            # clear delete mode if we were deleting
            if getattr(self, "delete_pending", False):
                self.delete_pending = False
            return

        # Keep current index highlighted during dwell time
        self.highlight_index = self.search_i

        # Match?
        if self.values[self.search_i] == self.search_target:
            hit_index = self.search_i
            # lock highlight on the hit for the normal dwell
            self.highlight_start = now

            if (self.delete_pending==True):
            # Delete + compact the used prefix so it stays contiguous
                if limit > 0:
                    for j in range(hit_index, limit - 1):
                        self.values[j] = self.values[j + 1]
                    self.values[limit - 1] = None
                    if hasattr(self, "current_Count") and self.current_Count > 0:
                        self.current_Count -= 1
                    self.message = f"Deleted at index {hit_index}"
                    self.message_until = now + 2000
                # exit delete mode
                self.delete_pending = False
            else:
                self.message = f"Found at index {hit_index}"
                self.message_until = now + 2000

            # end search either way
            self.search_active = False
            return

        # No match yet → advance after dwell time
        if now - self.highlight_start >= getattr(self, "search_step_ms", 600):
            self.search_i += 1
            self.highlight_start = now


    def insert(self, data: DataType) -> None:
    # only called when user clicks your “Insert” Button
        if (self.size) > self.current_Count:
            self.values[self.current_Count] = self.data_Type_dict[self.dataType](self.input_text)
            self.input_text = ''
            self.highlight_index = self.current_Count 
            self.current_Count += 1
            
            # start highlight animation…
            
            self.highlight_start = pygame.time.get_ticks()

    def Clear(self) -> None:
        # Clear the values and reset the current count
        self.values = [None] * self.size
        self.current_Count = 0
        self.highlight_index = None
        self.highlight_start = 0
        print("Cleared all values")    

    def delete(self, data: DataType) -> None:
        # kick off animated search; actual removal happens inside step_linear_search()
        self.delete_pending = True
        self.delete_target = data
        self.start_linear_search(data)


    def Draw(self, screen) -> None:
        # draw the prompt
        txt1 = "Enter the size of the values:(Press Enter to confirm)" 
        txt2 = "Please choose a moderate size For better visualization"
        screen.blit(FONT_S3.render(txt1, True, WHITE), (10, 10))
        screen.blit(FONT_S3.render(txt2, True, WHITE), (10, 50))
        # draw the current text
        txt_surf = FONT_S2.render(self.text, True, WHITE)
        self.input_box.w = max(200, txt_surf.get_width()+10)
        screen.blit(txt_surf, (self.input_box.x+5, self.input_box.y+5))
         # draw the box
        pygame.draw.rect(screen, self.color, self.input_box, 2)
        txt2 = "Choose the data type:"
        screen.blit(FONT_S2.render(txt2, True, WHITE), (10, 150))

    def start_linear_search(self, target):
        self.search_active = True
        self.search_target = target
        self.delete_pending = True
        self.search_i = 0

        now = pygame.time.get_ticks()
        self.flash_all_until = now + 300  # flash all for 300ms
        self.highlight_index = None
        self.highlight_start = now
        self.message = ''
        self.message_until = 0




    def drawInterface(self, screen) :
        if(self.text ==''):
            self.Draw(screen)
            return
        else:
         txt="Enter an element to insert/delete:"
         screen.blit(FONT_S2.render(txt, True, WHITE), (25, 10))
         txt_surf = FONT_S3.render(self.input_text, True, WHITE)
         screen.blit(txt_surf, (self.input_box_element.x+5, self.input_box_element.y+5))
         clr=None
         if self.active2:
             clr= self.color_active
         else:
             clr=self.color_inactive
         pygame.draw.rect(screen, clr, self.input_box_element, 2)
         for btn in self.interface_Btns:
             btn.display(screen)
        now = pygame.time.get_ticks()

        # drive the search state machine every frame
        self.step_linear_search()
        flash_all = now < self.flash_all_until
        i=0
        for i, rect in enumerate(self.rects):
            if flash_all:
                color = D_GREEN
            elif (i == self.highlight_index and now - self.highlight_start < self.interval):
                color = D_RED
            else:
                color = D_GREEN

            pygame.draw.rect(screen, color, rect, 4)

            # draw stored value (if any) centered
            if self.values[i] is not None:
                if(self.size< 10):
                    txt = FONT_S2.render(str(self.values[i]), True, WHITE)
                else:
                    txt = FONT_S3.render(str(self.values[i]), True, WHITE)
                txt_rect = txt.get_rect(center=rect.center)
                screen.blit(txt, txt_rect)
        for i, rect in enumerate(self.id_rects):
            if (i == self.highlight_index and
                now - self.highlight_start < self.interval):
                color = D_RED
            else:
                color = L_GREEN

            pygame.draw.rect(screen, color, rect, 4)
            if self.message and now < self.message_until:
                screen.blit(FONT_S2.render(self.message, True, WHITE), (25, 130))
            # draw index number centered
            txt = FONT_S4.render(str(i), True, WHITE)
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
                self.top_Margin,
                cell_w,
                CELL_HEIGHT
            )
            for i in range(self.size)

        ]  
        self.id_rects = [
            pygame.Rect(
                LEFT_MARGIN + i*(cell_w+SPACING),
                self.top_Margin + CELL_HEIGHT + 15,
                cell_w,
                30
            )
            for i in range(self.size)
        ]