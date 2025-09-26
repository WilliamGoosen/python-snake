import pygame as pg
from pathlib import Path
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_NAME, HS_FILE, SEGMENT_SIZE, TOP_BAR_HEIGHT, BLACK
from snake import Snake
from food import Pellet
from states import BaseState, TitleState, PlayState
from utilities import load_or_create_file, draw_confirm_popup

pg.init()

font_name = pg.font.match_font(FONT_NAME)
hs_file: Path = Path(HS_FILE)

# Generate all grid coordinates (20px segments)
# Advanced one-liner: [(x, y) for x in range(0, SCREEN_WIDTH, 20) 
#                           for y in range(0, SCREEN_HEIGHT, 20)]
GRID_COORDS: list = []
for x in range(0, SCREEN_WIDTH, SEGMENT_SIZE):
    for y in range(TOP_BAR_HEIGHT, SCREEN_HEIGHT, SEGMENT_SIZE):
        GRID_COORDS.append((x,y))

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake!!!")
clock = pg.time.Clock()
snake: Snake = Snake()
pellet: Pellet = Pellet()
pellet.spawn(GRID_COORDS, snake.body)

high_score: int = int(load_or_create_file(hs_file, '0'))
score: int = 0
confirm_popup = False
current_state: BaseState = TitleState(high_score, SCREEN_WIDTH, SCREEN_HEIGHT, font_name)

running = True
while running:
    
    dt = clock.tick(60) / 1000
    
    # --- Event Handling ---
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        current_state.get_event(event)

    current_state.update(dt)

    if current_state.done:
        if current_state.quit:
            running = False
            continue

    if current_state.next_state == "PLAY":
        current_state = PlayState(snake, pellet, GRID_COORDS, score, high_score, font_name, hs_file)


# --- Updates ---


    
    
    # --- Draw to the Screen
    screen.fill(BLACK)

    
    
    if confirm_popup:
        draw_confirm_popup(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font_name)
        # confirm_popup = False
    
    current_state.draw(screen)

    
    
    pg.display.flip()
pg.quit()