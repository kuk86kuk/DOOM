import math


# game settings
RES = WIDTH, HEIGHT = 1200, 600
FPS = 60

# player settings
PLAYER_POS = 3, 4 # Позиция игрока 
PLAYER_ANGLE = 0 # Угол игрока
PLAYER_SPEED = 0.004 # Скорость игрока
PLAYER_POT_SPEED = 0.002 # Скорость врачения игрока


# raycating settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20 