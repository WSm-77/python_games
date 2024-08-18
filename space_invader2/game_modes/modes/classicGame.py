############################
# external library imports #
############################

import pygame

#########################
# local library imports #
#########################

from game_files.enemy import Enemy
from game_files.enemyWave import EnemyWave
import game_modes

########
# code #
########

class ClassicGame(game_modes.GameMode):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.enemyWave = EnemyWave(game)
        self.cnt = 0

    def handle_collisions(self):
        # player bullets with enemies
        for playerBullet in self.player.bullets[:]:
            bulletRect = pygame.Rect(playerBullet.x, playerBullet.y, playerBullet.get_width(), playerBullet.get_height())

            for enemy in self.enemyWave.enemies[:]:
                enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.get_width(), enemy.get_height())

                # fast rect check for performance optymalization
                if not bulletRect.colliderect(enemyRect):
                    self.cnt += 1
                    # continue

                offsetX = enemy.x - playerBullet.x
                offsetY = enemy.y - playerBullet.y
                if playerBullet.mask.overlap(enemy.mask, (offsetX, offsetY)):
                    self.player.bullets.remove(playerBullet)
                    self.enemyWave.enemies.remove(enemy)

    def update_player(self):
        # player
        self.player.update()

        # player's bullets
        for bullet in self.player.bullets[:]:
            bullet.update()
            if bullet.y + bullet.get_height() < 0:
                self.player.bullets.remove(bullet)

    def update_game(self):
        self.handle_events()
        self.game.screen.blit(self.game.background, (0, 0))
        self.update_player()
        self.enemyWave.update()
        if not self.enemyWave.is_wave_freezed():
            self.handle_collisions()
        pygame.display.update()

    def start_game(self):
        super().start_game()
