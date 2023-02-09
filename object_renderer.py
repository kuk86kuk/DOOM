import pygame
import settings

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()
        self.sky_texture = self.get_texture('templates/textures/7.jpg', (settings.WIDTH, settings.HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_object()

    def draw_background(self):
        speed = 1
        self.sky_offset = (self.sky_offset  + speed + self.game.player_.rel) % settings.WIDTH
        self.screen.blit(self.sky_texture, (-self.sky_offset, 0))
        self.screen.blit(self.sky_texture, (-self.sky_offset + settings.WIDTH, 0))

        pygame.draw.rect(self.screen, settings.FLOOR_COLOR, (0, settings.HALF_HEIGHT, settings.WIDTH, settings.HEIGHT))

    def draw_floor(self):
        pass

    def render_game_object(self):
        list_object = self.game.raycasting_.object_to_renderer
        for depth, image, pos in list_object:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(settings.TEXTURE_SIZE, settings.TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_texture(self):
        return {
            1: self.get_texture('templates/textures/1.bmp'),
            2: self.get_texture('templates/textures/2.bmp'),
            3: self.get_texture('templates/textures/3.bmp'),
            4: self.get_texture('templates/textures/4.bmp'),
            5: self.get_texture('templates/textures/5.bmp'),
            6: self.get_texture('templates/textures/6.bmp'),
        }

        