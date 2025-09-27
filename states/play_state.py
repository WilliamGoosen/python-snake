import pygame as pg
from states.base_state import BaseState
from utilities import draw_text, new_high_score_check
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TOP_BAR_HEIGHT, CHARCOAL, BORDER_GRAY, TEXT_WHITE
from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    from pathlib import Path
    from snake import Snake
    from food import Apple
    from game_data import Game

class PlayState(BaseState):
    def __init__(self, snake: 'Snake', apple: 'Apple', grid_coords: list, game: 'Game', font_name: str, hs_file: 'Path'):
        super().__init__()
        self.snake = snake
        self.apple = apple
        self.game = game
        self.grid_coords = grid_coords
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
            self.next_state = "GAME_OVER"
            if new_high_score_check(self.hs_file, self.game.score, self.game.high_score):
                self.game.high_score = self.game.score

        if self.snake.head() == self.apple.food_position:
            self.game.score += 1
            self.snake.grow()
            self.apple.spawn(self.grid_coords, self.snake.body)


    def draw(self, surface) -> None:
        self.draw_ui(surface, CHARCOAL, BORDER_GRAY, TEXT_WHITE, self.font_name)
        self.snake.draw(surface)
        self.apple.draw(surface)


    def draw_ui(self, surface, bar_colour: tuple, border_colour: tuple, text_colour: tuple, font_name: str) -> None:
        top_bar_rect: tuple = (0, 0, self.screen_width, self.top_bar_height)
        x, y, width, height = top_bar_rect
        pg.Surface.fill(surface, bar_colour, top_bar_rect)
        line_width = 2
        bottom_y = y + height - line_width
        pg.draw.line(surface, border_colour, (x, bottom_y), (x + width, bottom_y), line_width)
        draw_text(surface, f"SCORE: {self.game.score}", 22, x + width * 0.01, height * 0.5, font_name, text_colour, align_x="left")
        draw_text(surface, f"HIGH SCORE: {self.game.score if self.game.score > self.game.high_score else self.game.high_score}", 22, width * 0.99, height * 0.5, font_name, text_colour, align_x="right")