import game_files.object as ob
from game_files.player import Player
from game_files.enemy import Enemy
from game_files.bullet import Bullet
from collections import deque

class Game:
    def __init__(self) -> None:
        # pygame initialization
        ob.pygame.init()

        # setting screen
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = ob.pygame.display.set_mode((self.screenWidth, self.screenHeight))

        # setting title, icon and background
        ob.pygame.display.set_caption("Space Invaders")
        self.icon = ob.pygame.image.load("./images/ufo.png")
        ob.pygame.display.set_icon(self.icon)
        self.backgroundImage = ob.pygame.image.load("./images/background.png")

        # setting background music
        self.backgroundMusic = ob.pygame.mixer.music.load("./sounds/background.mp3")

        # creating player
        self.player: Player = None

        # creating enemies
        self.enemies: list[Enemy] = []

        # creating bullets queue
        self.bullets: deque[Bullet] = deque()

        # score
        self.score = 0
        self.scorePosition = (10, 10)
        self.font = ob.pygame.font.Font("freesansbold.ttf", 32)

    def run(self, numberOfEnemies = 6, playMusic = True):
        if playMusic:
            ob.pygame.mixer.init()
            ob.pygame.mixer.music.set_volume(0.5)
            ob.pygame.mixer.music.play(-1)
        objectsSpeed = 5

        self.player = Player(self.screenWidth, self.screenHeight)
        self.enemies = [Enemy(self.screenWidth, self.screenHeight, objectsSpeed) for _ in range(numberOfEnemies)]


        # game loop
        running = True
        while running:
            for event in ob.pygame.event.get():
                match event.type:
                    case ob.pygame.QUIT:
                        running = False

                    case ob.pygame.KEYDOWN:
                        match event.key:
                            case ob.pygame.K_SPACE:
                                if len(self.bullets) < self.player.magazineCapacity:
                                    self.bullets.append(
                                        Bullet(self.player.x, self.player.y, objectsSpeed, self.screenWidth, self.screenHeight)
                                        )
                                    if playMusic:
                                        shootSound = ob.pygame.mixer.Sound("./sounds/shoot.mp3")
                                        shootSound.play()
                            case _:
                                pass

                    case _:
                        pass

            # player movement
            keys = ob.pygame.key.get_pressed()
            if keys[ob.pygame.K_LEFT] or keys[ob.pygame.K_a]:
                self.player.x -= objectsSpeed*self.player.speedFactor
            if keys[ob.pygame.K_RIGHT] or keys[ob.pygame.K_d]:
                self.player.x += objectsSpeed*self.player.speedFactor

            self.__update_objects()
            self.__handle_collisions()

            if self.__check_game_over_conditions():
                self.__game_over()
                # running = False
            else:
                self.__update_screen()

            ob.pygame.display.update()

    def __update_objects(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        bulletIndex = 0
        while bulletIndex < len(self.bullets):
            self.bullets[bulletIndex].update()
            if self.bullets[bulletIndex].y <= 0:
                del self.bullets[bulletIndex]
            else:
                bulletIndex += 1
            #end if
        #end while

    def __handle_collisions(self):
        enemyIndex = 0
        while enemyIndex < len(self.enemies):
            bulletIndex = 0
            while bulletIndex < len(self.bullets):
                if Game.__check_collision(self.bullets[bulletIndex], self.enemies[enemyIndex]):
                    del self.bullets[bulletIndex]
                    self.enemies[enemyIndex].reset()
                    self.score += 1
                else:
                    bulletIndex += 1
                #end if
            #end while
            enemyIndex += 1

    def __update_screen(self):
        self.screen.blit(self.backgroundImage, (0, 0))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        for bullet in self.bullets:
            self.screen.blit(bullet.image, (bullet.x, bullet.y))
        for enemy in self.enemies:
            self.screen.blit(enemy.image, (enemy.x, enemy.y))

        self.__show_score()

    def __show_score(self):
        scoreString = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(scoreString, self.scorePosition)

    def __check_game_over_conditions(self) -> bool:
        for enemy in self.enemies:
            if enemy.y + enemy.imageHeight >= self.player.y:
                return True
            
        return False
    
    def __game_over(self):
        gameOverFont = ob.pygame.font.Font("freesansbold.ttf", 64)
        gameOverMessage = gameOverFont.render(f"GAME OVER", True, (255, 255, 255))
        gameOverMessageRect = gameOverMessage.get_rect()
        self.screen.blit(gameOverMessage, (self.screenWidth // 2 - gameOverMessageRect.width // 2, 
                                           self.screenHeight // 2 - gameOverMessageRect.height // 2))

    @staticmethod
    def __check_collision(bullet: Bullet, enemy: Enemy):
        if (enemy.y <= bullet.y <= enemy.y + enemy.imageHeight) or (bullet.y <= enemy.y <= bullet.y + bullet.imageHeight):
            if (enemy.x <= bullet.x <= enemy.x + enemy.imageWidth) or (bullet.x <= enemy.x <= bullet.x + bullet.imageWidth):
                return True

        return False

    
game = Game()
game.run()