import pygame as pg
from collections import deque

class Snake():
    def __init__(self, start_x: int, start_y: int, segment_size: int = 20):
        self.segment_size = segment_size
        self.body: deque = deque([
            (start_x, start_y),
            (start_x - segment_size, start_y),
            (start_x - segment_size * 2, start_y)])
        self.direction = "right"
        
    def move(self, width: int, height: int, new_direction: str = "right") -> deque:
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            head = self.body[0]
            if self.body[0][0] <= 0:
                new_head = (0, head[1])
            else:
                new_head = (head[0] - 20, head[1])
                self.body.appendleft(new_head)
                self.body.pop()

        elif keystate[pg.K_RIGHT]:
            head = self.body[0]
            if self.body[0][0] >= width - 20:
                new_head = (width - 20, head[1])
            else:
                new_head = (head[0] + 20, head[1])
                self.body.appendleft(new_head)
                self.body.pop()

        elif keystate[pg.K_UP]:
            head = self.body[0]
            if self.body[0][1] <= 0:
                new_head = (head[0], 0)
            else:
                new_head = (head[0], head[1] - 20)
                self.body.appendleft(new_head)
                self.body.pop()

        elif keystate[pg.K_DOWN]:
            head = self.body[0]
            if self.body[0][1] >= height - 20:
                new_head = (head[0], height - 20)
            else:
                new_head = (head[0], head[1] + 20)
                self.body.appendleft(new_head)
                self.body.pop()

        return self.body
    
    def draw(self, screen: pg.Surface) -> None:
        for index, coord in enumerate(self.body):
            if index == 0:
                pg.Surface.fill(screen, "red", (coord[0], coord[1], 20, 20))
            else:
                pg.Surface.fill(screen, "green", (coord[0], coord[1], 20, 20))