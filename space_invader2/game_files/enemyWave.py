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
        # base config
        self.game = game
        self.enemies = []
        self.waveNb = 0
        self.generateOrder = [cfg.ENEMY_CONFIG.RED, cfg.ENEMY_CONFIG.GREEN, cfg.ENEMY_CONFIG.BLUE]
        self.generateIdx = 0

        # wave state
        self.freezeTimer = 0
        self.waveStarted = False

        # font config
        self.waveFont = None
        self.waveFontRect = None

    def generate_new_wave(self):
        nbOfEnemiesInWave = cfg.ENEMY_WAVE_CONFIG.NUMBER_OF_ENEMIES_IN_FIRST_WAVE + self.waveNb
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

        # update wave number
        self.waveNb += 1

    def update_enemies(self):
        # enemies
        for enemy in self.enemies:
            enemy.update()

    def update_enemies_bullets(self):
        # enemies' bullets
        for bullet in Enemy.bullets[:]:
            bullet.update()
            if bullet.y > cfg.WINDOW_CONFIG.HEIGHT:
                Enemy.bullets.remove(bullet)

    def draw_all(self):
        if self.is_wave_freezed():
            self.print_text()
        else:
            # draw enemies
            for enemy in self.enemies:
                enemy.draw()

            # draw enemies' bullets
            for bullet in Enemy.bullets:
                bullet.draw()


    def wave_start(self):
        # generate new wave
        self.generate_new_wave()

        # prepare text
        self.waveFont = self.game.font.render(f"WAVE {self.waveNb}", True, (255, 255, 255))
        self.waveFontRect = self.waveFont.get_rect()
        self.waveFontRect.center = (cfg.WINDOW_CONFIG.WIDTH // 2, cfg.WINDOW_CONFIG.HEIGHT // 2)

        # update wave state
        self.freezeTimer = cfg.ENEMY_WAVE_CONFIG.WAVE_START_FREEZE_TIME
        self.waveStarted = True

    def wave_end(self):
        # prepare text
        endTextOptions = len(cfg.ENEMY_WAVE_CONFIG.WAVE_END_TEXT_LIST)
        endText = cfg.ENEMY_WAVE_CONFIG.WAVE_END_TEXT_LIST[randint(0, endTextOptions - 1)]
        self.waveFont = self.game.font.render(endText, True, (255, 255, 255))
        self.waveFontRect = self.waveFont.get_rect()
        self.waveFontRect.center = (cfg.WINDOW_CONFIG.WIDTH // 2, cfg.WINDOW_CONFIG.HEIGHT // 2)

        # remove all enemies' lasers
        Enemy.bullets.clear()

        # update wave state
        self.freezeTimer = cfg.ENEMY_WAVE_CONFIG.WAVE_END_FREEZE_TIME
        self.waveStarted = False

    def is_wave_freezed(self):
        return self.freezeTimer > 0

    def check_wave_start_condition(self):
        return len(self.enemies) == 0 and not self.waveStarted

    def check_wave_end_condition(self):
        return len(self.enemies) == 0 and self.waveStarted

    def print_text(self):
        self.game.screen.blit(self.waveFont, self.waveFontRect)

    def update(self):
        if self.is_wave_freezed():
            self.freezeTimer -= 1
        elif self.check_wave_start_condition():
            self.wave_start()
        elif self.check_wave_end_condition():
            self.wave_end()
        else:
            self.update_enemies()
            self.update_enemies_bullets()
