############################
# external library imports #
############################

#########################
# local library imports #
#########################

from game_files.activeObject import ActiveObject

########
# code #
########

class Ship(ActiveObject):
    bullets = []

    def __init__(self, x, y, shipImage, laserImage, game) -> None:
        super().__init__(x, y, shipImage, game)
        self.laserImage = laserImage

    def move(self):
        pass

    def shoot(self):
        pass

    def actions(self):
        self.move()
        self.shoot()
