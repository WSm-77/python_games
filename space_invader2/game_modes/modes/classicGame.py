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
        self.enemies = []

    def update_active_objects(self):
        # player
        self.player.update()

        # bullets
        for bullet in self.player.bullets:
            bullet.update()

    def update_game(self):
        self.handle_events()
        self.game.screen.blit(self.game.background, (0, 0))
        self.update_active_objects()
        pygame.display.update()
