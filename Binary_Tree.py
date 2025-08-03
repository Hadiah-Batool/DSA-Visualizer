import pygame, math
pygame.init()
from UIProperties import *
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
                pygame.display.update()
                node.highlighted = False
                return node

             elif key < node.val:
                node = node.left
             else:
                node = node.right
        return None

    def _insert_recursive(self, node, key, screen):
        node.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(750)        #second pause
            # unmark it (or leave marked if found)
        node.highlighted = False

        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key, screen)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key, screen)
    def Insertion_Animated(self, screen,key ):
        if not self.values.root:
            self.values.root = Node(key)
            self.values.root.isRoot = True
        else:
            self._insert_recursive(self.values.root, key, screen)


    def delete(self, key, screen):
        self.root = self._delete_recursive(self.values.root, key, screen)

    def _delete_recursive(self, node, key, screen):
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
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x
    
    def left_rotate(self, x):
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
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S4.render(str(self.val), True, WHITE)
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

            vis = Visual_BST_Node()
            vis.val   = logical.key
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
            self.calculate_positions(SCREEN_WIDTH)
            vis = self.node_map.get(node)
            if vis:
                print("Heloo?")
                vis.color = PINK
                self.draw(screen);
                pygame.display.update()
                pygame.time.wait(1000)
                vis.color = D_GREEN
            return node
    
        root.highlighted = True
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(1000)        
            # unmark it (or leave marked if found)
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
        pygame.time.wait(500)        



        # Left Left Case
        if balance > 1 and key < root.left.key:
            old_root = root
            new_root = self.values.right_rotate(root)  # logical rotate
            self.animate_rotation(old_root, new_root, screen)
            return new_root
            
            # print("Shi is left heavy so, rotate towards right")
            # return self.values.right_rotate(root)
        
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            print("Shi is right heavy so, rotate towards left")
            return self.values.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            print("Shi is Left Right Case")
            root.left = self.values.left_rotate(root.left)
            return self.values.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            print("Shi is Left Right Left")
            root.right = self.values.right_rotate(root.right)
            return self.values.left_rotate(root)
        
        
        return root

    def Animated_Insert(self, screen):
        self.values.root= self.insert(self.values.root, self.val, screen)
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
            screen.fill(BLACK_1)  

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
