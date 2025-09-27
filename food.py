import pygame as pg
from random import choice
from collections import deque
from settings import SEGMENT_SIZE, WHITE
from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    from game_data import Game

class Food():
    def __init__(self, game: 'Game'):
        self.game = game
        self.apple_sprite = game.graphics_manager.food_sprites['apple']
        self.food_position: tuple = (0, 0)
        self.colour: tuple = (255, 255, 255)
        self.radius: int = 5
        self.segment_size = SEGMENT_SIZE


    def spawn(self, game_grid: list, snake_body: deque) -> None:
        
        if len(snake_body) < 100:
            while True:
                spawn_coord: tuple = choice(game_grid)
                if spawn_coord not in snake_body:
                    self.food_position = spawn_coord
                    break
        
        else:
            grid_set: set = set(game_grid)
            snake_body_set: set = set(snake_body)
            free_spot = grid_set - snake_body_set
            self.food_position = choice(list(free_spot))

            
    def draw(self, screen: pg.Surface) -> None:
        pass


class Pellet(Food):
    def __init__(self, game: 'Game',colour: tuple = WHITE, radius: int = 5):
        super().__init__(game)
        self.colour = colour
        self.radius = radius

    def spawn(self, game_grid: list, snake_body: deque) -> None:
        return super().spawn(game_grid, snake_body)
    
    def draw(self, screen: pg.Surface) -> None:
        segment_offset: float = self.segment_size / 2
        x_pos: float = self.food_position[0] + segment_offset
        y_pos: float = self.food_position[1] + segment_offset
        pg.draw.circle(screen, self.colour, (x_pos, y_pos), self.radius)
    

class Apple(Food):
    def __init__(self, game: 'Game'):
        super().__init__(game)
        
    def spawn(self, game_grid: list, snake_body: deque) -> None:
        return super().spawn(game_grid, snake_body)

    def draw(self, screen: pg.Surface) -> None:        
        screen.blit(self.apple_sprite, self.food_position)