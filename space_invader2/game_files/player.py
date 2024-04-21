from game_files.ship import Ship
import cfg.config as cfg
import pygame

class Player(Ship):
    def __init__(self, game) -> None:
        shipImage = pygame.image.load(cfg.PLAYER_CONFIG.SHIP_IMAGE)
        laserImage = pygame.image.load(cfg.PLAYER_CONFIG.LASER_IMAGE)
        x = cfg.WINDOW_CONFIG.WIDTH // 2 - shipImage.get_width() // 2
        y = cfg.WINDOW_CONFIG.HEIGHT - shipImage.get_height() - 10
        super().__init__(x, y, shipImage, laserImage, game)

    def move(self, pressedKeys):
        if pressedKeys[pygame.K_a]:
            self.x -= cfg.PLAYER_CONFIG.VEL_PER_FRAME
        if pressedKeys[pygame.K_d]:
            self.x += cfg.PLAYER_CONFIG.VEL_PER_FRAME
        if pressedKeys[pygame.K_w]:
            self.y -= cfg.PLAYER_CONFIG.VEL_PER_FRAME
        if pressedKeys[pygame.K_s]:
            self.y += cfg.PLAYER_CONFIG.VEL_PER_FRAME

    def update(self, pressedKeys):
        self.move(pressedKeys)
        super().draw()