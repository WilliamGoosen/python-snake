import pygame as pg
from collections import deque
from settings import SNAKE_BASE_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT, SEGMENT_SIZE
from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    from game_data import Game

class Snake():
    def __init__(self, game: 'Game'):
        self.game = game
        self.sprites: dict = game.graphics_manager.snake_sprites
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
        last = len(self.body) - 1

        for index, coord in enumerate(self.body):
            
            if index == 0:
                if coord[1] < self.body[1][1]:
                    screen.blit(self.sprites["head_N"], (coord[0], coord[1]))
                elif coord[1] > self.body[1][1]:
                    screen.blit(self.sprites["head_S"], (coord[0], coord[1]))
                elif coord[0] > self.body[1][0]:
                    screen.blit(self.sprites["head_E"], (coord[0], coord[1]))
                elif coord[0] < self.body[1][0]:
                    screen.blit(self.sprites["head_W"], (coord[0], coord[1]))
            # Tail orientation
            elif index == last:
                if coord[1] < self.body[last - 1][1]:
                    screen.blit(self.sprites["tail_N"], (coord[0], coord[1]))
                elif coord[1] > self.body[last - 1][1]:
                    screen.blit(self.sprites["tail_S"], (coord[0], coord[1]))
                elif coord[0] > self.body[last - 1][0]:
                    screen.blit(self.sprites["tail_E"], (coord[0], coord[1]))
                elif coord[0] < self.body[last - 1][0]:
                    screen.blit(self.sprites["tail_W"], (coord[0], coord[1]))

            # Body orientation
            elif index > 0 and index < last:
                leading = self.body[index - 1]
                current = self.body[index]
                trailing = self.body[index + 1]

                # Down and left
                if leading[0] < current[0] and current[1] > trailing[1]:
                    screen.blit(self.sprites["body_SE"], (coord[0], coord[1]))
                # Left and down
                elif leading[1] > current[1] and current[0] < trailing[0]:
                    screen.blit(self.sprites["body_NW"], (coord[0], coord[1]))
                # Left and Up
                elif leading[1] < current[1] and current[0] < trailing[0]:
                    screen.blit(self.sprites["body_SW"], (coord[0], coord[1]))
                # Down and right
                elif leading[0] > current[0] and current[1] > trailing[1]:
                    screen.blit(self.sprites["body_SW"], (coord[0], coord[1]))               
                 # Right and down
                elif leading[1] > current[1] and current[0] > trailing[0]:
                    screen.blit(self.sprites["body_NE"], (coord[0], coord[1]))
                # Up and left
                elif leading[0] < current[0] and current[1] < trailing[1]:
                    screen.blit(self.sprites["body_NE"], (coord[0], coord[1]))
                # Up and right
                elif leading[0] > current[0] and current[1] < trailing[1]:
                    screen.blit(self.sprites["body_NW"], (coord[0], coord[1]))
                # Right and up
                elif leading[1] < current[1] and current[0] > trailing[0]:
                    screen.blit(self.sprites["body_SE"], (coord[0], coord[1]))

                # Horizontal pieces
                elif leading[0] != trailing[0]:
                    screen.blit(self.sprites["body_H"], (coord[0], coord[1]))
                # Vertical pieces
                elif leading[1] != trailing[1]:
                    screen.blit(self.sprites["body_V"], (coord[0], coord[1]))