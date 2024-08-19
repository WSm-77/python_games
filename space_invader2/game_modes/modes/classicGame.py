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
import cfg.config as cfg

########
# code #
########

class ClassicGame(game_modes.GameMode):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.enemyWave = EnemyWave(game)
        self.score = 0

    def check_pixel_perfect_colision(self, obj1, obj2):
        offsetX = obj2.x - obj1.x
        offsetY = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offsetX, offsetY))

    def collision_enemy_arena_bottom(self):
        for enemy in self.enemyWave.enemies[:]:
            if enemy.y + enemy.get_height() > cfg.WINDOW_CONFIG.HEIGHT:
                self.player.hit(enemy.hp())
                self.enemyWave.enemies.remove(enemy)

    def collision_player_with_enemies(self):
        for enemy in self.enemyWave.enemies[:]:
            if not self.player.rect.colliderect(enemy.rect):
                continue

            if self.check_pixel_perfect_colision(self.player, enemy):
                self.player.hit(enemy.hp())
                self.enemyWave.enemies.remove(enemy)
                self.score += 1

    def collision_player_bullets_with_enemies(self):
        # player bullets with enemies
        for playerBullet in self.player.bullets[:]:
            for enemy in self.enemyWave.enemies[:]:
                # fast rect check for performance optymalization
                if not playerBullet.rect.colliderect(enemy.rect):
                    continue

                if self.check_pixel_perfect_colision(playerBullet, enemy):
                    enemy.hit(playerBullet.damage)
                    self.player.bullets.remove(playerBullet)
                    if enemy.is_destroyed():
                        self.enemyWave.enemies.remove(enemy)
                        self.score += 1

    def collision_player_with_enemies_bullets(self):
        for enemyBullet in Enemy.bullets[:]:
            if not self.player.rect.colliderect(enemyBullet.rect):
                continue

            if self.check_pixel_perfect_colision(self.player, enemyBullet):
                self.player.hit(enemyBullet.damage)
                Enemy.bullets.remove(enemyBullet)

    def handle_collisions(self):
        self.collision_enemy_arena_bottom()
        self.collision_player_with_enemies()
        self.collision_player_bullets_with_enemies()
        self.collision_player_with_enemies_bullets()

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
        if self.player.is_destroyed():
            self.running = False
        pygame.display.update()

    def start_game(self):
        super().start_game()
