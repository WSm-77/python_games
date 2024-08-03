############################
# external library imports #
############################

import pygame

#########################
# local library imports #
#########################

########
# code #
########

class ActiveObject:
    def __init__(self, x, y, image, game) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.game = game

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    # this method should be overwritten in derived class
    def actions(self):
        pass

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.actions()
        self.draw()
