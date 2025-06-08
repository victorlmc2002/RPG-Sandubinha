import pygame
import sys
from personagem import Sandubinha
from batalha import batalha
from interface import *

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


#Fase 2: Cavernas de Faturamentus
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
