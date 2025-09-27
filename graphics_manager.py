import pygame as pg
from pathlib import Path
from settings import SNAKE_SPRITES, FOOD_SPRITES

class GraphicsManager:
    """A class to manage the loading and storage of graphics assets."""
    def __init__(self, scale_factor: float = 0.5) -> None:
        PROJECT_ROOT = Path(__file__).parent
        IMG_DIR = PROJECT_ROOT / "img"
        self.scale_factor = scale_factor
        self.snake_spritesheet = pg.image.load(IMG_DIR / "snake_sheet.png").convert_alpha()
        self.snake_sprites: dict = {}
        self.food_sprites: dict = {}
        self._load_snake_sprites()
        self._load_food_sprites()
        

    def get_sprite(self, sheet: pg.Surface, x: int, y: int, width: int, height: int) -> pg.Surface:
        # Create a new surface for the individual sprite
        sprite_surface = pg.Surface((width, height), pg.SRCALPHA) 

        # Blit the desired portion of the spritesheet onto the new surface
        sprite_surface.blit(sheet, (0, 0), (x, y, width, height))
        return sprite_surface
    
    
    def _load_snake_sprites(self):
        for name, config in SNAKE_SPRITES.items():
            sprite = self.get_sprite(self.snake_spritesheet, config["x"], config["y"], config["width"], config["height"])
            self.snake_sprites[name] = pg.transform.scale_by(sprite, config["scale"])


    def _load_food_sprites(self):
        for name, config in FOOD_SPRITES.items():
            sprite = self.get_sprite(self.snake_spritesheet, config["x"], config["y"], config["width"], config["height"])
            self.food_sprites[name] = pg.transform.scale_by(sprite, config["scale"])