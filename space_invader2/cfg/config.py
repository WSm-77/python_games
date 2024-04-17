from collections import namedtuple
import os

def get_image_path(*parts):
    return os.path.join("assets", "graphics", *parts)

WindowConfig = namedtuple("WindowConfig", [
    "TITLE", 
    "ICON_PATH", 
    "BACKGROUND_PATH", 
    "WIDTH", 
    "HEIGHT"
])

GameConfig = namedtuple("GameConfig", [
    "FPS"                      
])

WINDOW_CONFIG = WindowConfig(
    TITLE = "Space Invaders V2",
    ICON_PATH = get_image_path("window", "icon.png"),
    BACKGROUND_PATH = get_image_path("window", "background-black.png"),
    WIDTH = 800,
    HEIGHT = 600
)

GAME_CONFIG = GameConfig(
    FPS = 60
)