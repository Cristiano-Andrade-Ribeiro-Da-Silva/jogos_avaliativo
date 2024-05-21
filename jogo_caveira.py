import pygame
import time
from elementos import*

pygame.init()
#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Freeway")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens/fundo.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
jogador1 = Personagem("imagens/personagem.png",100,100,700,400)

#Carregando as imagens
lista_fantasma = [fantasma("imagens/fantasma.png",100,80,0,40),
                  fantasma("imagens/fantasma.png",100,80,40,40),
                  fantasma("imagens/fantasma.png",100,80,80,40),
                  fantasma("imagens/fantasma.png",100,80,120,40),
                  fantasma("imagens/fantasma.png",100,80,180,40),
                  fantasma("imagens/fantasma.png",100,80,200,40),
                  fantasma("imagens/fantasma.png",100,80,220,40),
                  fantasma("imagens/fantasma.png",100,80,240,40)]

lista_obstaculo=[bomba("imagens/objeto.png",60,40,0,40),
                 bomba("imagens/objeto.png",60,40,40,80),
                 bomba("imagens/objeto.png",60,40,80,120)]

lista_bonus=[veja("imagens/bonus.png",80,60,10,40),
             veja("imagens/bonus.png",80,60,700,80),
             veja("imagens/bonus.png",80,60,500,120),
             veja("imagens/bonus.png",80,60,200,40),
             veja("imagens/bonus.png",80,60,100,80)]

#fonte
fonte_pontuacao=pygame.font.SysFont("Arial",20,True,True)
fonte_perdeu=pygame.font.SysFont("Arial",40,True,True)
#Criando um relogio para controlar o FPS
clock = pygame.time.Clock()

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))

    #Desenhando as imagens
    jogador1.movimentar_via_controle(pygame.K_d,pygame.K_a) or jogador1.movimentar_via_controle(pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.desenhar(tela)

    # movimenta e desenha todos os inimigos
    for inimigo in lista_fantasma:
        inimigo.movimenta()
        inimigo.desenhar(tela)
    
    # movimenta e desenha todos os obstaculos
    for Obstaculo in lista_obstaculo:
        Obstaculo.movimenta()
        Obstaculo.desenhar(tela)
        
        # overlap indentifica se se-tocaram
        if jogador1.mascara.overlap(Obstaculo.mascara,(Obstaculo.pos_x-jogador1.pos_x,Obstaculo.pos_y-jogador1.pos_y)):
                
                texto_perdeu=fonte_perdeu.render(f"vc perdeu com {jogador1.pontuacao} pontos",True,(255,255,255))
                tela.blit(texto_perdeu,(200,150)) 
                pygame.display.update()
                time.sleep(2)
                rodando=False
    # movimenta e desenha todos os itens bonus
    for bonus in lista_bonus:
        bonus.movimenta()
        bonus.desenhar(tela)

        # overlap indentifica se se-tocaram
        if jogador1.mascara.overlap(bonus.mascara,(bonus.pos_x-jogador1.pos_x,bonus.pos_y-jogador1.pos_y)):
                jogador1.pontuacao += 1

    texto_pontuacao_morcego=fonte_pontuacao.render(f"Pontuação player: {jogador1.pontuacao}",True,(0,0,0))
    tela.blit(texto_pontuacao_morcego,(0,10))     

    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)

