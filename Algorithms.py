import pygame
pygame.init()
from UIProperties import *
from Buttons import Button  
from Arrays import *
import time, random
random.seed(time.time()) #SEEEEDDD, NVM


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

class Searching_Algos:

    def __init__(self):
            self.algo_btns=[
            Button(170, 100, r"DSA_Visualizer\B_Purp.png", "Linear Search",48, 510, 255),
            Button(170, 300, r'DSA_Visualizer\B_Pink.png', "Binary Search", 48, 510, 255)
        ]

    def Draw(self, screen):
        txt = "Choose type of search to visualize."
        screen.blit(FONT_S2.render(txt, True, BLACK_1, YELLOW), (60, 70))
        for btn in self.algo_btns:
            btn.display(screen)
class Binary_Search:
    def __init__(self):
        self.array = Array()
        self.array.dataType = int
        self.array.size = 12
        # build the first dataset & remember it
        self.array.values = sorted(random.sample(range(0, 100), self.array.size))
        self.base_values = self.array.values[:]           # <— remember baseline data
        self.array.InitializeRects()

        # animation state
        self.running = False
        self.paused  = False
        self.done    = False
        self.last_step_ms = 0

        self.low  = 0
        self.high = self.array.size - 1
        self.mid  = self.array.size // 2
        self.target = None

        self.control_btns = [
            Button(20, 520,  r'DSA_Visualizer\B_Pink.png', "Start",   28, 160, 80),
            Button(190, 520, r'DSA_Visualizer\B_Pink.png', "Restart", 28, 160, 80),
        ]

        self.banner_text  = ""
        self.banner_until = 0

        self.tgt_box     = pygame.Rect(SCREEN_WIDTH - 180, 12, 140, 40)
        self.tgt_active  = False
        self.tgt_text    = ""
        self.n = self.array.size

    # ---------- helpers ----------
    def _set_banner(self, msg, ms):
        self.banner_text  = msg
        self.banner_until = pygame.time.get_ticks() + ms

    def _draw_banner(self, screen):
        if not self.banner_text or pygame.time.get_ticks() > self.banner_until:
            return
        surf = FONT_S3.render(self.banner_text, True, WHITE)
        pad  = 8
        rect = surf.get_rect(midtop=(SCREEN_WIDTH // 2, 8))
        bg   = pygame.Rect(rect.x - pad, rect.y - pad, rect.w + 2*pad, rect.h + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, DED_GREEN, bg, 2)
        screen.blit(surf, rect)

    # ---------- lifecycle ----------
    def _reset_state(self):
        self.low  = 0
        self.high = self.n - 1
        self.mid  = None
        self.running = True
        self.paused  = False
        self.done    = False

    def start(self, target=None):
        """Start with a NEW (sorted) random array unless target was typed already."""
        # create new data and remember it
        self.array.values = sorted(random.sample(range(0, 100), self.n))
        self.base_values  = self.array.values[:]                # <— remember dataset
        self.array.InitializeRects()

        # set target
        if target is None and self.tgt_text.strip().isdigit():
            self.target = int(self.tgt_text)
        elif target is not None:
            self.target = target
        elif self.target is None:
            return

        self._reset_state()
        self._set_banner(f"Starting Binary Search for {self.target}", 2500)

    def restart(self):
        """Re-run on the SAME array; reset colors and pointers."""
        self.array.values = self.base_values[:]                 
        self.array.InitializeRects()                                                                # reset target text
        self._reset_state()
        self._set_banner("Restarted on same array", 1600)
        self.tgt_text = ""
        self.target = None
        self.mid = self.n // 2


    def toggle_pause(self):
       
        t = int(self.tgt_text) if self.tgt_text.strip().isdigit() else None
        self.start(t)

    # ---------- input ----------
    def handle_event(self, event):
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            for b in self.control_btns:
                b.is_hovered(event)
                if b.is_clicked(event):
                    label = b.text.strip().lower()
                    if label == "start":
                        self.toggle_pause()
                    elif label == "restart":
                        self.restart()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.tgt_active = self.tgt_box.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN:
            if self.tgt_active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.target = int(self.tgt_text.strip())
                        self._set_banner(f"Target set to {self.target}", 1400)
                    except:
                        self._set_banner("Invalid target", 1200)
                elif event.key == pygame.K_BACKSPACE:
                    self.tgt_text = self.tgt_text[:-1]
                else:
                    self.tgt_text += event.unicode
            if event.key == pygame.K_SPACE:
                self.toggle_pause()
            elif event.key == pygame.K_r:
                self.restart()


    # ---------- drawing ----------
    def _draw_array(self, screen):
        vals, rects, ids = self.array.values, self.array.rects, self.array.id_rects

        for k, rect in enumerate(rects):
            # color by role
            if self.mid is not None and k == self.mid:
                border = L_RED
            elif self.low is not None and self.high is not None and self.low <= k <= self.high:
                border = DED_GREEN
            else:
                border = GREY_2

            pygame.draw.rect(screen, border, rect)
            txt = (FONT_S2 if self.array.size < 10 else FONT_S3).render(str(vals[k]), True, WHITE)
            screen.blit(txt, txt.get_rect(center=rect.center))

            # index box
            idr = ids[k]
            pygame.draw.rect(screen, border, idr)
            idx = FONT_S4.render(str(k), True, WHITE)
            screen.blit(idx, idx.get_rect(center=idr.center))

        # show low/high/mid tags (if defined)
        def tag(k, label, col):
            if k is None or k < 0 or k >= len(rects): return
            r = rects[k]
            t = FONT_S4.render(label, True, col)
            screen.blit(t, t.get_rect(midbottom=(r.centerx, r.top - 6)))

        tag(self.low,  "Low", L_GREEN)
        tag(self.high, "High", PINK)
        tag(self.mid,  "Mid", L_RED)

    def _draw_target_box(self, screen):
        # label
        lab = FONT_S4.render("Target:", True, WHITE)
        screen.blit(lab, (self.tgt_box.x - lab.get_width() - 8, self.tgt_box.y + 8))

        # box
        pygame.draw.rect(screen, self.array.color_active if self.tgt_active else self.array.color_inactive, self.tgt_box, 2)
        txt = FONT_S3.render(self.tgt_text, True, WHITE)
        screen.blit(txt, (self.tgt_box.x + 5, self.tgt_box.y + 6))

    def update_and_draw(self, screen):
        # draw everything first
        self._draw_array(screen)
        for b in self.control_btns:
            b.display(screen)
        self._draw_target_box(screen)
        self._draw_banner(screen)
        if self.target is  None:
            return

        if not self.running or self.paused or self.done:
            return

        # throttle by array.interval
        now = pygame.time.get_ticks()
        if now - self.last_step_ms < self.array.interval:
            return
        self.last_step_ms = now

        # if no target yet, pick typed one (or keep the one set at start)
        if self.target is None and self.tgt_text.strip().isdigit():
            self.target = int(self.tgt_text.strip())

        # guard
        if self.low > self.high:
            self.running = False
            self.done = True
            self._set_banner("Not found", 1800)
            return

        # step: compute mid, compare, shrink range
        self.mid = (self.low + self.high) // 2
        mid_val = self.array.values[self.mid]

        if mid_val == self.target:
            self.running = False
            self.done = True
            self._set_banner(f"Found at index {self.mid}", 2200)
        elif mid_val < self.target:
            self.low = self.mid + 1
        else:
            self.high = self.mid - 1
class Linear_Search:
    def __init__(self):
        self.array = Array()
        self.array.dataType = int
        self.array.size = 12
        # fill with random values; mark the used length
        self.array.values = [random.randint(0, 99) for _ in range(self.array.size)]
        self.array.current_Count = self.array.size
        self.array.InitializeRects()

        self.target = None
        self.running = False
        self.banner_text = ""
        self.banner_until = 0
        self.last_step_ms = 0

        # controls + target box (same placement as Binary Search for consistency)
        self.control_btns = [
            Button(20, 520,  r'DSA_Visualizer\B_Pink.png', "Start",   28, 160, 80),
            Button(190, 520, r'DSA_Visualizer\B_Pink.png', "Restart", 28, 160, 80),
        ]
        self.tgt_box = pygame.Rect(SCREEN_WIDTH - 180, 12, 140, 40)
        self.tgt_active = False
        self.tgt_text = ""

        # remember dataset for “Restart”
        self.base_values = self.array.values[:]

    def _set_banner(self, msg, ms):
        self.banner_text = msg
        self.banner_until = pygame.time.get_ticks() + ms

    def _draw_banner(self, screen):
        if not self.banner_text or pygame.time.get_ticks() > self.banner_until:
            return
        surf = FONT_S3.render(self.banner_text, True, WHITE)
        pad  = 8
        rect = surf.get_rect(midtop=(SCREEN_WIDTH // 2, 8))
        bg   = pygame.Rect(rect.x - pad, rect.y - pad, rect.w + 2*pad, rect.h + 2*pad)
        pygame.draw.rect(screen, BLACK_1, bg)
        pygame.draw.rect(screen, DED_GREEN, bg, 2)
        screen.blit(surf, rect)

    def start(self, target=None):
        # set target
        if target is None and self.tgt_text.strip().isdigit():
            self.target = int(self.tgt_text)
        elif target is not None:
            self.target = target
        elif self.target is None:
            return

        # kick the existing engine; IMPORTANT: turn off delete mode for pure search
        self.array.start_linear_search(self.target)
        self.array.delete_pending = False
        self.running = True
        self._set_banner(f"Starting Linear Search for {self.target}", 2000)

    def restart(self):
        # same dataset
        self.array.values = self.base_values[:]
        self.array.current_Count = len(self.array.values)
        self.array.InitializeRects()
        # reset the internal engine state
        self.array.search_active = False
        self.array.highlight_index = None
        self.array.highlight_start = 0
        self.array.search_i = 0
        self.array.message = ""
        self.tgt_text = ""
    
        self.array.message_until = 0
        self.array.flash_all_until = 0
        self.running = False
        self._set_banner("Restarted on same array", 1400)

    def handle_event(self, event):
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            for b in self.control_btns:
                b.is_hovered(event)
                if b.is_clicked(event):
                    label = b.text.strip().lower()
                    if label == "start":
                        t = int(self.tgt_text) if self.tgt_text.strip().isdigit() else None
                        self.start(t)
                    elif label == "restart":
                        self.restart()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.tgt_active = self.tgt_box.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN:
            if self.tgt_active:
                if event.key == pygame.K_RETURN:
                    try:
                        self.target = int(self.tgt_text.strip())
                        self._set_banner(f"Target set to {self.target}", 1200)
                    except:
                        self._set_banner("Invalid target", 1200)
                elif event.key == pygame.K_BACKSPACE:
                    self.tgt_text = self.tgt_text[:-1]
                else:
                    self.tgt_text += event.unicode

            if event.key == pygame.K_SPACE:
                t = int(self.tgt_text) if self.tgt_text.strip().isdigit() else None
                self.start(t)
            elif event.key == pygame.K_r:
                self.restart()

    def _draw_target_box(self, screen):
        lab = FONT_S4.render("Target:", True, WHITE)
        screen.blit(lab, (self.tgt_box.x - lab.get_width() - 8, self.tgt_box.y + 8))
        pygame.draw.rect(
            screen,
            self.array.color_active if self.tgt_active else self.array.color_inactive,
            self.tgt_box,
            2
        )
        txt = FONT_S3.render(self.tgt_text, True, WHITE)
        screen.blit(txt, (self.tgt_box.x + 5, self.tgt_box.y + 6))

    def _draw_array_simple(self, screen):
        """A lightweight drawer that mirrors Arrays.drawInterface highlights
           without the insert/delete UI."""
        now = pygame.time.get_ticks()
        flash_all = now < self.array.flash_all_until

        for i, rect in enumerate(self.array.rects):
            if flash_all:
                color = D_GREEN
            elif (i == self.array.highlight_index and now - self.array.highlight_start < self.array.interval):
                color = D_RED
            else:
                color = D_GREEN

            pygame.draw.rect(screen, color, rect)
            # value
            if self.array.values[i] is not None:
                txt = (FONT_S2 if self.array.size < 10 else FONT_S3).render(str(self.array.values[i]), True, WHITE)
                screen.blit(txt, txt.get_rect(center=rect.center))

        for i, rect in enumerate(self.array.id_rects):
            pygame.draw.rect(screen, L_GREEN, rect)
            idx = FONT_S4.render(str(i), True, WHITE)
            screen.blit(idx, idx.get_rect(center=rect.center))

        # message from Array engine (Found/Not found)
        if self.array.message and now < self.array.message_until:
            screen.blit(FONT_S2.render(self.array.message, True, WHITE), (25, 130))

    def update_and_draw(self, screen):
        # advance the engine
        self.array.step_linear_search()

        # draw
        self._draw_array_simple(screen)
        for b in self.control_btns:
            b.display(screen)
        self._draw_target_box(screen)
        self._draw_banner(screen)

