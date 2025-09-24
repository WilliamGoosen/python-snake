import pygame as pg


_text_cache = {}
_font_cache = {}

def draw_text(surf: pg.Surface, text: str, size: int, x: int, y: int, font_name: str, colour: tuple = (0, 0, 0), align_x: str = "left", align_y: str = "top"):
    # --- 1. CACHE THE FONT OBJECT ---
    # Create a key for the font (name + size)
    font_key = (font_name, size)
    if font_key not in _font_cache:
        _font_cache[font_key] = pg.font.Font(font_name, size)
    font = _font_cache[font_key]
    
    # --- 2. CACHE THE RENDERED TEXT SURFACE ---
    # Create a key for the specific text (font key + text + color)
    text_key = font_key + (text, colour)
    if text_key not in _text_cache:
        _text_cache[text_key] = font.render(text, True, colour)
    text_surface = _text_cache[text_key]
    
    # --- 3. BLIT THE PRE-RENDERED SURFACE (This is fast) ---
    text_rect = text_surface.get_rect()

    # Horizontal alignment
    if align_x == "left":
        text_rect.left = x
    elif align_x == "center":
        text_rect.centerx = x
    elif align_x == "right":
        text_rect.right = x
    
    # Vertical alignment  
    if align_y == "top":
        text_rect.top = y
    elif align_y == "center":
        text_rect.centery = y
    elif align_y == "bottom":
        text_rect.bottom = y
    
    surf.blit(text_surface, text_rect)