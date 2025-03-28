############################
# external library imports #
############################

import pygame

#########################
# local library imports #
#########################

import cfg.config as cfg
import game_modes.modes as game_modes

########
# code #
########

class Game:
    def __init__(self) -> None:
        # seting pygame
        Game.init()

        # setting window properties
        self.screen = pygame.display.set_mode((cfg.WINDOW_CONFIG.WIDTH, cfg.WINDOW_CONFIG.HEIGHT))
        self.background = pygame.transform.scale(
            pygame.image.load(cfg.WINDOW_CONFIG.BACKGROUND_IMAGE), (cfg.WINDOW_CONFIG.WIDTH, cfg.WINDOW_CONFIG.HEIGHT)
        )
        self.clock = pygame.time.Clock()

        # font
        self.font = pygame.font.Font(cfg.GAME_CONFIG.FONT, cfg.GAME_CONFIG.FONT_SIZE)

        # game
        self.currentGame = None

    @staticmethod
    def init():
        pygame.init()
        pygame.display.set_caption("Space Invader V2")
        pygame.display.set_icon(pygame.image.load(cfg.get_image_path("window", "icon.png")))

    def start(self):
        self.main_menu()


    def main_menu(self):
        self.new_game()        # TODO

    def new_game(self):
        self.currentGame = game_modes.ClassicGame(self)
        self.currentGame.start_game()
        self.currentGame = None
