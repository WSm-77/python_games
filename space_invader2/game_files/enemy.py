############################
# external library imports #
############################

#########################
# local library imports #
#########################

from game_files.activeObject import ActiveObject
import cfg.config as cfg

########
# code #
########

class Enemy(ActiveObject):
    def __init__(self, x, y, image, game) -> None:
        super().__init__(x, y, image, game)

    def move(self):
        pass

    def shoot(self):
        pass

    def actions(self):
        pass

