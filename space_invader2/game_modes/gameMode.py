############################
# external library imports #
############################

import pygame

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

    def update_game(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False