import pygame
import sys

# --- Configurações Básicas do Jogo ---
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO_JOGO = "Zumzinho e Zum: Eclipse da Mente"
FPS = 60  # Frames por segundo

# Cores (em formato RGB)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL_CLARO = (173, 216, 230)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# --- Inicialização do Pygame ---
pygame.init()  # Inicializa todos os módulos do Pygame
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))  # Cria a janela do jogo
pygame.display.set_caption(TITULO_JOGO)  # Define o título da janela
clock = pygame.time.Clock()  # Cria um objeto Clock para controlar o FPS


#Função Principal do Jogo
def jogar():
    rodando_jogo = True
    while rodando_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando_jogo = False

        tela.fill(VERDE)  # Preenche a tela com verde (cor do jogo)

        # Aqui viria a lógica do seu jogo

        pygame.display.flip()  # Atualiza a tela

    print("Jogo encerrado!")


# --- Loop Principal do Menu ---
def menu_principal():
    rodando_menu = True
    while rodando_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Se o usuário clicar no 'X' da janela
                pygame.quit()  # Finaliza o Pygame
                sys.exit()  # Sai do programa

            if evento.type == pygame.MOUSEBUTTONDOWN:  # Se o mouse for clicado
                mouse_pos = pygame.mouse.get_pos()  # Pega a posição do clique

                # Verifica se o clique foi no botão "Iniciar Jogo"
                if botao_iniciar_rect.collidepoint(mouse_pos):
                    print("Iniciando Jogo...")
                    jogar()  # Chama a função do jogo
                    # Após o jogo terminar, podemos voltar ao menu ou sair
                    rodando_menu = False  # Para sair do loop do menu e finalizar o programa (pode ser ajustado)

                # Verifica se o clique foi no botão "Sair"
                if botao_sair_rect.collidepoint(mouse_pos):
                    print("Saindo do Jogo...")
                    rodando_menu = False  # Sai do loop do menu

        # --- Desenha o Menu ---
        tela.fill(AZUL_CLARO)  # Preenche o fundo do menu

        # Título do Menu
        fonte_titulo = pygame.font.Font(None, 74)  # None usa a fonte padrão, 74 é o tamanho
        texto_titulo = fonte_titulo.render("Zunzinho e Zoom", True, PRETO)  # Renderiza o texto (texto, suavização, cor)

        # Centraliza o título
        texto_titulo_rect = texto_titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 4))
        tela.blit(texto_titulo, texto_titulo_rect)  # Desenha o texto na tela

        # --- Botão "Iniciar Jogo" ---
        fonte_botao = pygame.font.Font(None, 50)
        texto_iniciar = fonte_botao.render("Iniciar Jogo", True, BRANCO)

        # Criando o retângulo do botão (posição e tamanho)
        # x, y, largura, altura
        botao_iniciar_rect = pygame.Rect(0, 0, 250, 60)
        # Centraliza o botão
        botao_iniciar_rect.center = (LARGURA_TELA // 2, ALTURA_TELA // 2)

        # Desenha o fundo do botão
        pygame.draw.rect(tela, VERMELHO, botao_iniciar_rect)
        # Desenha o texto do botão centralizado no retângulo do botão
        texto_iniciar_rect = texto_iniciar.get_rect(center=botao_iniciar_rect.center)
        tela.blit(texto_iniciar, texto_iniciar_rect)

        # --- Botão "Sair" ---
        texto_sair = fonte_botao.render("Sair", True, BRANCO)

        botao_sair_rect = pygame.Rect(0, 0, 250, 60)
        # Posiciona o botão "Sair" abaixo do botão "Iniciar Jogo"
        botao_sair_rect.center = (LARGURA_TELA // 2, ALTURA_TELA // 2 + 80)  # 80 pixels abaixo

        pygame.draw.rect(tela, VERMELHO, botao_sair_rect)
        texto_sair_rect = texto_sair.get_rect(center=botao_sair_rect.center)
        tela.blit(texto_sair, texto_sair_rect)

        pygame.display.flip()  # Atualiza toda a tela para mostrar os elementos desenhados
        clock.tick(FPS)  # Controla o FPS

    pygame.quit()  # Finaliza o Pygame ao sair do loop do menu
    sys.exit()  # Sai do programa


# --- Inicia o Menu ---
if __name__ == '__main__':
    menu_principal()