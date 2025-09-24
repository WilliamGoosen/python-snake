import pygame as pg
from snake import Snake

pg.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
start_x = SCREEN_WIDTH // 2
start_y = SCREEN_HEIGHT //2
snake_speed: int = 10
snake_collided: bool = False
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake!!!")
clock = pg.time.Clock()
snake = Snake(start_x, start_y)

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
                
    # --- Updates ---
    move_timer += dt
    if not snake_collided and move_timer > 1 / snake_speed:
        snake_collided = snake.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        move_timer = 0
    
    # --- Draw to the Screen
    screen.fill("white")
    
    snake.draw(screen)
    
    
    pg.display.flip()
pg.quit()