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
        
    def change_direction(self, new_direction: str):
        opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction
        
    def move(self, width: int, height: int) -> bool:
        head = self.body[0]
        x: int= head[0]
        y: int = head[1]
        
        if self.direction == "left":
            # if x <= 0:
            #     new_head = (0, y)
            # else:
                new_head = (x - 20, y)
                # self.body.appendleft(new_head)
                # self.body.pop()

        elif self.direction == "right":
            # if x >= width - 20:
            #     new_head = (width - 20, y)
            # else:
                new_head = (x + 20, y)
                # self.body.appendleft(new_head)
                # self.body.pop()

        elif self.direction == "up":
            # if y <= 0:
            #     new_head = (x, 0)
            # else:
                new_head = (x, y - 20)
                # self.body.appendleft(new_head)
                # self.body.pop()

        elif self.direction == "down":
            # if y >= height - 20:
            #     new_head = (x, height - 20)
            # else:
                new_head = (x, y + 20)
                # self.body.appendleft(new_head)
                # self.body.pop()
                
        # if self._check_collision(new_head):
        #     return False
        if x <= 0 or x >= width - 20 or y <= 0 or y >= height - 20:
            print("You scrashed into a wall!!!")
            return False

        if self._check_self_collision(new_head):
            print("You crashed into yourself!!!")
            return False
        
        
        self.body.appendleft(new_head)
        self.body.pop()
        return True

    # def _check_collision(self, position: tuple) -> bool:
    #     x: int= position[0]
    #     y: int = position[1]
    #     return x <= 0 or x >= width - 20
        
    def _check_self_collision(self, position: tuple) -> bool:
        return position in self.body
    
    def draw(self, screen: pg.Surface) -> None:
        for index, coord in enumerate(self.body):
            if index == 0:
                pg.Surface.fill(screen, "red", (coord[0], coord[1], 20, 20))
            else:
                pg.Surface.fill(screen, "green", (coord[0], coord[1], 20, 20))