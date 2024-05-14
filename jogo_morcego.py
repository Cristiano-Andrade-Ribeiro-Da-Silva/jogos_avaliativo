import pygame
from personagem import*
from elementos import*

pygame.init()
#Constrindo a tela
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Freeway")
tela.fill((80,120,200))

FUNDO = pygame.image.load("imagens/fundo.jpg")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#Criando mais personagens
jogador1 = Personagem("imagens/personagem.png",80,100,700,400)

#Carregando as imagens
lista_fantasma = [inimigo("imagens/fantasma.png",100,80,0,40),
                 inimigo("imagens/fantasma.png",100,80,40,80),
                 inimigo("imagens/fantasma.png",100,80,80,120),
                 inimigo("imagens/fantasma.png",100,80,120,200)]

lista_obstaculo=[Obstaculo("imagens/objeto.png",60,40,0,40),
                 Obstaculo("imagens/objeto.png",60,40,40,80),
                 Obstaculo("imagens/objeto.png",60,40,80,120)]

lista_bonus=[bonus("imagens/objeto.png",60,40,0,40),
             bonus("imagens/objeto.png",60,40,40,80),
             bonus("imagens/objeto.png",60,40,80,120),
             bonus("imagens/objeto.png",60,40,0,40),
             bonus("imagens/objeto.png",60,40,40,80)]

#fonte
fonte=pygame.font.SysFont("Arial",14,True,True)

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
    
    # movimenta e desenha todos os inimigos
    for Obstaculo in lista_obstaculo:
        Obstaculo.movimenta()
        Obstaculo.desenhar(tela)

        if jogador1.mascara.overlap(Obstaculo.mascara,(Obstaculo.pos_x-jogador1.pos_x,Obstaculo.pos_y-jogador1.pos_y)):
            jogador1.pos_x = 300
            jogador1.pos_y = 450
            jogador1.pontuacao -= 1


    if jogador1.pos_y <= 10:
        jogador1.pos_x = 300
        jogador1.pos_y = 450
        jogador1.pontuacao += 1
    
    texto_pontuacao_morcego=fonte.render(f"Pontuação player: {jogador1.pontuacao}",True,(0,0,0))
    tela.blit(texto_pontuacao_morcego,(0,10))     
  
    # overlap indentifica se se-tocaram
    if jogador1.mascara.overlap(Obstaculo.mascara,(Obstaculo.pos_x-jogador1.pos_x,Obstaculo.pos_y-jogador1.pos_y)):
        jogador1 = Personagem("imagens/morcego1.png",80,100,700,400)

    #Atualizando a tela
    pygame.display.update()

    #Regulando o FPS
    clock.tick(60)
