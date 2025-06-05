import pygame
import sys
from personagem import Sandubinha
from batalha import batalha

VELOCIDADE_TEXTO = 50  # milissegundos por caractere

# Inicialização do pygame
pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("A Jornada Do Sandubinha")
FONTE = pygame.font.SysFont("arial", 28)
CLOCK = pygame.time.Clock()

def desenhar_texto(texto, y=50):
    TELA.fill((30, 30, 30))
    linhas = texto.split('\n')
    for i, linha in enumerate(linhas):
        img = FONTE.render(linha, True, (255, 255, 255))
        TELA.blit(img, (40, y + i * 40))
    pygame.display.flip()

def esperar_enter():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
        

def escrever_mensagem(texto):
    TELA.fill((30, 30, 30))
    x, y = 40, 50
    linhas = []
    largura_max = LARGURA - 80 
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

    idx_linha = 0
    for linha in linhas:
        buffer_linha = ""
        for c in linha:
            buffer_linha += c
            TELA.fill((30, 30, 30))
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

#Fase 1: Floresta do Atendimentus
def floresta_do_atendimentus(sandu):
    escrever_mensagem("     Floresta do Atendimentus")
    escrever_mensagem("Um lugar encantado,dizem que pessoas doentes ou com almas feridas podem ir a floresta para serem curadas.")
    escrever_mensagem("Sandubinha percorre a floresta e encontra um monstro tenebroso.")
    escrever_mensagem("Sandubinha: Então você é meu primeiro desafio nessa floresta encantada?")
    escrever_mensagem("Processus: Bem-vindo, vejo que você é um dos escolhidos para enfraquecer Glozium, meu nome é Processus ministerii.")
    escrever_mensagem("Processus: Sou o ser mágico que atende as almas feridas, envio os informativos disso as cavernas de Faturamentus.")
    escrever_mensagem("Processus: Você não irá lutar comigo, mas sim contra esse ser criado por Glozium chamado Monstrengo.")
    escrever_mensagem("Seres mágicos do meu tipo não podem ser afetados por Glozium, mas também não podem lutar contra, ele me atrapalha me desconcentrando e provocando erros.")
    escrever_mensagem("Surge entre as pernas do grande monstro um ser humanoide, da altura de Sandubinha.")
    escrever_mensagem("Sandubinha: Primeiro, não é enfraquecer, vou dar um fim total em Glozium... Venha monnstro gigante!")
    desenhar_texto("Pressione Enter para iniciar a batalha...")

    vitoria = batalha(sandu, "Monstrengo", vida_inimigo=3, numeros_por_rodada=1)
    if vitoria:
        escrever_mensagem("Processus: Muito obrigado, tome o artefato 'Guia de Atendimento' e siga para o próximo desafio.")
        sandu.ganhar_item("Guia de Atendimento")
    else:
        escrever_mensagem("Processus: Oh não... o mundo será mais uma vez destruído por Glozium...")
        escrever_mensagem("O mundo foi destruído por Glozium. Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()


# Fase 2: Cavernas de Faturamentus
def cavernas_de_faturamentus(sandu):
    escrever_mensagem("     Cavernas de Faturamentus")
    escrever_mensagem("Existe sempre um preço a se pagar pela cura do corpo e da alma...")
    escrever_mensagem("Após a floresta do atendimentus, o preço é calculado pelo tipo de contrato divino.")
    escrever_mensagem("Percorrendo a caverna segurando uma tocha.")
    escrever_mensagem("Sandubinha escuta grunhidos e vê fantasmas anotando coisas em pergaminhos.")
    escrever_mensagem("O cenário é iluminado por minérios misteriosos. Anciões fantasmas anotam diversas coisas em pergaminhos, estão todos muito ocupados para falar algo a Sandubinha")
    escrever_mensagem("Um monstro em forma de urso surge e diz a Sandubinha:")
    escrever_mensagem("Urso Sangrento: Finalmente diversão! Vamos lutar heroizinho!")
    escrever_mensagem("Sandubinha: Criatura desagradável, nem me deu tempo de tomar uma água!")

    vitoria = batalha(sandu, "Urso Sangrento", vida_inimigo=6, numeros_por_rodada=2)
    if vitoria:
        escrever_mensagem("Ancião Faturador: Muito obrigado, mas tô ocupado demais para agradecimentos longos, tome o artefato sagrado e siga em frente.")
        sandu.ganhar_item("Faturamentus")
    else:
        escrever_mensagem("Ancião Faturador: Herói merda, nem para cumprir o trabalho dele, estamos perdidos!")
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()

def menu_fases(sandu):
    while True:
        TELA.fill((30, 30, 30))
        desenhar_texto("Escolha uma fase:\n1 - Floresta do Atendimentus\n2 - Cavernas de Faturamentus\n3 - Voltar ao menu", 100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    floresta_do_atendimentus(sandu)
                elif event.key == pygame.K_2:
                    cavernas_de_faturamentus(sandu)
                elif event.key == pygame.K_3:
                    if alerta():
                        tela_inicial()
                    else:
                        continue
def alerta():
    desenhar_texto("            Atenção!\n\n Se você voltar ao menu," \
    " perderá o progresso atual." \
    "\n\nPressione Enter para continuar..." \
    "\n\nPressione qualquer outra tecla para continuar...")
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return event.key == pygame.K_RETURN

def tela_inicial():
    while True:
        TELA.fill((30, 30, 30))
        desenhar_texto("       A Jornada Do Sandubinha     \n\n1 - Começar a aventura\n2 - Introdução\n3 - Sair", 100)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    iniciar_jogo()
                elif event.key == pygame.K_2:
                    introducao()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()


def introducao():
    escrever_mensagem("Em um mundo ameaçado por forças sombrias, o jovem guerreiro Sandubinha é convocado pela antiga guilda de Zerum Glozium.")
    escrever_mensagem("Sua missão: impedir que Glozium espalhe a escuridão pela província de Hospitalis.")
    escrever_mensagem("Aperte Enter para voltar ao Menu...")

def iniciar_jogo():
    sandu = Sandubinha()
    escrever_mensagem("Você acorda com uma sensação estranha... É hora de iniciar sua missão épica!")
    desenhar_texto("Pressione Enter para continuar...")
    menu_fases(sandu)

if __name__ == "__main__":
    tela_inicial()
