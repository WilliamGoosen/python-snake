TITLE = "Snake!!!"
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
SEGMENT_SIZE = 20
FPS = 60
MENU_FPS = 60
FONT_NAME = 'arial'
HS_FILE = 'highscore.txt'
CONFIG_FILE = "config.ini"

# Player attributes
SNAKE_BASE_SPEED = 10

# UI attributes
TOP_BAR_HEIGHT = 40

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
CHARCOAL = (45, 55, 72)
BORDER_GRAY = (74, 85, 104)
TEXT_WHITE = (226, 232, 240)
FOREST_GREEN = (34, 139, 34) # Forest Green
TITLE_SCREEN_BG = (0, 100, 0) # Dark Forest Green

# Snake body parts
SNAKE_SPRITES = {
    "head_W": {"x": 0, "y": 0, "width": 40, "height": 40, "scale": 0.5},
    "head_E": {"x": 40, "y": 40, "width": 40, "height": 40, "scale": 0.5},
    "head_N": {"x": 40, "y": 0, "width": 40, "height": 40, "scale": 0.5},
    "head_S": {"x": 0, "y": 40, "width": 40, "height": 40, "scale": 0.5},
    "tail_W": {"x": 40, "y": 80, "width": 40, "height": 40, "scale": 0.5},
    "tail_E": {"x": 40, "y": 120, "width": 40, "height": 40, "scale": 0.5},
    "tail_N": {"x": 0, "y": 80, "width": 40, "height": 40, "scale": 0.5},
    "tail_S": {"x": 0, "y": 120, "width": 40, "height": 40, "scale": 0.5},
    "body_H": {"x": 80, "y": 80, "width": 40, "height": 40, "scale": 0.5},
    "body_V": {"x": 80, "y": 120, "width": 40, "height": 40, "scale": 0.5},
    "body_NW": {"x": 80, "y": 0, "width": 40, "height": 40, "scale": 0.5},
    "body_NE": {"x": 120, "y": 0, "width": 40, "height": 40, "scale": 0.5},
    "body_SW": {"x": 80, "y": 40, "width": 40, "height": 40, "scale": 0.5},
    "body_SE": {"x": 120, "y": 40, "width": 40, "height": 40, "scale": 0.5}
}

# Food sprites
FOOD_SPRITES = {
    "apple": {"x": 120, "y": 80, "width": 40, "height": 40, "scale": 0.5}
}