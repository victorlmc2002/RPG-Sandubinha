import time
import os
VELOCIDADE_TEXTO = 0.05

def escrever_mensagem(texto):
    for c in texto:
        print(c, end= "")
        time.sleep(VELOCIDADE_TEXTO)

def tela_inicial():
    print("|||||  A Jornada Do Sandubinha  |||||")
    print("1 - Começar a aventura")
    print("2 - Introdução")
    print("3 - Sair")
    while True:
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
    tela_inicial()

def iniciar_jogo():
    escrever_mensagem("\nVocê acorda com uma sensação estranha... É hora de iniciar sua missão épica!\n\n")
    input("Pressione Enter para continuar...")
    print("(As fases ainda serão implementadas...)\n")
    input("Pressione Enter para voltar ao menu...")
    
