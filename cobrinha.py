import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

background_img = pygame.image.load('img.png')
pygame.mixer.music.set_volume(0.4)  # entre 0 e 1
background_music = pygame.mixer.music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound('smw_coin.wav')  # wav ou erro

width = 630
height = 480
x_snake = width//2 - 40//2
y_snake = height//2 - 50//2

velocity = 10
x_control = velocity
y_control = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)

score = 0
font = pygame.font.SysFont('comic sans', 40, True, False)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snakely")
clock = pygame.time.Clock()
snake_list = []
initial_length = 5
died = False


def increase_snake(snake_list):
    for XnY in snake_list:
        pygame.draw.rect(screen, (222, 11, 99), (XnY[0], XnY[1], 20, 20))


def restart_game():
    global score, initial_length, x_snake, y_snake, snake_list, head_list, x_apple, y_apple, died
    score = 0
    initial_length = 5
    x_snake = width // 2 - 40 // 2
    y_snake = height // 2 - 50 // 2
    snake_list = []
    head_list = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    died = False


while True:
    clock.tick(20)
    screen.fill((255, 255, 255))
    screen.blit(background_img, (0, 0))
    msg = f"Score:{score}"
    txt_formatted = font.render(msg, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_control == velocity:
                    pass
                else:
                    x_control = -velocity
                    y_control = 0
            if event.key == K_RIGHT:
                if x_control == -velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0
            if event.key == K_UP:
                if y_control == velocity:
                    pass
                else:
                    x_control = 0
                    y_control = -velocity
            if event.key == K_DOWN:
                if y_control == -velocity:
                    pass
                else:
                    x_control = 0
                    y_control = velocity

    x_snake = x_snake + x_control
    y_snake = y_snake + y_control

    snake = pygame.draw.rect(screen, (222, 11, 99), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(screen, (150, 6, 6), (x_apple, y_apple, 20, 20))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        score = score + 1
        collision_sound.play()
        initial_length = initial_length + 1
        
    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)
    snake_list.append(head_list)

    if snake_list.count(head_list) > 1 or x_snake < 0 or x_snake > width or y_snake < 0 or y_snake > height:
        font2 = pygame.font.SysFont('comic sans', 20, True, False)
        msg2 = str(f"You died. Press Enter to play again. Your score was {score}")
        txt_formatted2 = font2.render(msg2, True, (255, 0, 0))
        rect_text = txt_formatted2.get_rect()

        died = True
        while died:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        restart_game()

            rect_text.center = (width//2, height//2)
            screen.blit(txt_formatted2, rect_text)
            pygame.display.update()

    if len(snake_list) > initial_length:
        del snake_list[0]

    increase_snake(snake_list)

    screen.blit(txt_formatted, (450, 40))
    pygame.display.update()
