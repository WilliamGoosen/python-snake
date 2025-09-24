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
        self.should_grow: bool = False

    def head(self) -> tuple:
        return self.body[0]
    
    def grow(self)-> None:
        self.should_grow = True
        
    def change_direction(self, new_direction: str):
        opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction
        
    def move(self, width: int, height: int, top_bar: int) -> bool:
        head = self.body[0]
        x: int= head[0]
        y: int = head[1]
        
        if self.direction == "left":
            new_head = (x - self.segment_size, y)

        elif self.direction == "right":
            new_head = (x + self.segment_size, y)

        elif self.direction == "up":
            new_head = (x, y - self.segment_size)

        elif self.direction == "down":
            new_head = (x, y + self.segment_size)
                
        if self._check_wall_collision(width, height, top_bar, new_head):        
            print("You scrashed into a wall!!!")
            return True

        if self._check_self_collision(new_head):
            print("You crashed into yourself!!!")
            return True
        
        
        self.body.appendleft(new_head)
        if self.should_grow:
            self.should_grow = False
        else:
            self.body.pop()
            
        return False

    def _check_wall_collision(self, width: int, height: int, top_bar: int, head_position: tuple) -> bool:
        x: int= head_position[0]
        y: int = head_position[1]
        return x < 0 or x > width - self.segment_size or y < 0 + top_bar or y > height - self.segment_size
        
    def _check_self_collision(self, position: tuple) -> bool:
        return position in self.body
    
    def draw(self, screen: pg.Surface) -> None:
        for index, coord in enumerate(self.body):
            if index == 0:
                pg.Surface.fill(screen, "red", (coord[0], coord[1], 20, 20))
            else:
                pg.Surface.fill(screen, "green", (coord[0], coord[1], 20, 20))