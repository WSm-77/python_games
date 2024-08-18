############################
# external library imports #
############################

from collections import namedtuple
import os

#########################
# local library imports #
#########################

########
# code #
########

#############
# functions #
#############

def get_image_path(*parts):
    return os.path.join("assets", "graphics", *parts)

def get_font_path(*parts):
    return os.path.join("assets", "font", *parts)

################
# named tuples #
################

WindowConfig = namedtuple("WindowConfig", [
    "TITLE",
    "ICON_PATH",
    "BACKGROUND_IMAGE",
    "WIDTH",
    "HEIGHT"
])

GameConfig = namedtuple("GameConfig", [
    "FPS",
    "FONT",
    "FONT_SIZE"
])

PlayerConfig = namedtuple("PlayerConfig", [
    "SHIP_IMAGE",
    "LASER_IMAGE",
    "VEL_PER_FRAME",
    "SHOOT_COOLDOWN"
])

EnemyConfig = namedtuple("EnemyConfig", [
    "RED",
    "GREEN",
    "BLUE",
    "VEL_PER_FRAME",
    "SHOOTING_CHANCE"
])

EnemyImages = namedtuple("EnemyImages", [
    "SHIP_IMAGE",
    "LASER_IMAGE"
])

EnemyWaveConfig = namedtuple("EnemyWaveConfig", [
    "NUMBER_OF_ENEMIES_IN_FIRST_WAVE",
    "SPWAN_AREA",
    "WAVE_END_FREEZE_TIME",
    "WAVE_START_FREEZE_TIME",
    "WAVE_END_TEXT_LIST"
])

Area = namedtuple("Area", [
    "WIDTH",
    "HEIGHT"
])

LaserConfig = namedtuple("LaserConfig", [
    "VEL_PER_FRAME",
    "SPAWN_SPAN"
])

########################
# config specyfication #
########################

WINDOW_CONFIG = WindowConfig(
    TITLE = "Space Invaders V2",
    ICON_PATH = get_image_path("window", "icon.png"),
    BACKGROUND_IMAGE = get_image_path("window", "background-black.png"),
    WIDTH = 800,
    HEIGHT = 600
)

GAME_CONFIG = GameConfig(
    FPS = 60,
    FONT = get_font_path("go3v2.ttf"),
    FONT_SIZE = 32
)

PLAYER_CONFIG = PlayerConfig(
    SHIP_IMAGE = get_image_path("items", "pixel_ship_yellow.png"),
    LASER_IMAGE = get_image_path("items", "pixel_laser_yellow.png"),
    VEL_PER_FRAME = 300 / GAME_CONFIG.FPS,
    SHOOT_COOLDOWN = GAME_CONFIG.FPS // 2
)

ENEMY_CONFIG = EnemyConfig(
    RED = EnemyImages(
        SHIP_IMAGE = get_image_path("items", "pixel_ship_red_small.png"),
        LASER_IMAGE = get_image_path("items", "pixel_laser_red.png")
    ),
    GREEN = EnemyImages(
        SHIP_IMAGE = get_image_path("items", "pixel_ship_green_small.png"),
        LASER_IMAGE = get_image_path("items", "pixel_laser_green.png")
    ),
    BLUE = EnemyImages(
        SHIP_IMAGE = get_image_path("items", "pixel_ship_blue_small.png"),
        LASER_IMAGE = get_image_path("items", "pixel_laser_blue.png")
    ),
    VEL_PER_FRAME = 100 / GAME_CONFIG.FPS,
    SHOOTING_CHANCE = GAME_CONFIG.FPS * 3
)

ENEMY_WAVE_CONFIG = EnemyWaveConfig(
    NUMBER_OF_ENEMIES_IN_FIRST_WAVE = 5,
    SPWAN_AREA = Area(
        WIDTH = WINDOW_CONFIG.WIDTH,
        HEIGHT = WINDOW_CONFIG.HEIGHT * 2
    ),
    WAVE_END_FREEZE_TIME = GAME_CONFIG.FPS * 2,
    WAVE_START_FREEZE_TIME = GAME_CONFIG.FPS * 2,
    WAVE_END_TEXT_LIST = ["AWSOME!!!", "GREAT JOB!!!", "WELL DONE!!!"]
)

LASER_CONFIG = LaserConfig(
    VEL_PER_FRAME = 500 / GAME_CONFIG.FPS,
    SPAWN_SPAN = -50
)
