import pygame as pg
from snake import Snake
from food import Pellet
from utilities import draw_text, load_or_create_file

def new_high_score_check(file: str, score: int, high_score: int):
    
    if score > high_score:
        high_score = score
        with open(file, "w") as f:
            f.write(str(score))
        return True
    else:
        return False   

def draw_ui(surface, score: int, high_score: int, top_bar_rect: tuple, bar_colour: tuple, border_colour: tuple, text_colour: tuple, font_name: str) -> None:
    x, y, width, height = top_bar_rect
    pg.Surface.fill(surface, bar_colour, top_bar_rect)
    bottom_y = y + height
    pg.draw.line(surface, border_colour, (x, bottom_y), (x + width, bottom_y), 2)
    draw_text(surface, f"SCORE: {score}", 22, x + width * 0.01, height * 0.5, font_name, text_colour, align_x="left", align_y="center")
    draw_text(surface, f"HIGH SCORE: {high_score}", 22, width * 0.99, height * 0.5, font_name, text_colour, align_x="right", align_y="center")

pg.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
TOP_BAR_HEIGHT = 40
SEGMENT_SIZE = 20
FONT_NAME = pg.font.match_font("arial")

HS_FILE: str = 'highscore.txt'

# Colours
CHARCOAL = (45, 55, 72)
BORDER_GRAY = (74, 85, 104)
TEXT_WHITE = (226, 232, 240)
SCREEN_COLOUR = "black"

start_x = SCREEN_WIDTH // 2
start_y = SCREEN_HEIGHT //2

# Generate all grid coordinates (20px segments)
# Advanced one-liner: [(x, y) for x in range(0, SCREEN_WIDTH, 20) 
#                           for y in range(0, SCREEN_HEIGHT, 20)]
GRID_COORDS: list = []
for x in range(0, SCREEN_WIDTH, SEGMENT_SIZE):
    for y in range(TOP_BAR_HEIGHT, SCREEN_HEIGHT, SEGMENT_SIZE):
        GRID_COORDS.append((x,y))

top_bar_rect: tuple = (0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT)
snake_speed: int = 10
snake_collided: bool = False
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake!!!")
clock = pg.time.Clock()
snake = Snake(start_x, start_y)
pellet: Pellet = Pellet()
pellet.spawn(GRID_COORDS, snake.body)

high_score = int(load_or_create_file(HS_FILE, 0))
score: int = 0
move_timer = 0

running = True
while running:
    
    dt = clock.tick(60) / 1000
    
    # --- Event Handling ---
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_LEFT:
                snake.change_direction("left")
            if event.key == pg.K_RIGHT:
                snake.change_direction("right")
            if event.key == pg.K_UP:
                snake.change_direction("up")
            if event.key == pg.K_DOWN:
                snake.change_direction("down")
    
    if snake.head() == pellet.food_position:
        score += 1
        snake.grow()
        pellet.spawn(GRID_COORDS, snake.body)


    # --- Updates ---
    move_timer += dt
    if not snake_collided and move_timer > 1 / snake_speed:
        snake_collided = snake.move(SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT)
        move_timer = 0
    else:
        new_high_score_check(HS_FILE, score, high_score)

    
    
    # --- Draw to the Screen
    screen.fill(SCREEN_COLOUR)
    draw_ui(screen, score, high_score, top_bar_rect, CHARCOAL, BORDER_GRAY, TEXT_WHITE, FONT_NAME )
    snake.draw(screen)
    pellet.draw(screen)


    
    
    pg.display.flip()
pg.quit()