import pygame
import sys

pygame.init()

VELOCIDADE_TEXTO = 50
FONTE = pygame.font.SysFont("arial", 28)
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))

def desenhar_texto(texto, x=40, y=50, fundo=None):
    if fundo:
        TELA.blit(fundo, (0, 0))
    else:
        TELA.fill((30, 30, 30))
    linhas = texto.split('\n')
    for i, linha in enumerate(linhas):
        img = FONTE.render(linha, True, (255, 255, 255))
        TELA.blit(img, (x, y + i * 40))
    pygame.display.flip()

def esperar_enter():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def desenhar_fundo(fundo):
    if fundo:
        TELA.blit(fundo, (0, 0))
    else:
        TELA.fill((30, 30, 30))

def escrever_mensagem(texto, x=40, y=450, fundo=None):
    desenhar_fundo(fundo)
    linhas = quebrar_texto(texto, LARGURA - 80)
    desenhar_texto_animado(linhas, x, y, fundo)

def quebrar_texto(texto, largura_max):
    linhas = []
    palavras = texto.split(' ')
    linha_atual = ""
    for palavra in palavras:
        teste_linha = linha_atual + ("" if linha_atual == "" else " ") + palavra
        largura = FONTE.size(teste_linha)[0]
        if largura > largura_max:
            if linha_atual == "":
                for i in range(len(palavra)):
                    teste_palavra = palavra[:i+1]
                    largura_p = FONTE.size(teste_palavra)[0]
                    if largura_p > largura_max:
                        linhas.append(palavra[:i])
                        linha_atual = palavra[i:]
                        break
            else:
                linhas.append(linha_atual)
                linha_atual = palavra
        else:
            linha_atual = teste_linha
    if linha_atual:
        linhas.append(linha_atual)
    return linhas

def desenhar_texto_animado(linhas, x, y, fundo):
    idx_linha = 0
    desenhar_fundo(fundo)
    for linha in linhas:
        buffer_linha = ""
        for c in linha:
            buffer_linha += c
            for i in range(idx_linha):
                img = FONTE.render(linhas[i], True, (255, 255, 255))
                TELA.blit(img, (x, y + i * 40))
            img = FONTE.render(buffer_linha, True, (255, 255, 255))
            TELA.blit(img, (x, y + idx_linha * 40))
            pygame.display.flip()
            pygame.time.wait(VELOCIDADE_TEXTO)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return
        idx_linha += 1
    esperar_enter()