import pygame as pg
from snake import Snake

pg.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
start_x = SCREEN_WIDTH // 2
start_y = SCREEN_HEIGHT //2
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake!!!")
clock = pg.time.Clock()
snake = Snake(start_x, start_y)

running = True
while running:
    
    dt = clock.tick(60) / 1000
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            
    screen.fill("white")
    
    snake.draw(screen)
    snake.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    #Draw to screen
    
    pg.display.flip()
pg.quit()