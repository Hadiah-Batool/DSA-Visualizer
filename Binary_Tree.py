import pygame, math
pygame.init()
from UIProperties import *
from Buttons import Button
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.isRoot=False

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            self.root.isRoot=True
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Get the inorder successor (smallest in right subtree)
            temp = self._min_value_node(node.right)
            node.val = temp.val
            # Delete the inorder successor
            node.right = self._delete_recursive(node.right, temp.val)
        
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
class Visual_BST_Node:
    def __init__(self):
        self.value=0
        self.pos=(0, 0)
        self.color= WHITE
        self.radius = 20
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S2.render(str(self.val), True, WHITE)
        screen.blit(text_surface, (self.pos[0] - text_surface.get_width() // 2, self.pos[1] - text_surface.get_height() // 2))

class Animated_BST:
    def __init__(self):
         self.nodes = []
         self.values = Binary_Search_Tree()
         self.input_box= pygame.Rect(200, 100, 140, 50)   
         self.color_active = L_GREEN
         self.color_inactive = DED_GREEN
         self.color = self.color_inactive
         self.active1 = False # for value input
         self.active2 = False # for index input
         self.text = ''
         self.val = None
         self.interface_Btns = [
            Button(5, 0, r'DSA_Visualizer\B_Pink.png', "Insert", 28, 160, 80),
            Button(5, 60, r'DSA_Visualizer\B_Pink.png', "Delete", 28, 160, 80),
            Button(5, 120, r'DSA_Visualizer\B_Pink.png', "Search", 28, 160, 80)
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
    
    def Calculate_Node_Positions_Recursive(self):
        self.nodes.clear()
        pass
    def AskUser(self, screen) -> None:
        txt="Please select a data type:"
        screen.blit(FONT_S1.render(txt, True, WHITE, DED_GREEN), (20, 20))
        for btn in self.dataType_Btns:
            btn.display(screen) 
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

        """ Draw the input box for index"""
        x="Input Index"
        pygame.draw.rect(screen, clr, self.index_input_box, 3)
        idx_surface = FONT_S2.render(self.idx_txt, True, WHITE)
        x_surface = FONT_S4.render(x, True, WHITE)

        screen.blit(x_surface, (self.index_input_box.x , self.index_input_box.y + 50))
        screen.blit(idx_surface, (self.index_input_box.x + 5, self.index_input_box.y + 5))
        if self.In_Indx:
            pygame.draw.rect(screen, clr, self.index_input_box, 3)

