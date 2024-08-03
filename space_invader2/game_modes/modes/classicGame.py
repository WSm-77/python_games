############################
# external library imports #
############################

import pygame

#########################
# local library imports #
#########################

import game_modes

########
# code #
########

class ClassicGame(game_modes.GameMode):
    def __init__(self, game) -> None:
        super().__init__(game)

    def update_game(self):
        self.handle_events()
        self.game.screen.blit(self.game.background, (0, 0))
        self.player.update()
        pygame.display.update()
