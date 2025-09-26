import pygame as pg
from pathlib import Path

class GraphicsManager:
    """A class to manage the loading and storage of graphics assets."""
    def __init__(self) -> None:
        PROJECT_ROOT = Path(__file__).parent
        IMG_DIR = PROJECT_ROOT / "img"
        self.snake_spritesheet = pg.image.load(IMG_DIR / "snake_sheet.png").convert_alpha()
        self.snake_head_left = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 0, 0, 40, 40), 0.5)
        self.snake_head_right = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 40, 40, 40, 40), 0.5)
        self.snake_head_up = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 40, 0, 40, 40), 0.5)
        self.snake_head_down = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 0, 40, 40, 40), 0.5)
        self.snake_tail_left = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 40, 80, 40, 40), 0.5)
        self.snake_tail_right = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 40, 120, 40, 40), 0.5)
        self.snake_tail_up = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 0, 80, 40, 40), 0.5)
        self.snake_tail_down = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 0, 120, 40, 40), 0.5)
        self.snake_horizontal = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 80, 80, 40, 40), 0.5)
        self.snake_vertical = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 80, 120, 40, 40), 0.5)
        self.snake_NW = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 80, 0, 40, 40), 0.5)
        self.snake_NE = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 120, 0, 40, 40), 0.5)
        self.snake_SW = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 80, 40, 40, 40), 0.5)
        self.snake_SE = pg.transform.scale_by(self.get_sprite(self.snake_spritesheet, 120, 40, 40, 40), 0.5)
        


    def get_sprite(self, sheet: pg.Surface, x: int, y: int, width: int, height: int) -> pg.Surface:
        # Create a new surface for the individual sprite
        sprite_surface = pg.Surface((width, height), pg.SRCALPHA) 

        # Blit the desired portion of the spritesheet onto the new surface
        sprite_surface.blit(sheet, (0, 0), (x, y, width, height))
        return sprite_surface