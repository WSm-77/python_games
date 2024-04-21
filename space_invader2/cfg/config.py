from collections import namedtuple
import os

def get_image_path(*parts):
    return os.path.join("assets", "graphics", *parts)

def get_font_path(*parts):
    return os.path.join("assets", "font", *parts)

WindowConfig = namedtuple("WindowConfig", [
    "TITLE", 
    "ICON_PATH", 
    "BACKGROUND_PATH", 
    "WIDTH", 
    "HEIGHT"
])

GameConfig = namedtuple("GameConfig", [
    "FPS",
    "FONT"
])

PlayerConfig = namedtuple("PlayerConfig", [
    "SHIP_IMAGE",
    "LASER_IMAGE",
    "VEL_PER_FRAME"
])

WINDOW_CONFIG = WindowConfig(
    TITLE = "Space Invaders V2",
    ICON_PATH = get_image_path("window", "icon.png"),
    BACKGROUND_PATH = get_image_path("window", "background-black.png"),
    WIDTH = 800,
    HEIGHT = 600
)

GAME_CONFIG = GameConfig(
    FPS = 60,
    FONT = get_font_path("go3v2.ttf")
)

PLAYER_CONFIG = PlayerConfig(
    SHIP_IMAGE = get_image_path("items", "pixel_ship_yellow.png"),
    LASER_IMAGE = get_image_path("items", "pixel_laser_yellow.png"),
    VEL_PER_FRAME = 300 / GAME_CONFIG.FPS
)