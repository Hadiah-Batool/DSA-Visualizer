import pygame
pygame.init()

from UIProperties import *
from Buttons import Button  
from Arrays import *
import time, random
random.seed(time.time())


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
        self.array = Array()
        self.array.dataType = int
        self.array.size = 10
        self.array.values = [random.randint(0, 99) for _ in range(self.array.size)]
        self.array.InitializeRects()

        # animation state
        self.i = 0
        self.j = 0
        self.running = False
        self.paused = False
        self.done = False
        self.last_step_ms = 0  # throttle by array.interval

        # small control buttons (bottom-left; away from Back at bottom-right)
        self.control_btns = [
            Button(20, 520, r'DSA_Visualizer\B_Pink.png', " Stop/Start", 28,  160, 80),
            Button(170, 520, r'DSA_Visualizer\B_Pink.png', " Restart",     28, 160, 80),
        ]

        # banner message state
        self.banner_text = ""
        self.banner_until = 0

    # ---- public API ----
    def start(self):
        """(Re)start with fresh random values and show banner."""
        n = self.array.size
        self.array.values = [random.randint(0, 99) for _ in range(n)]
        self.i = 0
        self.j = 0
        self.running = True
        self.paused = False
        self.done = False
        self._set_banner("Starting Bubble Sort with random values…", 2500)
        

    def restart(self):
        self.start()

    def toggle_pause(self):
        if not self.running:  
            return
        self.paused = not self.paused

 
    def handle_event(self, event):
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            for b in self.control_btns:
                b.is_hovered(event)
                if b.is_clicked(event):
                    if b.text.strip() == "Stop/Resume":
                        self.toggle_pause()
                    elif b.text.strip() == "Restart":
                        self.restart()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   # keyboard pause/resume
                self.toggle_pause()
            elif event.key == pygame.K_r:     # keyboard restart
                self.restart()

    # ---- drawing & stepping ----
    def _set_banner(self, text, ms):
        self.banner_text = text
        self.banner_until = pygame.time.get_ticks() + ms

    def _draw_banner(self, screen):
        if pygame.time.get_ticks() > self.banner_until or not self.banner_text:
            return
        surf = FONT_S3.render(self.banner_text, True, WHITE)
        pad = 8
        rect = surf.get_rect(midtop=(SCREEN_WIDTH // 2, 8))
        bg = pygame.Rect(rect.x - pad, rect.y - pad, rect.w + 2*pad, rect.h + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, DED_GREEN, bg, 2)  # <- 2px outline
        screen.blit(surf, rect)

    
        
    

    def _draw_array(self, screen, highlight_a=None, highlight_b=None, sorted_from=None):
        arr = self.array
        values, rects, ids = arr.values, arr.rects, arr.id_rects
        # don’t clear here; the menu already filled screen and (optionally) grid
        for k, rect in enumerate(rects):
            if k in (highlight_a, highlight_b):
                border = L_RED
            elif sorted_from is not None and k >= sorted_from:
                border = L_GREEN
            else:
                border = DED_GREEN
            pygame.draw.rect(screen, border, rect)
            txt = (FONT_S2 if arr.size < 10 else FONT_S3).render(str(values[k]), True, WHITE)
            screen.blit(txt, txt.get_rect(center=rect.center))

            idr = ids[k]
            pygame.draw.rect(screen, border, idr)
            idx = FONT_S4.render(str(k), True, WHITE)
            screen.blit(idx, idx.get_rect(center=idr.center))

        # draw controls
        for b in self.control_btns:
            b.display(screen)

        # banner last (top, slim)
        self._draw_banner(screen)

    def update_and_draw(self, screen):
        """Call this every frame: draws + advances by at most one comparison."""
        arr = self.array
        n = arr.size
        values = arr.values

        # draw current frame first
        sorted_from = (n - self.i) if self.running else (n if self.done else None)
        self._draw_array(screen, 
                         highlight_a=self.j if self.running else None,
                         highlight_b=(self.j + 1) if self.running else None,
                         sorted_from=sorted_from)

        if not self.running or self.paused or self.done:
            return  # nothing to advance

        # throttle: only do a step every arr.interval ms
        now = pygame.time.get_ticks()
        if now - self.last_step_ms < arr.interval:
            return
        self.last_step_ms = now

        # --- one bubble-sort comparison step ---
        if values[self.j] > values[self.j + 1]:
            values[self.j], values[self.j + 1] = values[self.j + 1], values[self.j]

        self.j += 1
        if self.j >= n - self.i - 1:
            self.j = 0
            self.i += 1
            if self.i >= n - 1:
                self.running = False
                self.done = True
                self._set_banner("Done.", 1800)
class Selection_Sort:
    def __init__(self):
        self.array = Array()
        self.array.dataType = int
        self.array.size = 10
        self.array.values = [random.randint(0, 99) for _ in range(self.array.size)]
        self.array.InitializeRects()

        self.i = 0
        self.j = 1
        self.min_idx = 0
        self.running = False
        self.paused = False
        self.done = False
        self.last_step_ms = 0

        # swap animation state
        self.swapping = False
        self.swap_a = None
        self.swap_b = None
        self.swap_flash_until = 0

        
        self.control_btns = [
            Button(20, 520, r'DSA_Visualizer\B_Pink.png', " Stop/Start", 28,  160, 80),
            Button(170, 520, r'DSA_Visualizer\B_Pink.png', " Restart",     28, 160, 80),
        ]
        self.banner_text = ""
        self.banner_until = 0

    # ---------- user actions ----------
    def _set_banner(self, text, ms):
        self.banner_text = text
        self.banner_until = pygame.time.get_ticks() + ms

    def start(self):
        n = self.array.size
        self.array.values = [random.randint(0, 99) for _ in range(n)]
        self.i, self.j, self.min_idx = 0, 1, 0
        self.running, self.paused, self.done = True, False, False
        self.swapping = False
        self._set_banner("Starting Selection Sort with random values", 2500)
        

    def restart(self):
        self.start()

    def toggle_pause(self):
        if self.running:
            self.paused = not self.paused

    # ---------- events ----------
    def handle_event(self, event):
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            for b in self.control_btns:
                b.is_hovered(event)
                if b.is_clicked(event):
                    if b.text.strip() == "Stop/Resume":
                        self.toggle_pause()
                    elif b.text.strip() == "Restart":
                        self.restart()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.toggle_pause()
            elif event.key == pygame.K_r:
                self.restart()

    # ---------- drawing ----------
    def _draw_banner(self, screen):
        if pygame.time.get_ticks() > self.banner_until or not self.banner_text:
            return
        surf = FONT_S3.render(self.banner_text, True, WHITE)
        pad = 8
        rect = surf.get_rect(midtop=(SCREEN_WIDTH // 2, 8))
        bg = pygame.Rect(rect.x - pad, rect.y - pad, rect.w + 2*pad, rect.h + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, DED_GREEN, bg, 2)  # <- 2px outline
        screen.blit(surf, rect)


    def _draw_array(self, screen, highlight_a=None):
        arr = self.array
        values, rects, ids = arr.values, arr.rects, arr.id_rects
        n = len(values)

        for k, rect in enumerate(rects):
            # decide border color
            if self.swapping and (k == self.swap_a or k == self.swap_b):
                border = PURPLE  # flash swapped ones
            elif k < self.i:
                border = L_GREEN  # sorted portion
            elif k == self.min_idx and not self.done:
                border = L_RED  # current min
                # Show a text saying current min
                txt = FONT_S4.render("Current Min", True, WHITE)
                screen.blit(txt, txt.get_rect(center=(rect.centerx+5, rect.top - 20)))
            elif k == highlight_a:
                border = PINK    # scanning element
            else:
                border = DED_GREEN

            pygame.draw.rect(screen, border, rect)
            txt = (FONT_S2 if arr.size < 10 else FONT_S3).render(str(values[k]), True, WHITE)
            screen.blit(txt, txt.get_rect(center=rect.center))

            # index box
            idr = ids[k]
            pygame.draw.rect(screen, border, idr)
            idx = FONT_S4.render(str(k), True, WHITE)
            screen.blit(idx, idx.get_rect(center=idr.center))

        # min marker rectangle (under the min_idx box)
        if not self.done:
            min_rect = rects[self.min_idx]
            marker = pygame.Rect(min_rect.x, min_rect.bottom + 4, min_rect.w, 6)
            pygame.draw.rect(screen, L_RED, marker)

        for b in self.control_btns:
            b.display(screen)
        self._draw_banner(screen)

    # ---------- logic: one step per frame ----------
    def update_and_draw(self, screen):
        values = self.array.values
        n = len(values)

        # draw first
        self._draw_array(screen, highlight_a=self.j)

        if not self.running or self.paused or self.done:
            return

        now = pygame.time.get_ticks()
        if now - self.last_step_ms < self.array.interval:
            return
        self.last_step_ms = now

        # handle swap flash timeout
        if self.swapping and pygame.time.get_ticks() > self.swap_flash_until:
            self.swapping = False

        # if j reached end, swap min into position
        if self.j >= n:
            if self.min_idx != self.i:
                values[self.i], values[self.min_idx] = values[self.min_idx], values[self.i]
                # record for flashing
                self.swapping = True
                self.swap_a, self.swap_b = self.i, self.min_idx
                self.swap_flash_until = pygame.time.get_ticks() + 600
            self.i += 1
            if self.i >= n - 1:
                self.running = False
                self.done = True
                self._set_banner("Done.", 1000)
                return
            self.min_idx = self.i
            self.j = self.i + 1
            return

        # scanning step
        if values[self.j] < values[self.min_idx]:
            self.min_idx = self.j
        self.j += 1



# --- Insertion Sort with TEMP box, shifts & placement cues -------------------
class Insertion_Sort:
    def __init__(self):
        self.array = Array()
        self.array.dataType = int
        self.array.size = 10
        self.array.values = [random.randint(0, 99) for _ in range(self.array.size)]
        self.array.InitializeRects()

        # indices for incremental insertion
        self.i = 1            # first unsorted index
        self.j = 0            # pointer scanning the sorted prefix
        self.key = None       # value being inserted (shows in TEMP)
        self.phase = "load"   # "load" -> take into TEMP, "shift" -> j→j+1 moves, "place" -> write TEMP
        self.running = False
        self.paused = False
        self.done = False
        self.last_step_ms = 0

        # TEMP UI
        self.temp_visible = False
        self.temp_pos = None   # computed from array rects
        self.temp_flash_until = 0

        # flash/arrow state for shifts/placement
        self.swapping = False
        self.swap_a = None
        self.swap_b = None
        self.swap_flash_until = 0


        # colors/tags
        self.color_i = L_GREEN
        self.color_j = L_RED
        self.color_w = PINK

        # UI controls (bottom-left; won’t cover Back button)
        self.control_btns = [
            Button(20, 520,  r'DSA_Visualizer\B_Pink.png', " Stop/Start", 28, 160, 80),
            Button(190, 520, r'DSA_Visualizer\B_Pink.png', " Restart",     28, 160, 80),
        ]
        self.banner_text = ""
        self.banner_until = 0

    # ---------- helpers ----------
    def _set_banner(self, text, ms):
        self.banner_text = text
        self.banner_until = pygame.time.get_ticks() + ms

    def _flash(self, a, b, ms=450):
        self.swapping = True
        self.swap_a, self.swap_b = a, b
        self.swap_flash_until = pygame.time.get_ticks() + ms




    def start(self):
        n = self.array.size
        self.array.values = [random.randint(0, 99) for _ in range(n)]
        self.i, self.j, self.key, self.phase = 1, 0, None, "load"
        self.running = True
        self.paused = False
        self.done = False
        self.temp_visible = False
        self._set_banner("Starting Insertion Sort with random values", 2500)

    def restart(self):
        self.start()

    def toggle_pause(self):
        if self.running:
            self.paused = not self.paused

    # ---------- input ----------
    def handle_event(self, event):
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            for b in self.control_btns:
                b.is_hovered(event)
                if b.is_clicked(event):
                    label = b.text.strip().lower()
                    if label in ("stop/resume", "stop/start"):
                        self.toggle_pause()
                    elif label == "restart":
                        self.restart()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.toggle_pause()
            elif event.key == pygame.K_r:
                self.restart()

    # ---------- drawing ----------
    def _draw_banner(self, screen):
        if pygame.time.get_ticks() > self.banner_until or not self.banner_text:
            return
        surf = FONT_S3.render(self.banner_text, True, WHITE)
        pad = 8
        rect = surf.get_rect(midtop=(SCREEN_WIDTH // 2, 8))
        bg = pygame.Rect(rect.x - pad, rect.y - pad, rect.w + 2*pad, rect.h + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, DED_GREEN, bg, 2)
        screen.blit(surf, rect)

    def _draw_temp_box(self, screen):
        if not self.temp_visible:
            return
        # base rect for TEMP (computed from array layout)
        r = self.temp_pos
        pygame.draw.rect(screen, DED_GREEN, r)
        cap = FONT_S4.render("TEMP", True, WHITE)
        screen.blit(cap, cap.get_rect(midbottom=(r.centerx, r.top - 6)))

        # key value text
        if self.key is not None:
            kv = FONT_S2.render(str(self.key), True, WHITE)
            screen.blit(kv, kv.get_rect(center=r.center))



    def _draw_array(self, screen, highlight=None):
        arr = self.array
        values, rects, ids = arr.values, arr.rects, arr.id_rects
        n = len(values)

        # compute a nice TEMP location the first time we draw
        if self.temp_pos is None and n > 0:
            # center TEMP under the middle of the array row
            mid = rects[n // 2]
            w, h = mid.w, mid.h
            self.temp_pos = pygame.Rect((mid.centerx - w//2)+140, mid.bottom + 80, w, h)

        write_k = (self.j + 1) if self.phase in ("shift", "place") else None

        for k, rect in enumerate(rects):
            # color priority
            if self.swapping and (k == self.swap_a or k == self.swap_b):
                border = PURPLE
            elif k < self.i and not (self.phase == "load" and k == self.i):  # sorted prefix except the “hole”
                border = L_GREEN
            elif highlight is not None and k == highlight:
                border = self.color_j
            elif write_k is not None and k == write_k:
                border = self.color_w
            elif self.phase == "load" and k == self.i:
                border = self.color_i
            else:
                border = DED_GREEN

            # draw cell; if we are in LOAD, hollow out the i-cell (value lifted to TEMP)
            if self.phase == "load" and k == self.i and self.temp_visible:
                pygame.draw.rect(screen, border, rect)
                # do NOT draw the number; show the gap
            else:
                pygame.draw.rect(screen, border, rect)
                txt = (FONT_S2 if arr.size < 10 else FONT_S3).render(str(values[k]), True, WHITE)
                screen.blit(txt, txt.get_rect(center=rect.center))

            # index mini-box
            idr = ids[k]
            pygame.draw.rect(screen, border, idr)
            idx = FONT_S4.render(str(k), True, WHITE)
            screen.blit(idx, idx.get_rect(center=idr.center))


        # TEMP box 
        self._draw_temp_box(screen)
        

        # controls + banner
        for b in self.control_btns:
            b.display(screen)
        self._draw_banner(screen)

    # ---------- logic: one step per frame ----------
    def update_and_draw(self, screen):
        values = self.array.values
        n = len(values)

        # highlight current j while shifting; highlight i while loading
        highlight = self.j if self.phase in ("shift",) else (self.i if self.phase == "load" else None)
        self._draw_array(screen, highlight=highlight)

        # pause/finish/flash timing
        if not self.running or self.paused or self.done:
            return

        # drop swap flash after timeout
        if self.swapping and pygame.time.get_ticks() > self.swap_flash_until:
            self.swapping = False

        now = pygame.time.get_ticks()
        if now - self.last_step_ms < self.array.interval:
            return
        self.last_step_ms = now

        # state machine
        if self.phase == "load":
            if self.i >= n:
                self.running = False
                self.done = True
                self._set_banner("Done.", 1200)
                return

            # take value into TEMP, create “hole” at i
            self.key = values[self.i]
            self.temp_visible = True
            self.j = self.i - 1
            # arrow: from the i-cell to TEMP
            cell = self.array.rects[self.i]
            self.phase = "shift"

        elif self.phase == "shift":
            if self.j >= 0 and values[self.j] > self.key:
                # shift j -> j+1
                old_j, new_j = self.j, self.j + 1
                values[new_j] = values[old_j]
                self._flash(old_j, new_j, ms=350)
                # arrow j -> j+1
                rj  = self.array.rects[old_j]
                rj1 = self.array.rects[new_j]
    
                self.j -= 1
            else:
                self.phase = "place"

        elif self.phase == "place":
            write_pos = self.j + 1
            values[write_pos] = self.key
            # arrow TEMP -> write_pos
            wr = self.array.rects[write_pos]

            self._flash(write_pos, self.i, ms=450)

            # clear TEMP & advance outer loop
            self.temp_visible = False
            self.i += 1
            self.phase = "load"


