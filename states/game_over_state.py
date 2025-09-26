import pygame as pg
from states.base_state import BaseState
from utilities import draw_text, draw_confirm_popup, new_high_score_check
from settings import *
from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    from game_data import Game

class GameOverState(BaseState):
    def __init__(self, game: 'Game'):
        super().__init__()
        self.game = game
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.font_name = pg.font.match_font(FONT_NAME)
        self.show_confirmation = False
        self.pending_action = None
        
    
    def startup(self):
        super().startup()
    
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if self.show_confirmation:
                if event.key == pg.K_y:
                    if self.pending_action == "quit_game":
                        self.quit = True
                        self.done = True
                    self.show_confirmation = False
                    self.pending_action = None
                
                elif event.key == pg.K_n or event.key == pg.K_ESCAPE:
                    self.show_confirmation = False
                    self.pending_action = None
                    
            else:                 
                if event.key == pg.K_q:
                    self.pending_action = "quit_game"
                    self.show_confirmation = True

                elif event.key == pg.K_ESCAPE:
                    self.done = True
                    self.next_state = "TITLE"
                elif event.key == pg.K_r:                   
                    self.done = True
                    self.next_state = "PLAY"   
    
    def draw(self, surface):
        surface.fill(TITLE_SCREEN_BG)
        self.draw_game_over_title(surface)
        if self.show_confirmation:
            draw_confirm_popup(surface, self.screen_width, self.screen_height, self.font_name)
    
    def draw_game_over_title(self, surface):
        scale_factor = 1
        screen_width = self.screen_width
        screen_height = self.screen_height

        draw_text(surface, "High Score: " + str(self.game.high_score), round(22 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.02), self.font_name)
        draw_text(surface, "GAME OVER", round(48 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.25), self.font_name)
        draw_text(surface, "Score: " + str(self.game.score), round(30 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.4), self.font_name)

        # if new_high_score_check():
        #     draw_text(surface, "NEW HIGH SCORE!", round(30 * scale_factor), screen_width / 2, screen_height * 2 / 5, self.game.font_name, GREEN)

        # draw_icon(surface, self.game.graphics_manager.icons["spacebar_icon"], icon_x, icon_y)
        # draw_icon_text(surface, "Try Again", round(22 * scale_factor), text_x, text_y, self.game.font_name)
        draw_text(surface, "Press R to try again", round(22 * scale_factor), round(screen_width * 0.5), round(screen_height * 0.7), self.font_name)

        # draw_icon(surface, self.game.graphics_manager.icons["esc_icon"], screen_width * 0.07, screen_height * 0.92)
        # draw_icon_text(surface, "Quit to Title", round(18 * scale_factor), screen_width * 0.11, screen_height * 0.940, self.game.font_name)
        draw_text(surface, "ESC: Quit to Title", round(18 * scale_factor), round(screen_width * 0.05), round(screen_height * 0.940), self.font_name, align_x="left")

        # draw_icon(surface, self.game.graphics_manager.icons["q_icon"], screen_width * 0.93, screen_height * 0.92)
        # draw_icon_text(surface, "Quit Game", round(18 * scale_factor), screen_width * 0.770, screen_height * 0.940, self.game.font_name)
        draw_text(surface, "Q: Quit Game", round(18 * scale_factor), round(screen_width * 0.950), round(screen_height * 0.940), self.font_name, align_x="right")

