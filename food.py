import pygame as pg
from random import choice
from collections import deque

class Food():
    def __init__(self, colour: str = "white", radius: int = 5, segment_size: int = 20):
        self.food_position: tuple = (0, 0)
        self.colour = colour
        self.radius = radius
        self.segment_size = segment_size


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
        segment_offset: float = self.segment_size / 2
        x_pos: float = self.food_position[0] + segment_offset
        y_pos: float = self.food_position[1] + segment_offset
        pg.draw.circle(screen, self.colour, (x_pos, y_pos), self.radius)


class Pellet(Food):
    def __init__(self, colour: str = "white", radius: int = 5):
        super().__init__(colour, radius)

    def spawn(self, game_grid: list, snake_body: deque) -> None:
        return super().spawn(game_grid, snake_body)
    
    def draw(self, screen: pg.Surface) -> None:
        return super().draw(screen)
    

class Apple(Food):
    def __init__(self, apple_image: pg.Surface):
        super().__init__()
        self.apple_image = apple_image
        
    def spawn(self, game_grid: list, snake_body: deque) -> None:
        return super().spawn(game_grid, snake_body)

    def draw(self, screen: pg.Surface) -> None:        
        screen.blit(self.apple_image, self.food_position)


