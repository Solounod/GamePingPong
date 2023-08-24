import pygame
import random
import math
import sys

pygame.init()

#screen const
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100 

#ball
BALL_SIZE = 20



class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.font30 = pygame.font.Font(None, 30)

    def displayScore(self, text, score, x, y, color):
        text = self.font30.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)

        angle = random.uniform(-math.pi / 3, math.pi / 3)
        self.speed_x = 10 * math.cos(angle)
        self.speed_y = 10 * math.sin(angle)

player_paddle = Paddle(width - 20, height // 2)
opponent_paddle = Paddle( 20, height // 2)
ball = Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, opponent_paddle, ball)
score1 = 0
score2 = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    

    #logic game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_paddle.rect.top > 0:
                player_paddle.rect.y -= 50
            if event.key == pygame.K_DOWN and player_paddle.rect.bottom < height:
                player_paddle.rect.y += 50
            if event.key == pygame.K_w and opponent_paddle.rect.top > 0:
                opponent_paddle.rect.y -= 50
            if event.key == pygame.K_s and opponent_paddle.rect.bottom < height :
                opponent_paddle.rect.y += 50



    ball.rect.x += ball.speed_x
    ball.rect.y += ball.speed_y

    if ball.rect.top <= 0 or ball.rect.bottom >= height:
        ball.speed_y *= -1  
    if ball.rect.left <= 0:
        score1 += 1
        ball.rect.x = width // 2
        ball.rect.y = height // 2
        angle = random.uniform(-math.pi / 2, math.pi / 4)
        ball.speed_x = 10 * math.cos(angle)
        ball.speed_y = 10 * math.sin(angle)
    if ball.rect.right >= width:
        score2 += 1
        ball.rect.x = width // 2
        ball.rect.y = height // 2
        angle = random.uniform(-math.pi / 2, math.pi / 4)
        ball.speed_x = 10 * math.cos(angle)
        ball.speed_y = 10 * math.sin(angle)

    if pygame.sprite.collide_mask(player_paddle, ball):
        
        ball.speed_x *= -1
    if pygame.sprite.collide_rect(ball, opponent_paddle):
        ball.speed_x *= -1

    #update screen
    screen.fill(BLACK)
    player_paddle.displayScore("Player 1: ", score1, 100, 20, WHITE)
    opponent_paddle.displayScore("Player 2: ", score2, 600, 20, WHITE)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()