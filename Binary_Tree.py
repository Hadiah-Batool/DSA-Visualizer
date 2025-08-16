import pygame, math
pygame.init()
from UIProperties import *
import UIProperties
from Buttons import Button
class Trees:
    def __init__(self):

        self.Buttons=[Button(200, 150, r'DSA_Visualizer\B_Sk_Blu.png', "  Binary Search Tree", 36, 360, 180),
                      Button(200, 270, r'DSA_Visualizer\B_Pink.png', "AVL Tree", 36, 360, 180),
                      Button(200, 390, r"DSA_Visualizer\B_Purp.png", "Red Black Tree",36, 360, 180)
                      ]
    def display(self, screen):
        txt="Choose a type of tree."
        screen.blit(FONT_S2.render(txt, True, WHITE, PURPLE),(140, 70))
        for b in self.Buttons:
            b.display(screen)

        

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.isRoot = False
        

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            self.root.isRoot = True
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        node.highlighted = True


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

    def print_tree(self):
        if not self.root:
            print("Tree is empty")
        else:
            self._print_inorder(self.root)
    
    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(node.val, end=" ")
            self._print_inorder(node.right)
class Visual_BST_Node:
    def __init__(self):
        self.value=0
        self.pos=(0, 0)
        self.color= WHITE
        self.radius = 30
        self.highlighted=False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S4.render(str(self.val), True, WHITE)
        screen.blit(text_surface, (self.pos[0] - text_surface.get_width() // 2, self.pos[1] - text_surface.get_height() // 2))

class Animated_BST:
    def __init__(self):
         self.nodes = []
         self.values = Binary_Search_Tree()
         self.input_box= pygame.Rect(10, 10, 140, 70)  
         self.color_active = L_GREEN
         self.color_inactive = DED_GREEN
         self.color = self.color_inactive
         self.active1 = False # for value input
         self.text = ''
         self.val = None
         self.dataType = None
         self.interface_Btns = [
            Button(155, 0, r'DSA_Visualizer\B_Pink.png', "Insert", 32, 200, 100),
            Button(355, 0, r'DSA_Visualizer\B_Pink.png', "Delete",32, 200, 100),
            Button(555, 0, r'DSA_Visualizer\B_Pink.png', "Search", 32, 200, 100)
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

    def Draw_Buttons(self, screen):
        for btn in self.interface_Btns:
            btn.display(screen)

            
    def calculate_positions(self, screen_width):
        """
        Builds a mapping self.node_map from each logical BST Node() to a Visual_BST_Node
        with .pos set so that the tree fans out downward.
        """
        self.node_map = {}
        level_gap = 60      # vertical spacing between levels
        y_start   = 150       # top margin

        def recurse(logical, x_min, x_max, depth):
            if logical is None:
                return
            # center this node in [x_min, x_max]
            x = (x_min + x_max) // 2
            y = y_start + depth * level_gap

            vis = Visual_BST_Node()
            vis.val   = logical.val
            vis.pos   = (x, y)
            # if we’ve marked this node as “highlighted” in an algorithm, pick a special color
            vis.color = PINK if getattr(logical, 'highlighted', False) else DED_GREEN

            self.node_map[logical] = vis

            recurse(logical.left,  x_min, x,     depth + 1)
            recurse(logical.right, x,     x_max, depth + 1)

        recurse(self.values.root, 0, screen_width, 0)


    def draw(self, screen):
        """
        Clears the screen, recalculates positions, draws edges, then draws nodes.
        """
       
        # 1) position every node
        self.calculate_positions(SCREEN_WIDTH)

        # 2) draw edges (parent→child)
        for logical, vis in self.node_map.items():
            if logical.left:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[logical.left].pos, 2)
            if logical.right:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[logical.right].pos, 2)

        # 3) draw each node on top of its edges
        for vis in self.node_map.values():
            vis.draw(screen)
    def _blit_message(self, screen, msg, color, y=20):
        text = FONT_S1.render(msg, True, color)
        pad = 10
        r = text.get_rect()
        bg = pygame.Rect((SCREEN_WIDTH - r.width)//2 - pad, y - pad,
                        r.width + 2*pad, r.height + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, color, bg, 2)
        screen.blit(text, ((SCREEN_WIDTH - r.width)//2, y))
        


    def search_animated(self, screen, key):
        node = self.values.root
        while node:
              # mark it
             node.highlighted = True
             self.draw(screen)
             pygame.display.update()
             pygame.time.wait(1000)        #second pause
            # unmark it (or leave marked if found)
             node.highlighted = False
             
             if key == node.val:
                node.highlighted = True   # final highlight
                self.draw(screen)
                self._blit_message(screen, "Found!", L_GREEN, 500)
                pygame.display.update()
                pygame.time.wait(1000)
                node.highlighted = False
                return node
             

             elif key < node.val:
                node = node.left
             else:
                node = node.right
        self._blit_message(screen, "Not found!", D_RED, 500)
        pygame.display.update()
        pygame.time.wait(1000)
        return None
    

    def _insert_recursive(self, node, key, screen):
        node.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(750)
        node.highlighted = False

        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key, screen)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key, screen)
        else:
            # duplicate → optionally flash a message
            self._blit_message(screen, "Duplicate! Ignored.", D_RED, 500)
            pygame.display.update()
            pygame.time.wait(750)
            return



    def Insertion_Animated(self, screen,key ):
        if not self.values.root:
            self.values.root = Node(key)
            self.values.root.isRoot = True
        else:
            self._insert_recursive(self.values.root, key, screen)

    def _min_value_node(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def delete(self, key, screen):
        self.values.root = self._delete_recursive(self.values.root, key, screen)


    def _delete_recursive(self, node, key, screen):
    
        if node is None:
            self._blit_message(screen, "Not found!", D_RED, 500)
            pygame.display.update()
            pygame.time.wait(500)
            return None
        node.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(750)        
            # unmark it (or leave marked if found)
        node.highlighted = False
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_recursive(node.left, key, screen)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key, screen)
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
            node.right = self._delete_recursive(node.right, temp.val, screen)
        
        return node

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.Balance_Factor=0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        if y is None or y.left is None:
            return y
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x
    
    def left_rotate(self, x):
        if x is None or x.right is None:
            return x
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y
    
    def insert(self, root, key, screen):
        # Standard BST insert
        if not root:
            return AVLNode(key)
        root.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(750)        
            # unmark it (or leave marked if found)
        root.highlighted = False


        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed
        
        # Update height
        self.update_height(root)
        
        # Get balance factor
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            print("Shi is left heavy so, rotate towards right")
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            print("Shi is right heavy so, rotate towards left")
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            print("Shi is Left Right Case")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            print("Shi is Left Right Left")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        
        return root
    
    def insert_key(self, key, screen):
        self.root = self.insert(self.root, key, screen)
    
    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, root, key):
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        if not root:
            return root
        
        # Update height
        self.update_height(root)
        
        # Get balance factor
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        
        # Left Right Case
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        
        # Right Left Case
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def delete_key(self, key):
        self.root = self.delete(self.root, key)
    
    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def search_key(self, key):
        return self.search(self.root, key)
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.key, end=' ')
        self.inorder(root.right)
    
    def print_inorder(self):
        self.inorder(self.root)
        print()
class Animated_AVL_Node:
    def __init__(self):
        self.value=0
        self.pos=(0, 0)
        self.color= WHITE
        self.radius = 30
        self.highlighted=False
        self.Balance_Factor=0
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S4.render(str(self.val), True, BLACK_1)
        bf_surface= FONT_S4.render(str(self.Balance_Factor), True, WHITE)
        screen.blit(bf_surface, ((self.pos[0] - text_surface.get_width() // 2)+10, self.pos[1] - text_surface.get_height()-30))
        screen.blit(text_surface, (self.pos[0] - text_surface.get_width() // 2, self.pos[1] - text_surface.get_height() // 2))
    
class Animated_AVL_Tree:
    def __init__(self):
         self.nodes = []
         self.values = AVLTree()
         self.input_box= pygame.Rect(10, 10, 140, 70)  
         self.color_active = L_GREEN
         self.color_inactive = DED_GREEN
         self.color = self.color_inactive
         self.active1 = False # for value input
         self.text = ''
         self.val = None
         self.dataType = None
         self.interface_Btns = [
            Button(155, 0, r'DSA_Visualizer\B_Pink.png', "Insert", 32, 200, 100),
            Button(355, 0, r'DSA_Visualizer\B_Pink.png', "Delete",32, 200, 100),
            Button(555, 0, r'DSA_Visualizer\B_Pink.png', "Search", 32, 200, 100)
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

    def Draw_Buttons(self, screen):
        for btn in self.interface_Btns:
            btn.display(screen)            
    def calculate_positions(self, screen_width):
        """
        Builds a mapping self.node_map from each logical BST Node() to a Visual_BST_Node
        with .pos set so that the tree fans out downward.
        """
        self.node_map = {}
        level_gap = 60      # vertical spacing between levels
        y_start   = 150       # top margin

        def recurse(logical, x_min, x_max, depth):
            if logical is None:
                return
            # center this node in [x_min, x_max]
            x = (x_min + x_max) // 2
            y = y_start + depth * level_gap

            vis = Animated_AVL_Node()
            vis.val   = logical.key
            vis.Balance_Factor= self.values.balance_factor(logical)
            vis.pos   = (x, y)
            # if we’ve marked this node as “highlighted” in an algorithm, pick a special color
            vis.color = PINK if getattr(logical, 'highlighted', False) else DED_GREEN

            self.node_map[logical] = vis

            recurse(logical.left,  x_min, x,     depth + 1)
            recurse(logical.right, x,     x_max, depth + 1)

        recurse(self.values.root, 0, screen_width, 0)


    def draw(self, screen):
        """
        Clears the screen, recalculates positions, draws edges, then draws nodes.
        """
       
        # 1) position every node
        self.calculate_positions(SCREEN_WIDTH)

        # 2) draw edges (parent→child)
        for logical, vis in self.node_map.items():
            if logical.left:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[logical.left].pos, 2)
            if logical.right:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[logical.right].pos, 2)

        # 3) draw each node on top of its edges
        for vis in self.node_map.values():
            vis.draw(screen)       

    def insert(self, root, key, screen):
        if not root:
            node = AVLNode(key)
            self.values.root = self.values.root
            return node
    
        root.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(1000)        
            # unmark it 
        root.highlighted = False


        if key < root.key:
            root.left = self.insert(root.left, key, screen)
        elif key > root.key:
            root.right = self.insert(root.right, key, screen)
        else:
            return root  # Duplicate keys not allowed
        
        # Update height
        self.values.update_height(root)
        
        # Get balance factor
        balance = self.values.balance_factor(root)
        

        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(1000)        



        # Left Left Case
        if balance > 1 and key < root.left.key:
            old_root = root
            new_root = self.values.right_rotate(root)  # logical rotate
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            old_root = root
            new_root = self.values.left_rotate(root)  # logical rotate
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
        # 1) First rotation on the left child
            old_child = root.left
            new_child = self.values.left_rotate(root.left)
        # animate child rotation
            self.animate_rotation(old_child, new_child, screen)
            root.left = new_child

        # 2) Then rotation at the root
            old_root = root
            new_root = self.values.right_rotate(root)
        # animate root rotation
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        # Right-Left Case
        if balance < -1 and key < root.right.key:
        # 1) First rotation on the right child
            old_child = root.right
            new_child = self.values.right_rotate(root.right)
        # animate child rotation
            self.animate_rotation(old_child, new_child, screen)
            root.right = new_child

        # 2) Then rotation at the root
            old_root = root
            new_root = self.values.left_rotate(root)
        # animate root rotation
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        
        return root

    def Animated_Insert(self, screen):
        self.values.root= self.insert(self.values.root, self.val, screen)


    def delete(self, root, key, screen):
        if not root:
            self._blit_message(screen, "Not found!", D_RED, 500)
            pygame.display.update()
            pygame.time.wait(800)
            return root
        
        root.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(1000)        
            # unmark it 
        root.highlighted = False

        if key < root.key:
            root.left = self.delete(root.left, key, screen)
        elif key > root.key:
            root.right = self.delete(root.right, key, screen)
        else:
            # Node with only one child or no child
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            
            # Node with two children
            temp = self.values.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key, screen)
        
        if not root:

            return root
        
        # Update height
        self.values.update_height(root)
        
        # Get balance factor
        balance = self.values.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            old_root = root
            new_root = self.values.right_rotate(root)  # logical rotate
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            old_root = root
            new_root = self.values.left_rotate(root)  # logical rotate
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
        # 1) First rotation on the left child
            old_child = root.left
            new_child = self.values.left_rotate(root.left)
        # animate child rotation
            self.animate_rotation(old_child, new_child, screen)
            root.left = new_child

        # 2) Then rotation at the root
            old_root = root
            new_root = self.values.right_rotate(root)
        # animate root rotation
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        # Right-Left Case
        if balance < -1 and key < root.right.key:
        # 1) First rotation on the right child
            old_child = root.right
            new_child = self.values.right_rotate(root.right)
        # animate child rotation
            self.animate_rotation(old_child, new_child, screen)
            root.right = new_child

        # 2) Then rotation at the root
            old_root = root
            new_root = self.values.left_rotate(root)
        # animate root rotation
            self.animate_rotation(old_root, new_root, screen)
            return new_root
        
        
        return root
    
    def Delete_Animation(self, screen):
        self.values.root = self.delete(self.values.root, self.val, screen)

    def clear_highlights(self):
        """Clear highlight from every node in the tree."""
        def dfs(n):
            if not n: return
            n.highlighted = False
            dfs(n.left); dfs(n.right)
        dfs(self.values.root)

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

    def search_animated(self, screen, key, keep_colored=False, step_ms=700):
        """
        Visual search: color every visited node.
        If keep_colored is False, the visited path is uncolored at the end.
        """
        node = self.values.root
        visited = []

        # Optional: clear previous highlights so this run stands out
        # comment out if you prefer cumulative coloring
        # self.clear_highlights()

        while node:
            node.highlighted = True
            visited.append(node)

            # draw step
            self.draw(screen)
            pygame.display.update()
            pygame.time.wait(step_ms)

            if key == node.key:
                self._blit_message(screen, "Found!", L_GREEN, 500)
                pygame.display.update()
                pygame.time.wait(800)
                if not keep_colored:
                    for n in visited:
                        n.highlighted = False
                    self.draw(screen)
                    pygame.display.update()
                return node

            node = node.left if key < node.key else node.right

        # not found
        self._blit_message(screen, "Not found!", D_RED, 500)
        pygame.display.update()
        pygame.time.wait(800)

        if not keep_colored:
            for n in visited:
                n.highlighted = False
            self.draw(screen)
            pygame.display.update()
        return None

    def animate_rotation(self, old_root, new_root, screen, frames=120):
        """
        Animate the subtree rotation that transformed `old_root` into `new_root`.
        Assumes the rotation (e.g. right_rotate) has already been applied to the logical tree.
        """

        # 1) Snapshot old positions (full tree!)
        # ------------------------------------------------
        # Make sure self.values.root still points at the full tree
        self.values.root = old_root
        self.calculate_positions(SCREEN_WIDTH)
        old_map = { node: vis.pos for node, vis in self.node_map.items() }

        # 2) Snapshot new positions (tree after rotation)
        # ------------------------------------------------
        # Rotation already done; recalc positions
        self.values.root = new_root
        self.calculate_positions(SCREEN_WIDTH)
        new_map = { node: vis.pos for node, vis in self.node_map.items() }

        # 3) Interpolate
        # ------------------------------------------------
        clock = pygame.time.Clock()
        # only animate nodes present in both snapshots
        common_nodes = [n for n in old_map if n in new_map]

        for t in range(1, frames + 1):
            alpha = t / frames

            
            if UIProperties.Dark_Mode:
                screen.fill(BLACK_1)
            else:
                screen.fill(CREAM)
            # 3a) update each node’s position
            for node in common_nodes:
                ox, oy = old_map[node]
                nx, ny = new_map[node]
                vis = self.node_map[node]
                vis.pos = (ox + (nx - ox) * alpha,
                           oy + (ny - oy) * alpha)

            # 3b) draw edges at interpolated positions
            for logical, vis in self.node_map.items():
                if logical.left:
                    pygame.draw.line(screen, WHITE,
                                     vis.pos,
                                     self.node_map[logical.left].pos, 2)
                if logical.right:
                    pygame.draw.line(screen, WHITE,
                                     vis.pos,
                                     self.node_map[logical.right].pos, 2)

            # 3c) draw nodes on top
            for vis in self.node_map.values():
                vis.draw(screen)

            pygame.display.update()
        clock.tick(10)          # only 30 updates per second
        pygame.time.wait(1000)  

        # 4) Final snap (to ensure exact alignment)
        self.calculate_positions(SCREEN_WIDTH)
# Red-Black Tree implementation in Python

class Color:
    RED = 0
    BLACK = 1

class RB_Node:
    def __init__(self, key, color=Color.RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self, observer=None):
        self.NIL = RB_Node(None, Color.BLACK)
        self.root = self.NIL
        self.observer = observer  

    def left_rotate(self, x):
        pre = self.observer.capture_positions() if self.observer else None  
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        if self.observer:  
            self.observer.on_rotate(pre)

    def right_rotate(self, y):
        pre = self.observer.capture_positions() if self.observer else None 
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        if self.observer:
            self.observer.on_rotate(pre)

    def insert(self, key):
        node = RB_Node(key)
        node.left = self.NIL
        node.right = self.NIL

        y = None
        x = self.root

        # DUP GUARD  — no duplicates
        while x != self.NIL:
            y = x
            if node.key == x.key:
                if self.observer:
                    self.observer.message("Duplicate! Ignored.", kind="warn")
                return                          # <— bail out (no insertion)
            x = x.left if node.key < x.key else x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        self._fix_insert(node)


    def _fix_insert(self, z):
        while z.parent and z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    if self.observer:
                        self.observer.on_recolor([z.parent, y, z.parent.parent])  # <— NEW
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    if self.observer:
                        self.observer.on_recolor([z.parent, z.parent.parent]) 
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    if self.observer:
                        self.observer.on_recolor([z.parent, z.parent.parent])
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    if self.observer:
                        self.observer.on_recolor([z.parent, z.parent.parent])
                    self.left_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = Color.BLACK

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, key):
        z = self._search(key)
        if z == self.NIL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = Color.BLACK

    def _search(self, key):
        current = self.root
        while current != self.NIL and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def _minimum(self, node):
        current = node
        while current.left != self.NIL:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node != self.NIL:
            self._inorder(node.left, result)
            result.append((node.key, 'RED' if node.color == Color.RED else 'BLACK'))
            self._inorder(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node != self.NIL:
            result.append((node.key, 'RED' if node.color == Color.RED else 'BLACK'))
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node != self.NIL:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append((node.key, 'RED' if node.color == Color.RED else 'BLACK'))


class Animated_Red_Black_Tree:
    def __init__(self):
         self.nodes = []
         self._screen = None
         self.values = RedBlackTree(observer=self)
         self.input_box= pygame.Rect(10, 10, 140, 70)
         self.color_active = L_GREEN
         self.color_inactive = DED_GREEN
         self.color = self.color_inactive
         self.active1 = False # for value input
         self.text = ''
         self.val = None
         self.dataType = None
         self.interface_Btns = [
            Button(155, 0, r'DSA_Visualizer\B_Green.png', "Insert", 32, 200, 100),
            Button(355, 0, r'DSA_Visualizer\B_Green.png', "Delete",32, 200, 100),
            Button(555, 0, r'DSA_Visualizer\B_Green.png', "Search", 32, 200, 100)
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

    def Draw_Buttons(self, screen):
        for btn in self.interface_Btns:
            btn.display(screen)

    def calculate_positions(self, screen_width):
        self.node_map = {}
        level_gap = 60
        y_start = 150

        def recurse(logical, x_min, x_max, depth):
            if logical is None or logical == self.values.NIL:   # <— ignore NIL
                return
            x = (x_min + x_max) // 2
            y = y_start + depth * level_gap

            vis = Animated_RBTree_Node()
            vis.val = logical.key
            base = GREY_2 if logical.color == Color.BLACK else D_RED
            vis.color = DED_GREEN if getattr(logical, 'highlighted', False) else base  # <— highlight wins
            vis.pos = (x, y)
            self.node_map[logical] = vis

            recurse(logical.left,  x_min, x,     depth + 1)
            recurse(logical.right, x,     x_max, depth + 1)

        recurse(self.values.root, 0, screen_width, 0)
    def _blit_message(self, screen, msg, color, y=520):
        text = FONT_S1.render(msg, True, color)
        pad = 10
        r = text.get_rect()
        bg = pygame.Rect((SCREEN_WIDTH - r.width)//2 - pad, y - pad, r.width + 2*pad, r.height + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, color, bg, 2)
        screen.blit(text, ((SCREEN_WIDTH - r.width)//2, y))

    def message(self, msg, kind="info"):
        col = L_GREEN if kind == "ok" else (D_RED if kind == "warn" else WHITE)
        self._blit_message(self._screen, msg, col, 500)
        pygame.display.update()
        pygame.time.wait(800)

    def clear_highlights(self):
        def dfs(n):
            if not n or n == self.values.NIL: return
            n.highlighted = False
            dfs(n.left); dfs(n.right)
        dfs(self.values.root)

    def capture_positions(self):
        self.calculate_positions(SCREEN_WIDTH)
        return {node: vis.pos for node, vis in self.node_map.items()}

    def draw(self, screen):
        """
        Clears the screen, recalculates positions, draws edges, then draws nodes.
        """
       
        # 1) position every node
        self.calculate_positions(SCREEN_WIDTH)

        # 2) draw edges (parent→child)
        for logical, vis in self.node_map.items():
            if logical.left  and logical.left  != self.values.NIL:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[logical.left].pos, 2)
            if logical.right and logical.right != self.values.NIL:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[logical.right].pos, 2)


        # 3) draw each node on top of its edges
        for vis in self.node_map.values():
            vis.draw(screen)   
    def on_rotate(self, pre_positions, frames=60):
        # pre_positions = positions captured *before* the rotation
        post_positions = self.capture_positions()
        common = [n for n in pre_positions if n in post_positions]

        for t in range(1, frames + 1):
            alpha = t / frames

            # background
            if UIProperties.Dark_Mode:
                self._screen.fill(BLACK_1)
            else:                     
                self._screen.fill(CREAM)

            # interpolate node positions
            self.calculate_positions(SCREEN_WIDTH)  # refresh node_map with current nodes/colors
            for n in common:
                ox, oy = pre_positions[n]
                nx, ny = post_positions[n]
                self.node_map[n].pos = (ox + (nx - ox) * alpha, oy + (ny - oy) * alpha)

            # draw edges then nodes
            for n, vis in self.node_map.items():
                if n.left and n.left != self.values.NIL:
                    pygame.draw.line(self._screen, WHITE, vis.pos, self.node_map[n.left].pos, 2)
                if n.right and n.right != self.values.NIL:
                    pygame.draw.line(self._screen, WHITE, vis.pos, self.node_map[n.right].pos, 2)
            for vis in self.node_map.values():
                vis.draw(self._screen)

            pygame.display.update()
        pygame.time.wait(150)  # small settle pause

    def on_recolor(self, nodes):
        # Just redraw once with a short pause so color changes are visible
        self.draw(self._screen)
        pygame.display.update()
        pygame.time.wait(350)
    def search_animated(self, screen, key, keep_colored=False, step_ms=700):
        self._screen = screen
        node = self.values.root
        visited = []
        while node and node != self.values.NIL:
            node.highlighted = True
            visited.append(node)
            self.draw(screen); pygame.display.update(); pygame.time.wait(step_ms)

            if key == node.key:
                self.message("Found!", kind="ok")
                if not keep_colored:
                    for n in visited: n.highlighted = False
                    self.draw(screen); pygame.display.update()
                return node
            node = node.left if key < node.key else node.right

        self.message("Not found!", kind="warn")
        if not keep_colored:
            for n in visited: n.highlighted = False
            self.draw(screen);
            pygame.display.update()
        return None
    def insert_animated(self, screen, key):
        self._screen = screen
        # Visual descent (and duplicate check before calling logical insert)
        x = self.values.root
        while x and x != self.values.NIL:
            x.highlighted = True
            self.draw(screen); pygame.display.update(); pygame.time.wait(500)
            if key == x.key:
                self.message("Duplicate! Ignored.", kind="warn")
                x.highlighted = False
                self.draw(screen); pygame.display.update()
                return
            x.highlighted = False
            x = x.left if key < x.key else x.right

        # Logical insert triggers fixups; rotations/recolors animate via observer
        self.values.insert(key)
        self.draw(screen); 
        pygame.display.update()
    def delete_animated(self, screen, key):
        self._screen = screen
        z = self.values._search(key)
        if z == self.values.NIL:
            self.message("Not found!", kind="warn")
            return

        # Visual descent to the node
        x = self.values.root
        while x and x != self.values.NIL:
            x.highlighted = True
            self.draw(screen); pygame.display.update(); pygame.time.wait(400)
            if x == z: break
            x.highlighted = False
            x = x.left if key < x.key else x.right

        self.values.delete(key)   # rotations/recolors animate via observer
        self.message("Deleted", kind="ok")
        self.clear_highlights()
        self.draw(screen); pygame.display.update()




class Animated_RBTree_Node:
    def __init__(self):
        self.value=0
        self.pos=(0, 0)
        self.color= L_RED
        self.radius = 30
        self.highlighted=False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S4.render(str(self.val), True, WHITE)
        screen.blit(text_surface, (self.pos[0] - text_surface.get_width() // 2, self.pos[1] - text_surface.get_height() // 2))
