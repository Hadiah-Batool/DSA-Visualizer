import pygame, sys, math
from Buttons import Button
from UIProperties import *
from Arrays import Array
pygame.init()
temp= pygame.image.load(r'D:\Hadia\Python\DSA_Visualizer\HomeScreen_Bg.png')
Bg_Start= pygame.transform.smoothscale(temp, (800, 600))
Bg_Rect= Bg_Start.get_rect(center=(400, 300))

class MenuObj:
    def __init__(self, screen, clock, width, height, btns, selecButtons):
        self.screen = screen
        self.clock  = clock
        self.WIDTH  = width
        self.HEIGHT = height
        self.Menu_Btns= btns
        self.selec_Btns= selecButtons
        self.state = "main"    # other possible value: "options"
        self.ds_options=['Arrays', 'Linked Lists', 'Stacks', 'Queues', 'Trees', 'Heaps']
        self.ds_Btns = []
        i=80
        for B in self.ds_options:
            btn = Button(250, i, r'DSA_Visualizer\B_Pink.png', B, 30, 220, 110)
            self.ds_Btns.append(btn)
            i += 80

        self.algo_options=['Sorting Algorithms', '  Searching Algorithms']
        # 2) map button texts to the methods that should run
        self.algo_Btns = []
        self.actions ={
           
            "START":     self._go_to_options,
            "SETTINGS":  self._open_settings,
            "QUIT":      self._quit_game,
            "Data Structures": self._go_to_DataStructures,
            "Algorithms": self._go_to_Algorithms,
            "Arrays": self._go_to_Arrays,
            "Integer": self.go_to_arrayInterface,
            "Float": self.go_to_arrayInterface,
            "String": self.go_to_arrayInterface,
            "Char": self.go_to_arrayInterface, 
            # "Insert": self.go_to_Insert,
        }
    def _go_to_options(self):
        self.state = "options"
    def _go_to_DataStructures(self):
        self.state="Data Structures"
    def _go_to_Arrays(self):
        self.state="Arrays"
        self.array = Array()
    def go_to_arrayInterface(self):
        self.state = "Array Interface"
        self.array.InitializeRects()
    def _open_settings(self):
        # whatever you want your settings button to do
        pass
    # def go_to_Insert(self):
    #     self.state="Array_Insert"
    def _go_to_Algorithms(self):
        self.state="Algorithms"
    def _quit_game(self):
        pygame.quit()
        sys.exit()

    def title_screen(self):
        prompt = "Press any key to continue"
        title  = "Welcome to DSA Visualizer"
        t0     = pygame.time.get_ticks()

        while True:
            # 1) grab all events this frame
            for event in pygame.event.get():
                if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    return        # exit back to main when any key/mouse click
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            # 2) clear and draw your title screen
            self.screen.fill((30, 30, 30))
            self.screen.blit(Bg_Start, Bg_Rect)

            surf_title = FONT_S1.render(title, True, WHITE, L_GREEN)
            rect_title = surf_title.get_rect(
                center=(self.WIDTH//2, self.HEIGHT//3)
            )
            self.screen.blit(surf_title, rect_title)

            elapsed = pygame.time.get_ticks() - t0
            dx = 5 * math.sin(elapsed * 0.008)
            dy = 3 * math.sin(elapsed * 0.012)

            surf = FONT_S3.render(prompt, True, WHITE, PURPLE)
            rect = surf.get_rect(
                center=(self.WIDTH//2 + dx, self.HEIGHT*2//3 + dy)
            )
            self.screen.blit(surf, rect)

            # 3) flip & cap
            pygame.display.flip()
            self.clock.tick(60)
    def SelectionButtons_Display(self, screen):
        txt="What do you want to explore.\n"
        txt_D= FONT_S1.render(txt, True,WHITE, D_GREEN )
        txt_D_rect= txt_D.get_rect(center=(400, 50))
        screen.blit(txt_D, txt_D_rect)
        for s in self.selec_Btns:
            s.display(screen)

    def SelectionButtons_Fxn(self, event):
        for menu_b in self.selec_Btns:
            if menu_b.is_hovered(event):
                print(f"Selection Button{menu_b.text} hovered")
            if menu_b.is_clicked(event):
                print(f"Selection Button{ menu_b.text } clicked")
    def OptionButtons_Fxn(self, event, screen):
         for menu_b in self.Menu_Btns:
            if menu_b.is_hovered(event):
                print(f"Menu Button{menu_b.text} hovered")
            if menu_b.is_clicked(event):
                print(f"Menu Button{ menu_b.text } clicked")
                if menu_b.text=="START":
                    screen.fill(BLACK_1)

    def HandleEvents(self, event):
        
        if event.type not in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION, pygame.KEYDOWN, pygame.QUIT):
            return
        # choose which list to route events to
        if self.state == "main":
            button_list = self.Menu_Btns
        elif self.state == "options":
            button_list = self.selec_Btns
        elif self.state == "Data Structures":
            button_list = self.ds_Btns
        elif self.state == "Algorithms":
            button_list = self.algo_Btns
        elif self.state == "Arrays":
            button_list = self.array.dataType_Btns
            self.array.AskUser(event)
        elif self.state == "Array Interface":
            self.array.Take_input(event)
            button_list = self.array.interface_Btns
        # elif self.state == "Array_Insert":
        #     self.array.insert(self.array.val)
        #     button_list = self.array.interface_Btns
            
            

        else:
            button_list = self.Menu_Btns  

        for btn in button_list:
            if btn.is_clicked(event):
                if(self.state == "Arrays" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.array.dataType = btn.text
                action = self.actions.get(btn.text)
                if (self.state == "Array Interface") and btn.text == "Insert":
                    print("INSERT BUTTON CLICKED")
                    print("Printing Val:", self.array.val)
                    self.array.insert(self.array.val)
                # elif self.state == "Array Interface" and btn.text == "Delete":
                #     self.array.delete(self.array.val)
                # elif self.state == "Array Interface" and btn.text == "Back":
                #     self.state = "Arrays"
                if action:
                    action()
                else:
                    print(f"No action defined for button: {btn.text}")
                break
            elif btn.is_hovered(event):
                pass


    def HandleDisplay(self):
        self.screen.fill(BLACK_1)

        if self.state == "main":
            txt= "Choose an option."
            txt_D= FONT_S1.render(txt, True, WHITE,DED_GREEN)
            txt_D_rect= txt_D.get_rect(center=(400, 50))
            self.screen.blit(txt_D, txt_D_rect)
            for btn in self.Menu_Btns:
                btn.display(self.screen)

        elif self.state == "options":
            # draw a header, then only your selection buttons
            header = FONT_S2.render("What do you want to explore?", True, WHITE, D_GREEN)
            self.screen.blit(header, header.get_rect(center=(400, 50)))

            for btn in self.selec_Btns:
                btn.display(self.screen)

        elif self.state == "Data Structures":
           header = FONT_S2.render("Data Structures", True, WHITE, DED_GREEN)
           self.screen.blit(header, header.get_rect(center=(400, 50)))
           
           for btn in self.ds_Btns:
                btn.display(self.screen)
                
        elif self.state == "Algorithms":
            header = FONT_S1.render("Algorithms", True, WHITE, D_GREEN)
            self.screen.blit(header, header.get_rect(center=(350, 50)))
            i=100
            for B in self.algo_options:
                btn = Button(170, i, r'DSA_Visualizer\B_Red.png', B, 48, 510, 255)
                self.algo_Btns.append(btn)
                btn.display(self.screen)
                i += 200
        elif self.state == "Arrays":
            self.array.Draw(self.screen)
            for btn in self.array.dataType_Btns:
                btn.display(self.screen)
        elif self.state == "Array Interface":
            self.array.drawInterface(self.screen)
        elif self.state == "Array_Insert":
            self.array.drawInterface(self.screen)




