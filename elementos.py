import pygame
import random
class Personagem:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.mascara=pygame.mask.from_surface(self.imagem)

        self.pontuacao = 0
        
    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))



    def movimentar_via_controle(self,direita,esquerda):
        teclas = pygame.key.get_pressed()

        if teclas[esquerda]:
            if self.pos_x >= 0:
                self.pos_x = self.pos_x - 8

        if teclas[direita]:
            if self.pos_x <= 800-self.largura:
                self.pos_x = self.pos_x + 8

class fantasma:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.velocidade=random.randint(4,6)

    def movimenta(self):
        self.pos_x = self.pos_x + self.velocidade
        if self.pos_x >800:
            self.pos_x=0
            self.velocidade=random.randint(4,6)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))

class bomba:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.velocidade=random.randint(5,8)

        self.mascara=pygame.mask.from_surface(self.imagem)

    def movimenta(self):
        self.pos_y = self.pos_y + self.velocidade
        if self.pos_y >700:
            self.pos_y=0
            self.pos_x=random.randint(0,800)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))

class veja:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.velocidade=random.randint(5,8)

        self.mascara=pygame.mask.from_surface(self.imagem)

    def movimenta(self):
        self.pos_y = self.pos_y + self.velocidade
        if self.pos_y >800:
            self.pos_y=0
            self.pos_x=random.randint(0,800)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y))
