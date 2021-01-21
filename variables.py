import pygame
pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 45

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")

SCORE_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

FPS = 60
CLOCK = pygame.time.Clock()
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('spaceship_yellow.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('spaceship_red.png'), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load('space.png'), (WIDTH, HEIGHT))

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT = pygame.mixer.Sound('Grenade+1.mp3')
BULLET_FIRE = pygame.mixer.Sound('Gun+Silencer.mp3')