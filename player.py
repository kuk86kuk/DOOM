import settings
import pygame
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = settings.PLAYER_POS
        
        self.angle = settings.PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = settings.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin 
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        print(self.x)
        self.x += dx
        self.y += dy
        

        if keys[pygame.K_LEFT]:
            self.angle -= settings.PLAYER_POT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += settings.PLAYER_POT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def draw(self):
        pygame.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                        (self.x *100 + settings.WIDTH * math.cos(self.angle),
                        self.y * 100 + settings.WIDTH * math.sin(self.angle)), 2)

        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)


    def update(self):
        self.movement()

    # Метод класса возвращает позицию игрока
    @property
    def pos(self):
        return self.x, self.y

    # Метод класса возвращает позицию игрока на карте
    @property
    def map_pos(self):
        return int(self.x), int(self.y)