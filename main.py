import pygame as pg
from pathlib import Path
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_NAME, HS_FILE, SEGMENT_SIZE, TOP_BAR_HEIGHT, BLACK
from game_data import Game
from graphics_manager import GraphicsManager
from snake import Snake
from food import Pellet
from states import BaseState, TitleState, PlayState, GameOverState
from utilities import load_or_create_file

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

game = Game()
game.graphics_manager = GraphicsManager()
game.high_score = int(load_or_create_file(hs_file, '0'))
game.score = 0
current_state: BaseState = TitleState(game, font_name)

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
        snake: Snake = Snake(game)
        pellet: Pellet = Pellet()
        pellet.spawn(GRID_COORDS, snake.body)
        game.score = 0
        current_state = PlayState(snake, pellet, GRID_COORDS, game, font_name, hs_file)
    elif current_state.next_state == "GAME_OVER":
            current_state = GameOverState(game)
    elif current_state.next_state == "TITLE":
            current_state = TitleState(game, font_name)


   
    # --- Draw to the Screen
    screen.fill(BLACK)
    
    current_state.draw(screen)

    pg.display.flip()
pg.quit()