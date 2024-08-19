############################
# external library imports #
############################

import pygame
import sys

#########################
# local library imports #
#########################

import cfg.config as cfg
from game_files.player import Player

########
# code #
########

class GameMode:
    def __init__(self, game) -> None:
        self.game = game
        self.running = True
        self.player = Player(game)

    def start_game(self):

        #############
        # Game Loop #
        #############

        while self.running:
            self.game.clock.tick(cfg.GAME_CONFIG.FPS)
            self.update_game()
        #end while

        self.game_over()

    def game_over(self):
        gameOverText = self.game.font.render(cfg.GAME_OVER_CONFIG.TEXT, cfg.GAME_OVER_CONFIG.FONT_SIZE, (255, 255, 255))
        gameOverTextRect = gameOverText.get_rect()
        gameOverTextRect.center = (cfg.WINDOW_CONFIG.WIDTH // 2, cfg.WINDOW_CONFIG.HEIGHT // 2)
        for _ in range(cfg.GAME_OVER_CONFIG.FREEZE_TIME):
            self.handle_events()
            self.game.clock.tick(cfg.GAME_CONFIG.FPS)
            self.game.screen.blit(gameOverText, gameOverTextRect)
            pygame.display.update()

    # this method should be overwritten in derived class
    def update_game(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
