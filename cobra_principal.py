#Importação de bibliotecas necessárias para executar o jogo
import pygame
from pygame.locals import *
from sys import exit
from random import randint
from cobra_menu import menu_principal
from cobra_jogo import jogo_cobra, reiniciar_jogo


#variáveis e funções utilizadas para controlar o game

def principal():
    while True:
        escolha = menu_principal()
        if escolha == "jogar":
            resultado = jogo_cobra()
            if resultado == "reiniciar":
                continue
            elif resultado == "menu":
                continue
            elif resultado == "sair":
                break

#Inicialiação
pygame.init() #inicia todos os módulos do Pygame

principal()

