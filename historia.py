import time
import os
from personagem import Sandubinha
from batalha import batalha

VELOCIDADE_TEXTO = 0.05

def escrever_mensagem(texto):
    for c in texto:
        print(c, end="", flush=True)
        time.sleep(VELOCIDADE_TEXTO)

def floresta_do_atendimentus(sandu):
    escrever_mensagem("\n🌲 Floresta do Atendimentus\n " \
    "Um lugar encantado onde almas feridas encontram cura.\n" \
    " Sandubinha percorre a floresta e encontra um monstro tenebroso.\n" \
    " Sandubinha: Então você é meu primeiro desafio nessa floresta encantada?\n" \
    " Monstro: Bem-vindo. Sou Processus Ministerii, mas quem lutará com você é o Monstrengo.\n " \
    "Surge um ser humanoide entre as pernas do monstro gigante...\n" \
    " Sandubinha: Primeiro, não é enfraquecer, vou dar um fim total em Glozium... Venha monstro!\n")

    input("Pressione Enter para iniciar a batalha...")

    vitoria = batalha(sandu, "Monstrengo", vida_inimigo=3, numeros_por_rodada=1)
    if vitoria:
        escrever_mensagem("\nProcessus: Muito obrigado, tome o artefato 'Guia de Atendimento' e siga para o próximo desafio.")
        sandu.ganhar_item("Guia de Atendimento")
    else:
        escrever_mensagem("\nProcessus: Oh não... o mundo será mais uma vez destruído por Glozium...")
        escrever_mensagem("O mundo foi destruído por Glozium. Fim de jogo!")
        input("Pressione Enter para voltar ao menu...")
        return

    input("\nPressione Enter para voltar ao menu...")

def tela_inicial():
    print("|||||  A Jornada Do Sandubinha  |||||")
    print("1 - Começar a aventura")
    print("2 - Introdução")
    print("3 - Sair")
    opcao = 0
    while opcao not in [1, 2, 3]:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            iniciar_jogo()
        elif opcao == 2:
            introducao()
        elif opcao == 3:
            return
        else:
            print("Opção inválida")
            time.sleep(3)

def introducao():
    escrever_mensagem("\nEm um mundo ameaçado por forças sombrias, o jovem guerreiro Sandubinha é convocado pela antiga guilda de Zerum Glozium.")
    escrever_mensagem("\nSua missão: impedir que Glozium espalhe a escuridão pela província de Hospitalis.\n")
    input("\n\nAperte Enter para voltar ao Menu...")
    os.system('cls')
    tela_inicial()

def iniciar_jogo():
    sandu = Sandubinha()
    escrever_mensagem("\nVocê acorda com uma sensação estranha... É hora de iniciar sua missão épica!\n")
    input("Pressione Enter para continuar...")
    floresta_do_atendimentus(sandu)
    os.system('cls')
    tela_inicial()
