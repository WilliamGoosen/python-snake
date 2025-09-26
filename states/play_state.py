import pygame as pg
from states.base_state import BaseState
from utilities import draw_text, new_high_score_check
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT, CHARCOAL, BORDER_GRAY, TEXT_WHITE, HS_FILE
from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    from pathlib import Path
    from snake import Snake
    from food import Pellet

class PlayState(BaseState):
    def __init__(self, snake: 'Snake', pellet: 'Pellet', grid_coords: list, score: int, high_score: int, font_name: str, hs_file: 'Path'):
        super().__init__()
        self.snake = snake
        self.pellet = pellet
        self.grid_coords = grid_coords
        self.score = score
        self.high_score = high_score
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.top_bar_height = TOP_BAR_HEIGHT
        self.font_name = font_name
        self.hs_file = hs_file

    def startup(self):
        super().startup()
        
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
                self.quit = True
            if event.key == pg.K_LEFT:
                self.snake.change_direction("left")
            if event.key == pg.K_RIGHT:
                self.snake.change_direction("right")
            if event.key == pg.K_UP:
                self.snake.change_direction("up")
            if event.key == pg.K_DOWN:
                self.snake.change_direction("down")

    def update(self, dt):
        self.snake.update(dt)

        if self.snake.snake_collided:
            # confirm_popup = True
            new_high_score_check(self.hs_file, self.score, self.high_score)

        if self.snake.head() == self.pellet.food_position:
            self.score += 1
            self.snake.grow()
            self.pellet.spawn(self.grid_coords, self.snake.body)


    def draw(self, surface) -> None:
        self.draw_ui(surface, CHARCOAL, BORDER_GRAY, TEXT_WHITE, self.font_name)
        self.snake.draw(surface)
        self.pellet.draw(surface)


    def draw_ui(self, surface, bar_colour: tuple, border_colour: tuple, text_colour: tuple, font_name: str) -> None:
        top_bar_rect: tuple = (0, 0, self.screen_width, self.top_bar_height)
        x, y, width, height = top_bar_rect
        pg.Surface.fill(surface, bar_colour, top_bar_rect)
        line_width = 2
        bottom_y = y + height - line_width
        pg.draw.line(surface, border_colour, (x, bottom_y), (x + width, bottom_y), line_width)
        draw_text(surface, f"SCORE: {self.score}", 22, x + width * 0.01, height * 0.5, font_name, text_colour, align_x="left", align_y="center")
        draw_text(surface, f"HIGH SCORE: {self.score if self.score > self.high_score else self.high_score}", 22, width * 0.99, height * 0.5, font_name, text_colour, align_x="right", align_y="center")