import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.4)  # entre 0 e 1
musica_fundo = pygame.mixer.music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')  # wav ou erro

largura = 640
altura = 480
x = largura/2 - 40/2
y = altura/2 - 50/2
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('comic sans', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("snakely")
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    msg = f"Score:{pontos}"
    txt_formatado = fonte.render(msg, False, (245, 245, 245))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20

        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    # if y >= altura:
    #     y = 0
    # y = y + 1
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()

    tela.blit(txt_formatado, (450, 40))
    pygame.display.update()
