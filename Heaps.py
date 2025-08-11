import pygame, math
pygame.init()
from UIProperties import *
from Buttons import Button 
from collections import deque


class Heap:
    def __init__(self):

        self.Buttons=[Button(150, 150, r'DSA_Visualizer\B_Pink.png', "Min Heap", 54, 500, 250),
                      Button(150, 350, r'DSA_Visualizer\B_Sk_Blu.png', "Max Heap", 54, 500, 250)]
    def display(self, screen):
        txt="Choose a type of heap to visualize."
        screen.blit(FONT_S2.render(txt, True, WHITE, PURPLE),(10, 50))
        for b in self.Buttons:
            b.display(screen)        
class MinHeap:
    def __init__(self):
        """Initialize an empty min-heap."""
        self.heap = []

    def insert(self, value):
        """Insert a value into the min-heap."""
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the minimum element from the min-heap."""
        if self.is_empty():
            raise IndexError("Cannot extract from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def peek(self):
        """Return the minimum element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek an empty heap")
        return self.heap[0]

    def is_empty(self):
        """Return True if the heap is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def build_heap(self, arr):
        """Build a min-heap from an array."""
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._bubble_down(i)

    def _bubble_up(self, index):
        """Bubble up the element at the given index to maintain min-heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """Bubble down the element at the given index to maintain min-heap property."""
        min_index = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
                min_index = left
            if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
                min_index = right

            if min_index == index:
                break

            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            index = min_index

class MaxHeap:
    def __init__(self):
        """Initialize an empty max-heap."""
        self.heap = []

    def insert(self, value):
        """Insert a value into the max-heap."""
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        """Remove and return the maximum element from the max-heap."""
        if self.is_empty():
            raise IndexError("Cannot extract from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_val

    def peek(self):
        """Return the maximum element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek an empty heap")
        return self.heap[0]

    def is_empty(self):
        """Return True if the heap is empty, False otherwise."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def build_heap(self, arr):
        """Build a max-heap from an array."""
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._bubble_down(i)

    def _bubble_up(self, index):
        """Bubble up the element at the given index to maintain max-heap property."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index):
        """Bubble down the element at the given index to maintain max-heap property."""
        max_index = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left
            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right

            if max_index == index:
                break

            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            index = max_index
class Visual_Heap_Val:
    def __init__(self, val=0, pos=(0, 0), radius=30, color=WHITE):
        self.val = val
        self.pos = pos
        self.radius = radius
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        text_surface = FONT_S4.render(str(self.val), True, WHITE)
        screen.blit(text_surface, (self.pos[0] - text_surface.get_width() // 2, self.pos[1] - text_surface.get_height() // 2))
class Visual_Min_Heap:
    def __init__(self):
         self.nodes = []
         self.values = MinHeap()
         self.input_box= pygame.Rect(10, 10, 140, 70)  
         self.color_active = L_GREEN
         self.color_inactive = DED_GREEN
         self.color = self.color_inactive
         self.active1 = False # for value input
         self.text = ''
         self.val = None
         self.dataType = None
         self.highlight_index = None      # the node currently being inspected
         self.visited_indices = set()     # everything we’ve already looked at

         self.interface_Btns = [
            Button(155, 0, r'DSA_Visualizer\B_Maroon.png', "Insert", 32, 200, 100),
            Button(355, 0, r'DSA_Visualizer\B_Maroon.png', "  Extract Root",32, 210, 100),
            Button(555, 0, r'DSA_Visualizer\B_Maroon.png', "Search", 32, 200, 100)
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
        Builds self.node_map: index -> VisualNode. Uses (i, 2i+1, 2i+2) relations.
        """
        self.node_map = {}
        level_gap = 70   # vertical spacing between levels
        y_start   = 150  # top margin

        heap = self.values.heap  # MinHeap.heap list

        def recurse(i, x_min, x_max, depth):
            if i >= len(heap):
                return
            x = (x_min + x_max) // 2
            y = y_start + depth * level_gap

            vis = Visual_Heap_Val(val=heap[i], pos=(x, y),
                         color=PINK if getattr(self, 'highlight_index', None) == i else DED_GREEN)
            self.node_map[i] = vis

            left  = 2*i + 1
            right = 2*i + 2
            recurse(left,  x_min, x,     depth + 1)
            recurse(right, x,     x_max, depth + 1)

        recurse(0, 0, screen_width, 0)
    def draw(self, screen):
         # recompute positions each frame
            self.calculate_positions(SCREEN_WIDTH)

            # edges
            for i, vis in self.node_map.items():
                l, r = 2*i + 1, 2*i + 2
                if l in self.node_map:
                    pygame.draw.line(screen, WHITE, vis.pos, self.node_map[l].pos, 2)
                if r in self.node_map:
                    pygame.draw.line(screen, WHITE, vis.pos, self.node_map[r].pos, 2)

        # nodes with color logic
            for i, vis in self.node_map.items():
                if i == self.highlight_index:
                    vis.color = PINK       # current focus
                elif i in self.visited_indices:
                    vis.color = GREY     # already checked
                else:
                    vis.color = DED_GREEN  # default
                vis.draw(screen)

    def insert_animated(self, screen, value):
    # normal push
        self.values.heap.append(value)
        i = len(self.values.heap) - 1

        # bubble-up with visuals
        while i > 0:
            parent = (i - 1) // 2
            # highlight current & parent
            self.highlight_index = i
            screen.fill(BLACK_1)
            self.draw(screen)
            pygame.display.update()
            pygame.time.wait(500)

            if self.values.heap[i] < self.values.heap[parent]:  # min-heap compare
                
                self.values.heap[i], self.values.heap[parent] = self.values.heap[parent], self.values.heap[i]
                i = parent
            else:
                self.highlight_index=i
                break

        # final redraw
        screen.fill(BLACK_1)
        self.draw(screen)
        pygame.display.update()
        pygame.time.wait(750)
        self.highlight_index = None


    def extract_min_animated(self, screen):
        if not self.values.heap:
            return None
        if len(self.values.heap) == 1:
            v = self.values.heap.pop()
            screen.fill(BLACK_1); 
            self.draw(screen);
            pygame.display.update()
            return v

        min_val = self.values.heap[0]
        self.values.heap[0] = self.values.heap.pop()

        # bubble-down with visuals
        i = 0
        n = len(self.values.heap)
        while True:
            self.highlight_index = i
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
            pygame.time.wait(1000)

            left, right = 2*i+1, 2*i+2
            smallest = i
            if left < n and self.values.heap[left] < self.values.heap[smallest]:
                smallest = left
            if right < n and self.values.heap[right] < self.values.heap[smallest]:
                smallest = right
            if smallest == i:
                break

            self.highlight_index = i
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
            pygame.time.wait(1000)

            self.values.heap[i], self.values.heap[smallest] = self.values.heap[smallest], self.values.heap[i]
            i = smallest

        self.highlight_index = None
        screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
        return min_val
    def search_animated(self, screen, key):
        """
        Breadth-first search on a min-heap with pruning:
        If heap[i] > key, children (>= heap[i]) cannot contain key, so skip that subtree.
        Visuals:
        - highlight_index: node being inspected (PINK)
        - visited_indices: nodes already inspected (YELLOW)
        Returns (index or None).
        """
        heap = self.values.heap
        n = len(heap)
        if n == 0:
            return None

        
        q = deque([0])
        self.visited_indices.clear()
        self.highlight_index = None

        while q:
            i = q.popleft()
            if i >= n:
                continue

            # Focus this node
            self.highlight_index = i
            screen.fill(BLACK_1)
            self.draw(screen)
            pygame.display.update()
            pygame.time.wait(500)

            # Check for match
            if heap[i] == key:
                # leave it highlighted a bit longer for a nice "found!" effect
                pygame.time.wait(500)
                found_index = i

                # clean up visuals
                self.highlight_index = None
                self.visited_indices.clear()
                screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
                return found_index

            # Mark as visited (yellow thereafter)
            self.visited_indices.add(i)

            # Min-heap prune: if this node > key, no child can be key
            if heap[i] > key:
                continue

            # Otherwise, explore children
            left, right = 2*i + 1, 2*i + 2
            if left < n:
                q.append(left)
            if right < n:
                q.append(right)

            # Small redraw after enqueue to show growing frontier (optional)
            screen.fill(BLACK_1)
            self.draw(screen)
            pygame.display.update()

        # Not found
        self.highlight_index = None
        self.visited_indices.clear()
        screen.fill(BLACK_1); self.draw(screen);
        pygame.display.update()
        return None

class Visual_Max_Heap:
    def __init__(self):
        self.values = MaxHeap()                 # <— Max heap under the hood
        self.input_box = pygame.Rect(10, 10, 140, 70)

        # input state
        self.color_active   = L_GREEN
        self.color_inactive = DED_GREEN
        self.color = self.color_inactive
        self.active1 = False
        self.text = ''
        self.val = None
        self.dataType = None

        # visuals for animations
        self.highlight_index = None      # index being inspected
        self.visited_indices = set()     # already checked

        # buttons (same sizing as your min heap)
        self.interface_Btns = [
            Button(155, 0, r'DSA_Visualizer\B_Maroon.png', "Insert", 32, 200, 100),
            Button(355, 0, r'DSA_Visualizer\B_Maroon.png', "  Extract Root", 32, 210, 100),
            Button(555, 0, r'DSA_Visualizer\B_Maroon.png', "Search", 32, 200, 100),
        ]

       
        self.data_Type_dict = {"Integer": int, "Float": float, "String": str, "Char": str}
        self.dataType_Btns = [
            Button(50, 100,  r'DSA_Visualizer\B_Pink.png',   "Integer", 64, 300, 150),
            Button(400, 100, r'DSA_Visualizer\B_Purp.png',   "Float",   64, 300, 150),
            Button(50, 250,  r'DSA_Visualizer\B_DedBlu.png', "String",  64, 300, 150),
            Button(400, 250, r'DSA_Visualizer\B_Green.png',  "Char",    64, 300, 150),
        ]

    
    def AskUser(self, screen) -> None:
        txt = "Please select a data type:"
        screen.blit(FONT_S1.render(txt, True, WHITE, DED_GREEN), (20, 20))
        for btn in self.dataType_Btns:
            btn.display(screen)

    def HandleInput(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active1 = self.input_box.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active1:
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
        # helper text
        Ins1_surface = FONT_S3.render("Press Enter ", True, WHITE)
        Ins2_surface = FONT_S3.render("to confirm",   True, WHITE)
        Ins3_surface = FONT_S3.render("input",        True, WHITE)
        screen.blit(Ins1_surface, (630, 110))
        screen.blit(Ins2_surface, (630, 130))
        screen.blit(Ins3_surface, (630, 150))
        pygame.draw.rect(screen, YELLOW, pygame.Rect(620, 100, 175, 100), 3)

        # input box
        self.color = self.color_active if self.active1 else self.color_inactive
        pygame.draw.rect(screen, self.color, self.input_box, 3)
        txt_surface = FONT_S2.render(self.text, True, WHITE)
        y_surface   = FONT_S3.render("Input Value", True, WHITE)
        screen.blit(y_surface, (self.input_box.x, self.input_box.y + 80))
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        if self.active1:
            pygame.draw.rect(screen, self.color_active, self.input_box, 3)

    def Draw_Buttons(self, screen):
        for btn in self.interface_Btns:
            btn.display(screen)

    # ---------- layout & drawing ----------
    def calculate_positions(self, screen_width):
        """
        Build index->Visual_Heap_Val with positions using (i, 2i+1, 2i+2).
        """
        self.node_map = {}
        level_gap = 70
        y_start   = 150
        heap = self.values.heap

        def recurse(i, x_min, x_max, depth):
            if i >= len(heap): return
            x = (x_min + x_max) // 2
            y = y_start + depth * level_gap

            vis = Visual_Heap_Val(val=heap[i], pos=(x, y),
                                  color=PINK if self.highlight_index == i else DED_GREEN)
            self.node_map[i] = vis

            left, right = 2*i + 1, 2*i + 2
            recurse(left,  x_min, x,     depth + 1)
            recurse(right, x,     x_max, depth + 1)

        if heap:
            recurse(0, 0, screen_width, 0)

    def draw(self, screen):
        self.calculate_positions(SCREEN_WIDTH)

        # edges
        for i, vis in self.node_map.items():
            l, r = 2*i + 1, 2*i + 2
            if l in self.node_map:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[l].pos, 2)
            if r in self.node_map:
                pygame.draw.line(screen, WHITE, vis.pos, self.node_map[r].pos, 2)

        # nodes w/ color logic
        for i, vis in self.node_map.items():
            if i == self.highlight_index:
                vis.color = PINK         # current focus
            elif i in self.visited_indices:
                vis.color = GREY         # already checked
            else:
                vis.color = DED_GREEN    # default
            vis.draw(screen)

    # ---------- animations ----------
    def insert_animated(self, screen, value):
        self.values.heap.append(value)
        i = len(self.values.heap) - 1

        # bubble-up (max-heap: child > parent)
        while i > 0:
            parent = (i - 1) // 2
            self.highlight_index = i
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
            pygame.time.wait(500)

            if self.values.heap[i] > self.values.heap[parent]:
                self.values.heap[i], self.values.heap[parent] = self.values.heap[parent], self.values.heap[i]
                i = parent
            else:
                break

        self.highlight_index = None
        screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
        pygame.time.wait(750)

    def extract_max_animated(self, screen):
        if not self.values.heap:
            return None
        if len(self.values.heap) == 1:
            v = self.values.heap.pop()
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
            return v

        max_val = self.values.heap[0]
        self.values.heap[0] = self.values.heap.pop()

        # bubble-down (max-heap: parent < largest child)
        i, n = 0, len(self.values.heap)
        while True:
            self.highlight_index = i
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
            pygame.time.wait(1000)

            left, right = 2*i + 1, 2*i + 2
            largest = i
            if left < n and self.values.heap[left] > self.values.heap[largest]:
                largest = left
            if right < n and self.values.heap[right] > self.values.heap[largest]:
                largest = right
            if largest == i:
                break

            self.values.heap[i], self.values.heap[largest] = self.values.heap[largest], self.values.heap[i]
            i = largest

        self.highlight_index = None
        screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
        return max_val

    def search_animated(self, screen, key):
        """
        BFS on a max-heap with pruning:
        If heap[i] < key, children (<= heap[i]) cannot be key -> skip subtree.
        """
        heap = self.values.heap
        n = len(heap)
        if n == 0:
            return None

        from collections import deque
        q = deque([0])
        self.highlight_index = None
        self.visited_indices.clear()

        while q:
            i = q.popleft()
            if i >= n:
                continue

            # focus
            self.highlight_index = i
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
            pygame.time.wait(750)

            if heap[i] == key:
                pygame.time.wait(500)
                self.highlight_index = None
                self.visited_indices.clear()
                screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
                return i

            # mark visited
            self.visited_indices.add(i)

            # prune for max-heap
            if heap[i] < key:
                continue

            # explore children
            left, right = 2*i + 1, 2*i + 2
            if left  < n: q.append(left)
            if right < n: q.append(right)

            # optional redraw to show frontier growth
            screen.fill(BLACK_1); self.draw(screen); pygame.display.update()

        # not found
        self.highlight_index = None
        self.visited_indices.clear()
        screen.fill(BLACK_1); self.draw(screen); pygame.display.update()
        return None



