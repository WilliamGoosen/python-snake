import pygame as pg
from collections import deque
from food import Pellet
from settings import SNAKE_BASE_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT, SEGMENT_SIZE

class Snake():
    def __init__(self):
        self.start_x: int = SCREEN_WIDTH // 2
        self.start_y: int = SCREEN_HEIGHT // 2
        self.segment_size = SEGMENT_SIZE
        self.body: deque = deque([
            (self.start_x, self.start_y),
            (self.start_x - self.segment_size, self.start_y),
            (self.start_x - self.segment_size * 2, self.start_y)])
        self.direction = "right"
        self.should_grow: bool = False
        self.move_timer: float = 0
        self.snake_collided: bool = False
        self.speed: int = SNAKE_BASE_SPEED

    def update(self, dt: float) -> None:
        self.move_timer += dt
        if not self.snake_collided and self.move_timer > 1 / self.speed:
            self.snake_collided = self.move(SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT)
            self.move_timer = 0
       
    def head(self) -> tuple:
        return self.body[0]
    
    def grow(self)-> None:
        self.should_grow = True
        
    def change_direction(self, new_direction: str) -> bool:
        head_pos = self.body[0]
        neck_pos = self.body[1]

        if new_direction == "up":
            if head_pos[1] > neck_pos[1]:  # Prevent reversal from down
                return False
        elif new_direction == "down":
            if head_pos[1] < neck_pos[1]:  # Prevent reversal from up
                return False
        elif new_direction == "left":
            if head_pos[0] > neck_pos[0]:  # Prevent reversal from right
                return False
        elif new_direction == "right":
            if head_pos[0] < neck_pos[0]:  # Prevent reversal from left
                return False

        self.direction = new_direction
        return True
        
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