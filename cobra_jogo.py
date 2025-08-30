#importar a biblioteca pygame e algumas funções
import pygame
import sys
import os
from pygame.locals import *
from sys import exit
from random import randint
#from cobra_menu import menu_principal

#definição das variáveis para a configuração do jogo

#declaração do FPS do Jogo
relogio = pygame.time.Clock() #cria uma variável para controlar o tempo do jogo (frames por segundo - FPS)
dificuldade = 30
nivel = 0

#Declaração das variáveis para a configuração da tela
largura = 640
altura = 480
titulo = 'Snake'

#Declaração das variáveis para as Cores utilizadas no jogo (em formato RGB)
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (173, 216, 230)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul_petroleo = (0,128,128)
roxo = (128, 0, 128)

#declaração das variáveis para dar movimento ao objeto 'cobra'
x_cobra = largura/2 #o objeto fica no meio da tela
y_cobra = altura/2 #o objeto fica no meio da tela
velocidade = 10
x_controle = velocidade
y_controle = 0

#declarar as variáveis para controlar a movimentação da 'fruta' após as colisões com a 'cobra'
x_fruta = randint(40, 600)
y_fruta = randint(50, 430)

#Inicialiação
pygame.init() #inicia todos os módulos do Pygame
tela = pygame.display.set_mode((largura, altura)) #Cria a janela do jogo
pygame.display.set_caption(titulo) #Define o título da janela

#declarar as variaveis para o tamanho e fonte do texto da pontuação
pontos = 0 #variável que receberá a pontuação (quantidade de colisões realizadas)
fonte = pygame.font.SysFont('inkfree', 40, True, True) #nome a fonte, tamanho, negrito, itálico

#declaração de funções e variáveis que tratam o recorde
recordista = ""
recorde = 0
def carregar_recorde():
    try:
        with open("recorde.txt", "r") as arquivo:
            nome, pontos = arquivo.readline().strip().split(",")
            return nome, int(pontos)
    except:
        return "Sem record", 0

def salvar_recorde(nome, pontos):
    with open("recorde.txt", "w") as arquivo:
        arquivo.write(f"{nome},{pontos}")

#função para solicitar o nome do recordista
def solicitar_nome():
    nome = ""
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 40)
    ativo = True

    while ativo:
        tela.fill(branco)
        texto = fonte.render("Novo recorde! Digite seu nome:", True, roxo)
        texto_nome = fonte.render(nome, True, roxo)
        tela.blit(texto, (100, 150))
        tela.blit(texto_nome, (100, 200))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    ativo = False
                elif event.key == K_BACKSPACE:
                    nome = nome[:-1]
                else:
                    nome += event.unicode
        pygame.display.update()
        clock.tick(30)
    return nome

#Iniciar o mixer:
pygame.mixer.init()
#função para obter o caminho absoluto dos arquivos de som:
def caminho_relativo(nome_arquivo):
    pasta_base = getattr(sys, 'MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(pasta_base, nome_arquivo)

#Carregar e reproduzir a música de fundo
pygame.mixer.music.set_volume(0.3) #valores entre 0 e 1 - valores maiores que 1 não fazem diferença
pygame.mixer.music.load(caminho_relativo(os.path.join('recursos', 'musicas', 'BoxCat Games - CPU Talk.mp3')))
#comando para tocar a musica, o parâmetro '-1' serve para a música entrar em loop
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound(caminho_relativo(os.path.join('recursos', 'sons', 'smw_coin.wav')))
som_colisao.set_volume(0.7) #volume do som da colisão



#declarar as variáveis e funções para controlar a lista que definirá o tamanho da cobra
comprimento_inicial = 5
lista_cobra = []  # lista que armazena os valores da lista_cabeca para desenhar o corpo da cobra
def aumenta_cobra(lista_cobra): #função que desenha a cobra
    for XeY in lista_cobra: #variavel XeY 'pega' as posições x e y de cada posição
        pygame.draw.rect(tela,verde,(XeY[0], XeY[1], 20, 20))

morreu = False
#Variáveis e funções que controlam o reinício do jogo
def reiniciar_jogo():
    global pontos, dificuldade, nivel, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_fruta, y_fruta, morreu
    pontos = 0 #zera a quantidade de pontos
    dificuldade = 30
    nivel = 0
    comprimento_inicial = 5 #redefine o tamanho da cobra
    x_cobra = largura / 2  # o objeto fica no meio da tela
    y_cobra = altura / 2  # o objeto fica no meio da tela
    lista_cobra = [] #limpa a memória da lista da cobra
    lista_cabeca = [] #limpa a memória da lista da cabeça
    x_fruta = randint(40, 600) #redefine a posição da fruta
    y_fruta = randint(50, 430) #redefine a posição da fruta
    morreu = False

def game_over():
    global morreu
    morreu = True

    recordista_atual, recorde_atual = carregar_recorde()

    if pontos > recorde_atual:
        nome = solicitar_nome()
        salvar_recorde(nome, pontos)
    # mensagem "game over"
    fonte2 = pygame.font.SysFont('Arial', 15, False, False)
    mensagem_game_over = 'Game Over! Pressione a tecla R para JOGAR NOVAMENTE, V para voltar para o MENU PRINCIPAL ou ESC para SAIR'
    texto_formatado = fonte2.render(mensagem_game_over, True, preto)
    ret_texto = texto_formatado.get_rect()  # cria um retangulo para envolver o texto
    tela.fill(branco)
    while morreu:
        #tela.fill(branco)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_r:
                    #reiniciar_jogo()
                    return "reiniciar"
                elif event.key == K_v:
                    #menu_principal()
                    reiniciar_jogo()
                    return "menu"
                elif event.key == K_ESCAPE:  # se pressionar a tecla 'ESC'
                    pygame.quit()
                    exit()  # se pressionar a tecla 'ESC' a janela é fechada e o jogo é encerrado
            elif event.type == QUIT:  # se clicar no botão 'fechar' a janela é fechada e o jogo é encerrado
                pygame.quit()
                exit()

        ret_texto.center = (largura / 2, altura / 2)  # centraliza o 'retangulo' que envolve o texto
        tela.blit(texto_formatado, ret_texto)
        pygame.display.update()

#variáveis e funções que controlam a vida e Fim de jogo


def jogo_cobra():
    global x_cobra, y_cobra, x_controle, y_controle, pontos, comprimento_inicial
    global lista_cobra, lista_cabeca, x_fruta, y_fruta, morreu, dificuldade, nivel

    while True:
        relogio.tick(dificuldade)  # controla o FPS do jogo
        tela.fill(branco) #tela é preenchida de preto a cada loop

        #Borda da tela
        pygame.draw.rect(tela, azul_petroleo, (0,0, 640, 10))
        pygame.draw.rect(tela, azul_petroleo, (0,470, 640, 10))
        pygame.draw.rect(tela, azul_petroleo, (0,0,10,480))
        pygame.draw.rect(tela, azul_petroleo, (630, 0, 10, 480))


        mensagem = f'Pontos: {pontos}' #concatena o texto 'Pontos: ' com quantidade de pontos da variável 'pontos'
        texto_formatado = fonte.render(mensagem, True, preto) #aplica a formatação definida na variável 'fonte' ao texto incluído na variável 'mensagem' (antialias: forma texto)
        for event in pygame.event.get():
            if event.type == QUIT: #se clicar no botão 'fechar' a janela é fechada e o jogo é encerrado
                pygame.quit()
                exit()
            elif event.type == KEYDOWN: #se pressionar alguma tecla
                if event.key == K_ESCAPE: #se pressionar a tecla 'ESC'
                    pygame.quit()
                    exit() #se pressionar a tecla 'ESC' a janela é fechada e o jogo é encerrado

            #movimentação do objeto, impedindo o jogador de se movimentar na direção contrária
            if event.type == KEYDOWN:
                if event.key == K_LEFT:  # se a tecla 'seta para a esquerda' for pressionada
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade  # objeto será movido para a esquerda
                        y_controle = 0
                elif event.key == K_RIGHT:  # se a tecla 'seta para a direita' for pressionada
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade  # objeto será movido para a direita
                        y_controle = 0
                elif event.key == K_UP:  # se a tecla 'seta para cima' for pressionada
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade  # objeto será movido para cima
                        x_controle = 0
                elif event.key == K_DOWN:  # se a tecla 'seta para baxo' for pressionada
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade  # objeto será movido para baixo
                        x_controle = 0

        #continuamente as variáveis de localização do objeto "cobra" recebe valores definidos no loop acima, fazendo com que a cobra sempre semovimente para a ultima direção
        x_cobra = x_cobra + x_controle
        y_cobra = y_cobra + y_controle

          # declaração dos objetos do jogo
        cobra = pygame.draw.rect(tela, verde, (x_cobra,y_cobra,20,20))
        fruta = pygame.draw.rect(tela, vermelho, (x_fruta, y_fruta,20,20))

        if cobra.colliderect(fruta):
            x_fruta = randint(40, 600)
            y_fruta = randint(50, 430)
            pontos = pontos + 1
            nivel = nivel + 1
            if nivel == 10:
                dificuldade = dificuldade + 10
                nivel = 0

            som_colisao.play() #função para tocar o som quando a colisão ocorre
            comprimento_inicial = comprimento_inicial + 1
        tela.blit(texto_formatado, (450,40)) #apresenta o texto na tela

        # declarar as variáveis e funções para controlar a lista que definirá o tamanho da cobra
        lista_cabeca = []  # lista que armazena a posição da cabeça da cobra
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)
        lista_cobra.append(lista_cabeca)

        #Morte e Game Over / Reinício do game

        #colisão relacionada ao contato da cabeça com o corpo
        if lista_cobra.count(lista_cabeca) > 1 or x_cobra <= 10 or  x_cobra >= 630 or  y_cobra <= 10 or y_cobra >= 470:
            resultado = game_over()
            if resultado == "reiniciar":
                reiniciar_jogo()
                continue
            return resultado


        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]

        aumenta_cobra(lista_cobra)

        pygame.display.update()

if __name__ == "__main__":
    jogo_cobra()