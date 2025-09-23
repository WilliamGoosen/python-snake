import pygame as pg
from collections import deque

pg.init()
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake!!!")
clock = pg.time.Clock()

def draw_snake(snake_list: deque):
    for index, coord in enumerate(snake_list):
        if index == 0:
            pg.Surface.fill(screen, "red", (coord[0], coord[1], 20, 20))
        else:
            pg.Surface.fill(screen, "green", (coord[0], coord[1], 20, 20))

            
def move_snake(snake_list: deque):
    keystate = pg.key.get_pressed()
    if keystate[pg.K_LEFT]:
        head = snake_list[0]
        if snake_list[0][0] <= 0:
            new_head = (0, head[1])
        else:
            new_head = (head[0] - 20, head[1])
            snake_list.appendleft(new_head)
            snake_list.pop()
    
    elif keystate[pg.K_RIGHT]:
        head = snake_list[0]
        if snake_list[0][0] >= SCREEN_WIDTH - 20:
            new_head = (SCREEN_WIDTH - 20, head[1])
        else:
            new_head = (head[0] + 20, head[1])
            snake_list.appendleft(new_head)
            snake_list.pop()
        
    elif keystate[pg.K_UP]:
        head = snake_list[0]
        if snake_list[0][1] <= 0:
            new_head = (head[0], 0)
        else:
            new_head = (head[0], head[1] - 20)
            snake_list.appendleft(new_head)
            snake_list.pop()
        
    elif keystate[pg.K_DOWN]:
        head = snake_list[0]
        if snake_list[0][1] >= SCREEN_HEIGHT - 20:
            new_head = (head[0], SCREEN_HEIGHT - 20)
        else:
            new_head = (head[0], head[1] + 20)
            snake_list.appendleft(new_head)
            snake_list.pop()
        
    return snake_list

snake_body = deque([(360, 320), (340, 320), (320, 320), (320, 300), (320, 280)])
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
    
    draw_snake(snake_body)
    snake_body = move_snake(snake_body)
    
    #Draw to screen
    
    pg.display.flip()
pg.quit()