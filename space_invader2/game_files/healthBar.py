############################
# external library imports #
############################

#########################
# local library imports #
#########################

import cfg.config as cfg
import pygame

########
# code #
########

class HealthBar:
    def __init__(self, totalHp, activeObject, game, showBar) -> None:
        # object properties
        self.activeObject = activeObject
        self.game = game

        # hp
        self.totalHp = totalHp
        self.currentHp = totalHp

        # bar
        self.bottomEdgeYOffset = activeObject.get_bottom_edge_y_offset()
        barX = activeObject.x
        barY = self.activeObject.y + self.bottomEdgeYOffset + cfg.HEALTH_BAR_CONFIG.DISTANCE_FROM_BOTTOM_EDGE
        self.totalHpBar = pygame.rect.Rect(barX, barY, activeObject.get_width(), cfg.HEALTH_BAR_CONFIG.HEIGHT)
        self.currentHpBar = pygame.rect.Rect(barX, barY, activeObject.get_width(), cfg.HEALTH_BAR_CONFIG.HEIGHT)
        self.showBar = showBar

    def loose_hp(self, damage):
        self.currentHp -= damage
        if self.currentHp < 0:
            self.currentHp = 0
        self.currentHpBar.width = (self.currentHp * self.totalHpBar.width) // self.totalHp

    def recover_hp(self, heal):
        self.currentHp += heal
        if self.currentHp > self.totalHp:
            self.currentHp = self.totalHp
        self.currentHpBar.width = (self.currentHp * self.totalHpBar.width) // self.totalHp

    def update(self):
        if self.showBar:
            # update position
            barX = self.activeObject.x
            barY = self.activeObject.y + self.bottomEdgeYOffset + cfg.HEALTH_BAR_CONFIG.DISTANCE_FROM_BOTTOM_EDGE
            self.totalHpBar.topleft = (barX, barY)
            self.currentHpBar.topleft = (barX, barY)

            # draw total hp bar
            pygame.draw.rect(self.game.screen, cfg.HEALTH_BAR_CONFIG.TOTAL_HP_BAR_COLOR, self.totalHpBar)

            # draw current hp bar
            pygame.draw.rect(self.game.screen, cfg.HEALTH_BAR_CONFIG.CURRENT_HP_BAR_COLOR, self.currentHpBar)
