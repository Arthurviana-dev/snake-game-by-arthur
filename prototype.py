import pygame
import random
pygame.init()
#criação dos objetos
largura,altura = 600,400
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("snake game by arthur")
cobra = [(100,50)]
comida = (300,200)
direção = (0,0)
#desenhar os objetos na tela
def desenhar():
    tela.fill((0,180,0))
    pygame.draw.rect(tela,(255,0,0),(*comida,10,10))
    for parte in cobra:
        pygame.draw.rect(tela,(0,0,255),(*parte,10,10))
        pygame.display.update()

rodando = True
relogio = pygame.time.Clock()
#Criar eventos do jogo enquanto estiver rodando
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT and direção != (10,0):
                direção = (-10,0)
            if evento.key == pygame.K_RIGHT and direção != (-10,0):
                direção = (10,0)
            if evento.key == pygame.K_UP and direção != (0,10):
                direção = (0,-10)
            if evento.key == pygame.K_DOWN and direção != (0,-10):
                direção = (0,10)
#verificando colisão
    if direção != (0,0):
        nova_cabeça = cobra[0][0] + direção[0],cobra[0][1] + direção[1]
        if nova_cabeça[0] < 0 or nova_cabeça[0] > largura or nova_cabeça[1] < 0 or nova_cabeça[1] > altura or nova_cabeça in cobra:
            rodando = False
        else:
            cobra.insert(0,nova_cabeça)
        if nova_cabeça == comida:
            comida = random.randrange(0,largura,10),random.randrange(0,altura,10)
        else:
            cobra.pop()
        relogio.tick(20)
    desenhar()

pygame.quit()
