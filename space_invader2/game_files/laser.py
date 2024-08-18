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

class Laser(ActiveObject):
    def __init__(self, shipX, shipY, shipWidth, shipHeight, image, game, isShootByPlayer: bool) -> None:
        x = shipX + shipWidth // 2 - image.get_width() // 2
        y = shipY
        if isShootByPlayer:
            y -= image.get_height() + cfg.LASER_CONFIG.SPAWN_SPAN
        else:
            y += shipHeight + cfg.LASER_CONFIG.SPAWN_SPAN

        super().__init__(x, y, image, game)

        self.isShootByPlayer = isShootByPlayer

    def move(self):
        if self.isShootByPlayer:
            self.y -= cfg.LASER_CONFIG.VEL_PER_FRAME
        else:
            self.y += cfg.LASER_CONFIG.VEL_PER_FRAME

    def actions(self):
        self.move()
        super().actions()
