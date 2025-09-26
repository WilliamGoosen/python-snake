from typing import TYPE_CHECKING

# Use the TYPE_CHECKING guard to import for type hints only
if TYPE_CHECKING:
    from graphics_manager import GraphicsManager

class Game:
    """A container to hold all game components and the current state."""
    def __init__(self):
        # Managers
        self.graphics_manager: GraphicsManager
        # Variables from main.py        
        self.score: int = 0
        self.high_score: int = 0

