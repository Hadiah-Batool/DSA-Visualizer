import pygame, sys, math
from Buttons import Button
from UIProperties import *
from Arrays import Array
from Linked_Lists import LinkedList
from Stack import *
from Binary_Tree import *
from Algorithms import *
from Heaps import *
from Queue import *
from Settings import Setting_Object
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
        self.state = "main"    
        self.ds_options=['Arrays', 'Linked Lists', 'Stacks', 'Trees', 'Queues', 'Heaps']
        self.ds_Btns = []
        self.settings= Setting_Object()
        self.array = Array()
        self.linked_list = LinkedList()
        self.Stack=stack()
        self.tree = Trees()
        self.Queue= Queue()
        self.Heap= Heap()
        self.Min_Heap=Visual_Min_Heap()
        self.Max_Heap= Visual_Max_Heap()
        self.Array_Based_Queue= Queue_Array_Based()
        self.LL_Based_Queue= Queue_LinkedList_Based()
        self.BST= Animated_BST()  
        self.Array_Based_Stack= Stack_Array_Based()
        self.LL_Based_Stack= Stack_LinkedList_Based()
        self.AVL_Tree= Animated_AVL_Tree()
        self.Red_Black_Tree= Animated_Red_Black_Tree()
        self.Sorting_Algos= Sorting_Algos()
        self.Bubble_Sort= Bubble_Sort()
        self.DarkMode= False
        self.ShowGrid=False
        i=80
        for B in self.ds_options:
            btn = Button(250, i, r'DSA_Visualizer\B_Pink.png', B, 30, 220, 110)
            self.ds_Btns.append(btn)
            i += 80

        self.algo_options=['Sorting Algorithms', '  Searching Algorithms']
        
        self.algo_Btns = []
        i=100
        for B in self.algo_options:
            btn = Button(170, i, r'DSA_Visualizer\B_Red.png', B, 48, 510, 255)
            self.algo_Btns.append(btn)
            btn.display(self.screen)
            i += 200

        self.actions ={
           
            "START":     self._go_to_options,
            "SETTINGS":  self.go_to_Settings,
            "QUIT":      self._quit_game,
            "Data Structures": self._go_to_DataStructures,
            "Algorithms": self._go_to_Algorithms,
            "Arrays": self._go_to_Arrays,
            "Integer": self.go_to_arrayInterface,
            "Float": self.go_to_arrayInterface,
            "String": self.go_to_arrayInterface,
            "Char": self.go_to_arrayInterface, 
            "Linked Lists": self._go_to_LinkedLists,
            "Linked List Interface": self.go_to_linked_list_interface, 
            "At Head": self.go_AtHead,
            "At Tail": self.go_AtTail,
            "At Index": self.go_AtIndx,
            "Stacks" : self.go_to_Stack_Choose_Opt, 
            " Array Based Stack": self.go_to_Arr_Stack,
            "  Linked List Based Stack":self.go_to_LinkedListBasedStack,
            "Trees": self.go_to_trees, 
            "  Binary Search Tree" : self.go_to_BST,
            "AVL Tree": self.go_to_AVL_Tree,
            "Red Black Tree": self.go_to_RBTree, 
            "Sorting Algorithms":self.go_to_Sorting_Algo_interface,
            "Bubble Sort" : self.go_to_Bubble_sort,
            "Queues": self.go_to_Queue_Opt,
            " Array Based Queue": self.go_to_arrayBasedQueue, 
            "   Linked List Based Queue": self.go_to_LLBasedQueue,
            "Heaps": self.go_to_Heaps, "Min Heap": self.go_to_Min_Heap, 
            "Max Heap" : self.go_to_Max_Heap

        }
    def go_to_Settings(self):
        self.state = "Settings"
    def go_to_Max_Heap_Interface(self):
        self.state="Max Heap Interface"
    def go_to_Max_Heap(self):
        self.state= "Max Heap"
    def go_to_Min_Heap_Interface(self):
        self.state="Min Heap Interface"
    def go_to_Min_Heap(self):
        self.state="Min Heap"
    def go_to_Heaps(self):
        self.state="Heap"
    def go_to_LinkedListBasedQueue_Interface(self):
        self.state="LLBasedQueue_Interface"
    def go_to_LLBasedQueue(self):
        self.state= "LLBasedQueue"
    def go_to_arrayBasedQueue_Interface(self):
        self.state="ArrayBasedQueue Interface"
    def go_to_arrayBasedQueue(self):
        self.state="ArrayBasedQueue"
    def go_to_Queue_Opt(self):
        self.state="Queue_Opt"
    def go_to_Bubble_sort(self):
        self.state= "Bubble Sort"
    def go_to_Sorting_Algo_interface(self):
        self.state="Sorting Algo interface"
    def go_to_RBT_Interface(self):
        self.state="RBT_Interface"
    def go_to_RBTree(self):
        self.state="RB Tree"
    def go_to_AVL_Tree(self):
        self.state="AVL_Tree"
    def go_to_AVL_Interface(self):
        self.state="AVL_Interface"

    def go_to_BST_interface(self):
        self.state= "BST Interface"
    def go_to_BST(self):
        self.state= "BST"
    
    def go_to_trees(self):
        self.state="Trees_Opt_Choose"
    
    def go_to_LinkedListBasedStack_Interface(self):
        self.state="LinkedListBasedStack_Interface"
    def go_to_LinkedListBasedStack(self):
        self.state="  Linked List Based Stack"
    
    def go_to_Arr_Stack_Interface(self):
        self.state= "Array Stack Interface"
    def go_to_Arr_Stack(self):
        self.state= "Array Stack"
    def go_to_Stack_Choose_Opt(self):
        self.state="Stack_Choose_Opt"
    def go_AtHead(self):
        self.linked_list.At_Head()
        self.linked_list.inDisplayBoxes=False
        self.go_to_linked_list_interface()
    def go_AtTail(self):
        self.linked_list.At_Tail()
        self.linked_list.inDisplayBoxes=False
        self.go_to_linked_list_interface()
    def go_AtIndx(self):
        self.linked_list.At_Indx()
        self.linked_list.inDisplayBoxes=False
        self.go_to_linked_list_interface()
    def _go_to_options(self):
        self.state = "options"
    def _go_to_DataStructures(self):
        self.state="Data Structures"
    def _go_to_Arrays(self):
        self.state="Arrays"
        
    def go_to_arrayInterface(self):
        self.state = "Array Interface"
        self.array.InitializeRects()
    def _go_to_LinkedLists(self):
        
        self.state = "Linked Lists"
    def go_to_linked_list_interface(self):
        self.state = "Linked List Interface"
        
    def _open_settings(self, event):
        
        if (self.settings.Handle_Events(event)):
            self.ShowGrid = self.settings.Grid_Box.is_Clicked
            Dark_Mode = self.DarkMode = self.settings.Color_Mode_Box.is_Clicked
            self.state = "main"
            return
        else:
            self.ShowGrid = self.settings.Grid_Box.is_Clicked
            self.DarkMode = self.settings.Color_Mode_Box.is_Clicked



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
        print(f"Dark Mode: {Dark_Mode}")

        """ Handle all events in the menu"""
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
        elif self.state == "Linked Lists":
            button_list = self.linked_list.dataType_Btns
        elif self.state == "Linked List Interface" and not self.linked_list.inDisplayBoxes:
            button_list = self.linked_list.interface_Btns
        elif self.state == "Linked List Interface" and self.linked_list.inDisplayBoxes:
            self.linked_list.HandleInput(event)
            button_list = self.linked_list.Where_To_Buttons
        elif self.state=="Stack_Choose_Opt":
            button_list= self.Stack.Buttons
        elif self.state =="Array Stack":
            button_list = self.Array_Based_Stack.array.dataType_Btns
            self.Array_Based_Stack.array.AskUser(event)
        elif self.state =="Array Stack Interface":
            button_list= self.Array_Based_Stack.array.interface_Btns
            self.Array_Based_Stack.array.Take_input(event)
        elif self.state=="  Linked List Based Stack":
            button_list=self.LL_Based_Stack.dataType_Btns
        elif self.state=="LinkedListBasedStack_Interface":
            self.LL_Based_Stack.HandleInput(event)
            button_list= self.LL_Based_Stack.interface_Btns
        elif self.state=="Trees_Opt_Choose":
            button_list= self.tree.Buttons
        elif self.state== "BST":
            button_list= self.BST.dataType_Btns
        elif self.state=="BST Interface":
            self.BST.HandleInput(event)
            button_list= self.BST.interface_Btns
        elif self.state=="AVL_Tree":
            button_list= self.AVL_Tree.dataType_Btns
        elif self.state=="AVL_Interface":
            self.AVL_Tree.HandleInput(event)
            button_list= self.AVL_Tree.interface_Btns
        elif self.state=="RB Tree":
            button_list= self.Red_Black_Tree.dataType_Btns
        elif self.state=="RBT_Interface":
            self.Red_Black_Tree.HandleInput(event)
            button_list= self.Red_Black_Tree.interface_Btns
        elif self.state=="Sorting Algo interface":
            button_list=self.Sorting_Algos.algo_btns
        elif self.state=="Queue_Opt":
            button_list= self.Queue.Buttons
        elif self.state=="ArrayBasedQueue":
            button_list= self.Array_Based_Queue.array.dataType_Btns
            self.Array_Based_Queue.array.AskUser(event)
        elif self.state=="ArrayBasedQueue Interface":
            self.Array_Based_Queue.array.Take_input(event)
            button_list= self.Array_Based_Queue.array.interface_Btns
        elif self.state=="LLBasedQueue":
            button_list=self.LL_Based_Queue.dataType_Btns
        elif(self.state=="LLBasedQueue_Interface" ):
            self.LL_Based_Queue.HandleInput(event)
            button_list= self.LL_Based_Queue.interface_Btns
        elif self.state=="Heap":
            button_list= self.Heap.Buttons
        elif self.state=="Min Heap":
            button_list= self.Min_Heap.dataType_Btns
        elif self.state=="Min Heap Interface":
            button_list=self.Min_Heap.interface_Btns
            self.Min_Heap.HandleInput(event)
        elif self.state=="Max Heap":
            button_list= self.Max_Heap.dataType_Btns
        elif self.state=="Max Heap Interface":
            button_list=self.Max_Heap.interface_Btns
            self.Max_Heap.HandleInput(event)
        elif self.state == "Settings":
            self._open_settings(event)
            button_list = []  # No buttons to handle in settings


        # "Max Heap", "Max Heap Interface"
        else:
            button_list = self.Menu_Btns  




        for btn in button_list:
            if btn.is_clicked(event):
                if(self.state == "Arrays" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.array.dataType = btn.text
                    action = self.actions.get(btn.text)
                if (self.state == "Array Interface") and btn.text == "Insert":
                    self.array.insert(self.array.val)
                elif self.state == "Array Interface" and btn.text == "Delete":
                    self.array.delete(self.array.val)
                elif self.state == "Array Interface" and btn.text == "Clear":
                    self.array.Clear()
                elif self.state == "Linked Lists" and btn.text in ["Integer", "Float", "String", "Char"]:
                    self.linked_list.dataType = btn.text
                    self.go_to_linked_list_interface()
                    return
                elif self.state == "Linked List Interface" and btn.text in ["Insert", "Delete", "Search"]:
                    btn.amClicked=True
                    self.linked_list.inDisplayBoxes = True
                elif(self.state == "Array Stack" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.Array_Based_Stack.array.dataType = btn.text       
                    self.go_to_Arr_Stack_Interface()
                    return
                elif (self.state=="Array Stack Interface" and btn.text in["Push", "Pop", "Clear"]):
                    if (btn.text=="Push"):
                        self.Array_Based_Stack.array.insert(self.Array_Based_Stack.array.val)
                    elif (btn.text=="Pop"):
                        self.Array_Based_Stack.array.delete(self.Array_Based_Stack.array.values[(self.Array_Based_Stack.array.current_Count)-1])
                    elif(btn.text=="Clear"):
                        self.Array_Based_Stack.array.Clear()

                elif self.state == "  Linked List Based Stack" and btn.text in ["Integer", "Float", "String", "Char"]:
                    self.LL_Based_Stack.dataType = btn.text
                    self.go_to_LinkedListBasedStack_Interface()
                    return
                elif self.state=="LinkedListBasedStack_Interface" and btn.text in ["Push", "Pop", "Clear"]:
                    if (btn.text=="Push"):
                        self.LL_Based_Stack.insert_at_head(self.LL_Based_Stack.val)
                    elif (btn.text=="Pop"):
                        self.LL_Based_Stack.remove_At_Head()
                    elif(btn.text=="Clear"):
                        self.LL_Based_Stack.Clear()
                elif(self.state == "BST" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.BST.dataType = btn.text       
                    self.go_to_BST_interface()    
                    return          
                elif (self.state=="BST Interface" and btn.text in ["Insert", "Delete", "Search"] ):
                    if btn.text =="Insert":
                        self.BST.Insertion_Animated( self.screen, self.BST.val  )
                        self.BST.text=""
                    elif btn.text=="Delete":
                        self.BST.delete(self.BST.val, self.screen)
                        self.BST.text=""
                    elif btn.text=="Search":
                        self.BST.search_animated(self.screen, self.BST.val)
                        self.BST.text=""

                elif(self.state == "AVL_Tree" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.AVL_Tree.dataType = btn.text       
                    self.go_to_AVL_Interface() 
                    return
                elif (self.state=="AVL_Interface" and btn.text in ["Insert", "Delete", "Search"] ):
                    if btn.text =="Insert":
                        self.AVL_Tree.Animated_Insert(self.screen)
                        self.AVL_Tree.text=""

                    elif btn.text=="Delete":
                        # self.AVL_Tree.values.delete_key(self.AVL_Tree.val)
                        self.AVL_Tree.Delete_Animation(self.screen)
                        self.AVL_Tree.text=""
                    elif btn.text=="Search":
                        self.AVL_Tree.values.search_key(self.AVL_Tree.val)
                elif(self.state=="RB Tree" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.Red_Black_Tree.dataType= btn.text
                    self.go_to_RBT_Interface()
                    return
                elif self.state=="RBT_Interface"  and btn.text in ["Insert", "Delete", "Search"]:
                    if btn.text =="Insert":
                        self.Red_Black_Tree.values.insert(self.Red_Black_Tree.val)
                        self.Red_Black_Tree.text=""

                    elif btn.text=="Delete":
                        self.Red_Black_Tree.values.delete(self.Red_Black_Tree.val)
                        self.Red_Black_Tree.text=""
                    elif btn.text=="Search":
                        self.Red_Black_Tree.values._search(self.Red_Black_Tree.val)
                        self.Red_Black_Tree.text=""
                elif(self.state == "ArrayBasedQueue" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.Array_Based_Queue.array.dataType = btn.text       
                    self.go_to_arrayBasedQueue_Interface()
                    return
                elif (self.state=="ArrayBasedQueue Interface" and btn.text in["Enqueue", "Dequeue", "Clear"]):
                    if (btn.text=="Enqueue" and (self.Array_Based_Queue.array.input_text !='') ):
                        self.Array_Based_Queue.Enqueue()
                    elif (btn.text=="Dequeue"and (len(self.Array_Based_Queue.array.values)!=0)):
                        self.Array_Based_Queue.Dequeue()
                    elif(btn.text=="Clear"):
                        self.Array_Based_Queue.Clear()  
                elif(self.state == "LLBasedQueue" and btn.text in ["Integer", "Float", "String", "Char"]):
                    self.LL_Based_Queue.dataType = btn.text       
                    self.go_to_LinkedListBasedQueue_Interface()
                    return
                elif(self.state=="LLBasedQueue_Interface" and btn.text in["Enqueue", "Dequeue", "Clear"]):
                    if (btn.text=="Enqueue" ):
                        self.LL_Based_Queue.insert_at_tail(self.LL_Based_Queue.val)
                        self.LL_Based_Queue.text=''
                    elif (btn.text=="Dequeue"and (len(self.LL_Based_Queue.values)!=0)):
                        self.LL_Based_Queue.remove_At_Head()
                        
                    elif(btn.text=="Clear"):
                        self.LL_Based_Queue.Clear() 
                elif self.state=="Min Heap"and btn.text in ["Integer", "Float", "String", "Char"]:
                     self.Min_Heap.dataType = btn.text       
                     self.go_to_Min_Heap_Interface()
                     return

                elif (self.state=="Min Heap Interface" and btn.text in ["  Extract Root",  "Insert", "Search"] ):
                    if btn.text =="Insert":
                        self.Min_Heap.insert_animated(self.screen,self.Min_Heap.val )
                        self.Min_Heap.text=""
                    elif btn.text=="  Extract Root":
                        self.Min_Heap.extract_min_animated(self.screen)
                        self.Min_Heap.text=""
                    elif btn.text=="Search":
                        self.Min_Heap.search_animated(self.screen, self.Min_Heap.val)
                        self.Min_Heap.text=""
                elif self.state=="Max Heap"and btn.text in ["Integer", "Float", "String", "Char"]:
                     self.Max_Heap.dataType = btn.text       
                     self.go_to_Max_Heap_Interface()
                     return

                elif (self.state=="Max Heap Interface" and btn.text in ["  Extract Root",  "Insert", "Search"] ):
                    if btn.text =="Insert":
                        self.Max_Heap.insert_animated(self.screen,self.Max_Heap.val )
                        self.Max_Heap.text=""
                    elif btn.text=="  Extract Root":
                        self.Max_Heap.extract_max_animated(self.screen)
                        self.Max_Heap.text=""
                    elif btn.text=="Search":
                        self.Max_Heap.search_animated(self.screen, self.Max_Heap.val)
                        self.Max_Heap.text=""

                # Max Heap Interface
                else:
                    btn.amClicked=False

                action = self.actions.get(btn.text)
                if action:
                    action()
                    return
                else:
                    print(f"No action defined for button: {btn.text}")
                    break
            elif btn.is_hovered(event):
                pass




    def HandleDisplay(self):
        if self.DarkMode:
            self.screen.fill(BLACK_1)
        else:
            self.screen.fill(CREAM)

        if self.ShowGrid and self.state in ["Array Interface", "Linked List Interface",
         "LLBasedQueue_Interface", "ArrayBasedQueue Interface", "AVL_Interface", 
         "BST Interface", "LinkedListBasedStack_Interface", "Array Stack Interface", 
         "Max Heap Interface", "Min Heap Interface", "RBT_Interface"]:
            self.Show_Grid()



        if self.state == "main":
            txt= "Choose an option."
            txt_D= FONT_S1.render(txt, True, WHITE,DED_GREEN)
            txt_D_rect= txt_D.get_rect(center=(400, 50))
            self.screen.blit(txt_D, txt_D_rect)
            for btn in self.Menu_Btns:
                btn.display(self.screen)

        elif self.state == "options":
           
            header = FONT_S2.render("What do you want to explore?", True, WHITE, D_GREEN)
            self.screen.blit(header, header.get_rect(center=(400, 50)))

            for btn in self.selec_Btns:
                btn.display(self.screen)
        elif self.state == "Settings":
            self.settings.Display(self.screen)

        elif self.state == "Data Structures":
           header = FONT_S2.render("Data Structures", True, WHITE, DED_GREEN)
           self.screen.blit(header, header.get_rect(center=(400, 50)))
           
           for btn in self.ds_Btns:
                btn.display(self.screen)
                
        elif self.state == "Algorithms":
            header = FONT_S1.render("Algorithms", True, WHITE, D_GREEN)
            self.screen.blit(header, header.get_rect(center=(350, 50)))
            for btn in self.algo_Btns:
                btn.display(self.screen)

        elif self.state == "Arrays":
            self.array.Draw(self.screen)
            for btn in self.array.dataType_Btns:
                btn.display(self.screen)
        elif self.state == "Array Interface":
            self.array.drawInterface(self.screen)
        elif self.state == "Array_Insert":
            self.array.drawInterface(self.screen)
        elif self.state == "Linked Lists":
            self.linked_list.AskUser(self.screen)
        elif self.state == "Linked List Interface" :
            self.linked_list.Draw_Buttons(self.screen)
            if self.linked_list.inDisplayBoxes:
                self.linked_list.Draw_Where_To_Buttons(self.screen)
                self.linked_list.Draw_Inp_Box(self.screen)
            if len(self.linked_list.values)>0 :
                self.linked_list.Calculate_Node_Positions()
                self.linked_list.Draw(self.screen)
        elif self.state=="Stack_Choose_Opt":
            self.Stack.display(self.screen)
        elif self.state=="Array Stack":
            self.Array_Based_Stack.array.Draw(self.screen)
            for btn in self.Array_Based_Stack.array.dataType_Btns:
                btn.display(self.screen)
        elif self.state=="Array Stack Interface":
            self.Array_Based_Stack.Display(self.screen)
        elif self.state == "  Linked List Based Stack":
            self.LL_Based_Stack.AskUser(self.screen)
        elif self.state=="LinkedListBasedStack_Interface":
            self.LL_Based_Stack.Draw_Buttons(self.screen)
            self.LL_Based_Stack.Draw_Inp_Box(self.screen)
            self.LL_Based_Stack.Calculate_Node_Positions()
            self.LL_Based_Stack.Draw(self.screen)
        elif self.state=="Trees_Opt_Choose":
            self.tree.display(self.screen)
        elif self.state=="BST":
                self.BST.AskUser(self.screen)
        elif self.state=="BST Interface":
            self.BST.Draw_Inp_Box(self.screen)
            self.BST.Draw_Buttons(self.screen)
            self.BST.draw(self.screen)
        elif self.state=="AVL_Tree":
                self.AVL_Tree.AskUser(self.screen ) 
        elif self.state=="AVL_Interface":
            self.AVL_Tree.Draw_Inp_Box(self.screen)
            self.AVL_Tree.Draw_Buttons(self.screen)  
            self.AVL_Tree.draw(self.screen) 
        elif self.state=="RB Tree":
            self.Red_Black_Tree.AskUser(self.screen)
        elif self.state=="RBT_Interface":
            self.Red_Black_Tree.Draw_Inp_Box(self.screen)
            self.Red_Black_Tree.Draw_Buttons(self.screen)  
            self.Red_Black_Tree.draw(self.screen)    
        elif self.state=="Sorting Algo interface":
            self.Sorting_Algos.Draw(self.screen) 
        elif self.state=="Bubble Sort":
            self.Bubble_Sort.Perform_Animate(self.screen)   
        elif self.state=="Queue_Opt":
            self.Queue.display(self.screen)
        elif self.state=="ArrayBasedQueue":
            self.Array_Based_Queue.array.Draw(self.screen)
            for btn in self.Array_Based_Queue.array.dataType_Btns:
                btn.display(self.screen)
        elif self.state=="ArrayBasedQueue Interface":
            self.Array_Based_Queue.Display(self.screen)
        elif self.state == "LLBasedQueue":
            self.LL_Based_Queue.AskUser(self.screen)
        elif self.state=="LLBasedQueue_Interface":
            self.LL_Based_Queue.Draw_Buttons(self.screen)
            self.LL_Based_Queue.Draw_Inp_Box(self.screen)
            self.LL_Based_Queue.Calculate_Node_Positions()
            self.LL_Based_Queue.Draw(self.screen)
        elif self.state=="Heap":
            self.Heap.display(self.screen)
        elif self.state=="Min Heap":
            self.Min_Heap.AskUser(self.screen)
        elif self.state=="Min Heap Interface":
            self.Min_Heap.Draw_Inp_Box(self.screen)
            self.Min_Heap.Draw_Buttons(self.screen)
            self.Min_Heap.draw(self.screen)
        elif self.state=="Max Heap":
            self.Max_Heap.AskUser(self.screen)
        elif self.state=="Max Heap Interface":
            self.Max_Heap.Draw_Inp_Box(self.screen)
            self.Max_Heap.Draw_Buttons(self.screen)
            self.Max_Heap.draw(self.screen) 

    def Show_Grid(self):
        if self.DarkMode:
            clr = BLACK_2
        else :
            clr = (210, 192, 169)
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, clr, (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, clr, (0, y), (SCREEN_WIDTH, y), 1)




