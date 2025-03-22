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
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.game = game

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def get_bottom_edge_y_offset(self):
        offsetY = 0
        for y in range(self.get_height() - 1, 0, -1):
            for x in range(self.get_width()):
                if self.mask.get_at((x, y)):
                    offsetY = y
                    break
            if offsetY != 0:
                break

        return offsetY

    # this method should be overwritten in derived class
    def actions(self):
        self.update_rect()

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.actions()
