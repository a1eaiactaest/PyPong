import pygame 
from pygame.locals import *
import sys
import random

pygame.init()

win = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('PyPong')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (150, 0, 255)
MINT = (0, 255, 187)
ORANGE = (255, 153, 0)
RED = (227, 30, 30)
colors = [BLACK, WHITE, VIOLET, MINT, ORANGE, RED]

background = BLACK
interface = WHITE

# paddle 
paddle_width = 100
paddle_height = 20
paddle_pos = (350, 720)
paddle = pygame.Surface([paddle_width, paddle_height])
vel = 5
# pygame.draw.rect(win,(255,255,255),[350,720, paddle_width,paddle_height])
paddle.fill(interface)
paddle_rect = paddle.get_rect()
paddle_rect.x = paddle_pos[0]
paddle_rect.y = paddle_pos[1]

# ball
ball_width = 20
ball_height = 20
#ball_speed = 4
ball_x_speed = 4
ball_y_speed = 4
ball = pygame.Surface([ball_width, ball_height], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(ball, interface, [0, 0, ball_width, ball_height])
ball_rect = ball.get_rect()
ball_rect.x = 400   
ball_rect.y = 400

# points
score = '0'
font = pygame.font.Font('freesansbold.ttf', 64)

def print_score():
    txt = font.render(score, True, interface)
    txt_rect = txt.get_rect()
    txt_rect.center = (400, 400)
    win.blit(txt, txt_rect)

fps = 100
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(0)

    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_a] and paddle_rect.x > vel:
        paddle_rect.x -= vel
    if pressed[pygame.K_d] and paddle_rect.x < 800 - vel - paddle_width:
        paddle_rect.x += vel
    
    if pressed[pygame.K_b]:
        background = random.choice(colors)

    if background != BLACK:
        font_color = BLACK
        interface = BLACK
        paddle.fill(BLACK)
        
        pygame.draw.ellipse(ball, BLACK, [0, 0, ball_width, ball_height])

    elif background == BLACK:
        font_color = WHITE
        interface = WHITE
        paddle.fill(WHITE)

        pygame.draw.ellipse(ball, WHITE, [0, 0, ball_width, ball_height])        

    ball_rect.move_ip(ball_x_speed, ball_y_speed)

    if ball_rect.right >= 800:
        ball_x_speed *= -1 
    
    if ball_rect.left <= 0:
        ball_x_speed *= -1
    
    if ball_rect.top <= 0:
        ball_y_speed *= -1

    if ball_rect.bottom >= 800:
        score = str(int(0))
        vel = 5
        ball_rect.x = 400
        ball_rect.y = 400

    if ball_rect.colliderect(paddle_rect):
        ball_y_speed *= -1
        ball_rect.bottom = paddle_rect.top
        score = str(int(score) + 1)
#        ball_x_speed = ball_x_speed + 1
#        ball_y_speed = ball_y_speed + 1
#        print(ball_x_speed, ball_y_speed)

    win.fill(background)
    
    print_score()

    win.blit(paddle, paddle_rect)
    
    win.blit(ball, ball_rect)

    pygame.display.flip()

    clock.tick(fps)
    




            

