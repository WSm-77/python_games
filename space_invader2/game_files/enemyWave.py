############################
# external library imports #
############################

from random import randint
import pygame

#########################
# local library imports #
#########################

from game_files.enemy import Enemy
import cfg.config as cfg

########
# code #
########

class EnemyWave:
    def __init__(self, game) -> None:
        self.game = game
        self.enemies = []
        self.waveNb = 1
        self.generateOrder = [cfg.ENEMY_CONFIG.RED, cfg.ENEMY_CONFIG.GREEN, cfg.ENEMY_CONFIG.BLUE]
        self.generateIdx = 0

    def generate_new_wave(self):
        nbOfEnemiesInWave = cfg.ENEMY_WAVE_CONFIG.NUMBER_OF_ENEMIES_IN_FIRST_WAVE + self.waveNb - 1
        for _ in range(nbOfEnemiesInWave):
            # prepare enemy
            shipImage = pygame.image.load(self.generateOrder[self.generateIdx].SHIP_IMAGE)
            laserImage = pygame.image.load(self.generateOrder[self.generateIdx].LASER_IMAGE)
            shipWidth = shipImage.get_width()
            shipHeight = shipImage.get_height()
            x = randint(0, cfg.ENEMY_WAVE_CONFIG.SPWAN_AREA.WIDTH - shipWidth)
            y = randint(-cfg.ENEMY_WAVE_CONFIG.SPWAN_AREA.HEIGHT, -shipHeight)

            # create enemy
            newEnemy = Enemy(x, y, shipImage, laserImage, self.game)
            self.enemies.append(newEnemy)

            # update generator
            self.generateIdx = (self.generateIdx + 1) % 3

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()

    def update(self):
        if len(self.enemies) == 0:
            self.generate_new_wave()
        else:
            self.update_enemies()
