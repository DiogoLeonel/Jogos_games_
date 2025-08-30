import pygame
import sys
from pygame.locals import *
from sys import exit

# --- Configurações Básicas do Jogo ---
largura = 640
altura = 480
titulo = "Snake"
FPS = 60  # Frames por segundo

# Cores (em formato RGB)
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (173, 216, 230)
azul_claro = (173, 216, 230)
vermelho = (255, 0, 0)
vermelho_claro = (255, 100, 100)
verde = (0, 255, 0)
azul_petroleo = (0,128,128)
roxo = (128, 0, 128)

#variáveis para para animar os botões utilizando o "efeito hover" (mudar a cor quando o mouse passar em cima dos botões):
cor_botao_normal = vermelho
cor_botao_hover = vermelho_claro

#funções e variáveis para implementar o recorde do jogo
recordista = ""
recorde = 0

def carregar_recorde():
    try:
        with open("recorde.txt", "r") as arquivo:
            linha = arquivo.readline()
            nome, pontos = linha.strip().split(",")
            return nome, int(pontos)
    except:
        return "Sem record", 0

# --- Inicialização do Pygame ---
pygame.init()  # Inicializa todos os módulos do Pygame
tela = pygame.display.set_mode((largura, altura))  # Cria a janela do jogo
pygame.display.set_caption(titulo)  # Define o título da janela
clock = pygame.time.Clock()  # Cria um objeto Clock para controlar o FPS

# --- Loop Principal do Menu ---
def menu_principal():
    from cobra_jogo import jogo_cobra
    rodando_menu = True

    # Fontes e botões
    fonte_titulo = pygame.font.Font(None, 74)  # None usa a fonte padrão, 74 é o tamanho
    fonte_botao = pygame.font.Font(None, 50)
    # Criando o retângulo do botão (posição e tamanho)
    botao_iniciar_rect = pygame.Rect(0, 0, 250, 60)  # x, y, largura, altura
    botao_iniciar_rect.center = (largura // 2, altura // 2)  # Centraliza o botão
    botao_sair_rect = pygame.Rect(0, 0, 250, 60)
    # Posiciona o botão "Sair" abaixo do botão "Iniciar Jogo"
    botao_sair_rect.center = (largura // 2, altura // 2 + 80)  # 80 pixels abaixo



    while rodando_menu:
        for event in pygame.event.get():
            if event.type == QUIT: #se clicar no botão 'fechar' a janela é fechada e o jogo é encerrado
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: #se pressionar alguma tecla
                if event.key == K_ESCAPE: #se pressionar a tecla 'ESC'
                    pygame.quit()
                    sys.exit() #se pressionar a tecla 'ESC' a janela é fechada e o jogo é encerrado
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Se o mouse for clicado
                mouse_pos = pygame.mouse.get_pos()  # Pega a posição do clique

                # Verifica se o clique foi no botão "Iniciar Jogo"
                if botao_iniciar_rect.collidepoint(mouse_pos):
                   retorno_menu = jogo_cobra()
                   return retorno_menu

                # Verifica se o clique foi no botão "Sair"
                if botao_sair_rect.collidepoint(mouse_pos):
                    rodando_menu = False  # Sai do loop do menu

        # --- Desenha o Menu ---
        tela.fill(azul_claro)  # Preenche o fundo do menu

        # Título do Menu

        texto_titulo = fonte_titulo.render("Jogo da Cobra", True, preto)  # Renderiza o texto (texto, suavização, cor)

        # Centraliza o título
        texto_titulo_rect = texto_titulo.get_rect(center=(largura // 2, altura // 4))
        tela.blit(texto_titulo, texto_titulo_rect)  # Desenha o texto na tela

        #animação dos botões
        mouse_pos = pygame.mouse.get_pos() #captura a posição do mouse

        # --- Botão "Iniciar Jogo" ---

        texto_iniciar = fonte_botao.render("Iniciar Jogo", True, branco)

        # Desenha o fundo do botão e adicionar o "efeito hover" no botão iniciar
        cor_iniciar = cor_botao_hover if botao_iniciar_rect.collidepoint(mouse_pos) else cor_botao_normal
        pygame.draw.rect(tela, cor_iniciar, botao_iniciar_rect)
        # Desenha o texto do botão centralizado no retângulo do botão
        texto_iniciar_rect = texto_iniciar.get_rect(center=botao_iniciar_rect.center)
        tela.blit(texto_iniciar, texto_iniciar_rect)

        # --- Botão "Sair" ---
        texto_sair = fonte_botao.render("Sair", True, branco)

        # Desenha o fundo do botão e adiciona o "efeito hover" no botão sair
        cor_sair = cor_botao_hover if botao_sair_rect.collidepoint(mouse_pos) else cor_botao_normal
        pygame.draw.rect(tela, cor_sair, botao_sair_rect)
        texto_sair_rect = texto_sair.get_rect(center=botao_sair_rect.center)
        tela.blit(texto_sair, texto_sair_rect)

        #texto do recorde do game
        recordista, recorde = carregar_recorde()
        fonte_recorde = pygame.font.Font(None, 50)
        texto_recorde = fonte_recorde.render(f"Recorde: {recordista} {recorde}", True, roxo)

        # posicionar o recorde na parte inferior da tela
        texto_recorde_rect = texto_recorde.get_rect()
        texto_recorde_rect.bottomright = (largura - 20, altura - 20)
        tela.blit(texto_recorde, texto_recorde_rect)

        pygame.display.flip()  # Atualiza toda a tela para mostrar os elementos desenhados
        clock.tick(FPS)  # Controla o FPS

    pygame.quit()  # Finaliza o Pygame ao sair do loop do menu
    sys.exit()  # Sai do programa

# --- Inicia o Menu ---
if __name__ == '__main__':
    menu_principal()