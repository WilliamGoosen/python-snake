import pygame as pg
from states.base_state import BaseState
from utilities import draw_text
from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    pass

class TitleState(BaseState):
    def __init__(self, high_score: int, screen_width: int, screen_height: int, font_name: str):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font_name = font_name
        self.high_score = high_score
        self.scale_factor: float = 1.00

    def startup(self):
        super().startup()

    def get_event(self, event: pg.Event) -> None:
        """Handle imput events for title state"""
        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_ESCAPE:
                self.quit = True
                self.done = True

            else:
                # Any other key (Space, Enter, etc.) was pressed. Start the game.
                self.done = True
                self.next_state = "PLAY"

    
    def draw(self, surface: pg.Surface, bg_colour: tuple) -> None:
        surface.fill(bg_colour)
        self.draw_title_menu(surface)

    def draw_title_menu(self, surface):
        scale_factor = self.scale_factor
        screen_width = self.screen_width
        screen_height = self.screen_height

        draw_text(surface, "High Score: " + str(self.high_score), round(22 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.02), self.font_name, align_x="center", align_y="center")
        draw_text(surface, "SNAKE!", round(64 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.25), self.font_name, align_x="center", align_y="center")

        draw_text(surface, "Press any key to Start", round(22 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.75), self.font_name, align_x="center", align_y="center")
