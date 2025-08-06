import pygame, random
pygame.init()
from UIProperties import *
from Buttons import Button  
from Arrays import *
random.seed(76)

class Sorting_Algos:
    def __init__(self):
        self.algo_btns=[
            Button(200, 150, r'DSA_Visualizer\B_Sk_Blu.png', "Bubble Sort", 36, 360, 180),
            Button(200, 270, r'DSA_Visualizer\B_Pink.png', "Selection Sort", 36, 360, 180),
            Button(200, 390, r"DSA_Visualizer\B_Purp.png", "Insertion Sort", 36, 360, 180)
        ]

    def Draw(self, screen):
        txt = "Choose an algorithm to visualize."
        screen.blit(FONT_S2.render(txt, True, BLACK_1, YELLOW), (60, 70))
        for btn in self.algo_btns:
            btn.display(screen)

class Bubble_Sort:
    def __init__(self):
        # initialize array of fixed size with random ints
        self.array = Array()
        self.array.dataType = int
        self.array.size = 10
        self.array.values = [random.randint(0, 99) for _ in range(self.array.size)]
        # prepare rectangles for rendering
        self.array.InitializeRects()

    def Perform_Animate(self, screen):
        """
        Animate bubble sort on the array:
        - Highlight the two elements being compared in red
        - Highlight sorted elements (end of list) in light green
        - Draw each step with a delay of array.interval milliseconds
        """
        arr = self.array
        n = arr.size
        values = arr.values
        rects = arr.rects
        id_rects = arr.id_rects

        # bubble sort with animation
        for i in range(n):
            for j in range(0, n - i - 1):
                # render current state
                screen.fill(BLACK_1)
                for k in range(n):
                    rect = rects[k]
                    # compare
                    if k == j or k == j + 1:
                        border_color = L_RED
                    # sorted region
                    elif k >= n - i:
                        border_color = L_GREEN
                    # unsorted region
                    else:
                        border_color = DED_GREEN

                    # draw value cell
                    pygame.draw.rect(screen, border_color, rect, 4)
                    if values[k] is not None:
                        txt = FONT_S2.render(str(values[k]), True, WHITE) if n < 10 else FONT_S3.render(str(values[k]), True, WHITE)
                        screen.blit(txt, txt.get_rect(center=rect.center))

                    # draw index below
                    id_rect = id_rects[k]
                    pygame.draw.rect(screen, border_color, id_rect, 4)
                    txt_idx = FONT_S4.render(str(k), True, WHITE)
                    screen.blit(txt_idx, txt_idx.get_rect(center=id_rect.center))

                pygame.display.update()
                pygame.time.wait(arr.interval)

                # perform swap if out of order
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]

        # final pass: mark all as sorted
        return
        screen.fill(BLACK_1)
        for k in range(n):
            rect = rects[k]
            pygame.draw.rect(screen, L_GREEN, rect, 4)
            if values[k] is not None:
                txt = FONT_S2.render(str(values[k]), True, WHITE) if n < 10 else FONT_S3.render(str(values[k]), True, WHITE)
                screen.blit(txt, txt.get_rect(center=rect.center))

            id_rect = id_rects[k]
            pygame.draw.rect(screen, L_GREEN, id_rect, 4)
            txt_idx = FONT_S4.render(str(k), True, WHITE)
            screen.blit(txt_idx, txt_idx.get_rect(center=id_rect.center))

        pygame.display.update()
