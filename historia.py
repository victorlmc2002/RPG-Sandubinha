import pygame
import sys
from personagem import Sandubinha
from batalha import batalha
from interface import *

#Fase 1: Floresta do Atendimentus
def floresta_do_atendimentus(sandu):
    escrever_mensagem("Floresta do Atendimentus", LARGURA/2 - LARGURA/8)
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

    vitoria = batalha(sandu, "Monstrengo", 3, 1)
    if vitoria == 0:
        escrever_mensagem("Processus: Muito obrigado, tome o artefato 'Guia de Atendimento' e siga para o próximo desafio.")
        sandu.ganhar_item("Guia de Atendimento")
        return
    elif vitoria == 1:
        escrever_mensagem("Processus: Oh não... o mundo será mais uma vez destruído por Glozium...")
        escrever_mensagem("O mundo foi destruído por Glozium. Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()
    else:
        return


#Fase 2: Cavernas de Faturamentus
def cavernas_de_faturamentus(sandu):
    escrever_mensagem("Cavernas de Faturamentus", LARGURA/2 - LARGURA/8)
    escrever_mensagem("Existe sempre um preço a se pagar pela cura do corpo e da alma...")
    escrever_mensagem("Após a floresta do atendimentus, o preço é calculado pelo tipo de contrato divino.")
    escrever_mensagem("Percorrendo a caverna segurando uma tocha.")
    escrever_mensagem("Sandubinha escuta grunhidos e vê fantasmas anotando coisas em pergaminhos.")
    escrever_mensagem("O cenário é iluminado por minérios misteriosos. Anciões fantasmas anotam diversas coisas em pergaminhos, estão todos muito ocupados para falar algo a Sandubinha")
    escrever_mensagem("Um monstro em forma de urso surge e diz a Sandubinha:")
    escrever_mensagem("Urso Sangrento: Finalmente diversão! Vamos lutar heroizinho!")
    escrever_mensagem("Sandubinha: Criatura desagradável, nem me deu tempo de tomar uma água!")

    vitoria = batalha(sandu, "Urso Sangrento", 6, 2)
    if vitoria == 0:
        escrever_mensagem("Ancião Faturador: Muito obrigado, mas tô ocupado demais para agradecimentos longos, tome o artefato sagrado e siga em frente.")
        sandu.ganhar_item("Faturamentus")
        return
    elif vitoria == 1:
        escrever_mensagem("Ancião Faturador: Herói merda, nem para cumprir o trabalho dele, estamos perdidos!")
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()
    else: 
        return

#Fase 3: Vila da Transmissão
def vila_da_trasmissao(sandu):
    escrever_mensagem("Vila da Transmissão", LARGURA/2 - LARGURA/8)
    escrever_mensagem("Uma vila mágica que recebe cobranças vindas das cavernas de Faturamentus. Os moradores entregam as mensagens na Torre")
    escrever_mensagem("Sandubinha é bem recebido em sua chegada. Ele é convidado para um jantar ritualístico com comidas típicas")
    escrever_mensagem("Os moradores contam que o monstro a ser enfrentado é um ser que voa. Para atacá-lo, o Sandubinha terá que derrubar o monstro e usar sua espada. Então, dão a ele um item, o Estilingue Mágico")
    sandu.ganhar_item("Estilingue Mágico")
    escrever_mensagem("Logo, um monstro em forma de dragão surge voando...")
    escrever_mensagem("Dragão da transmissão: Você já tem sua arma... já fui guardião dessas terras e transmitia as mensagens à torre. Mas milénios atrás Glozium me tornou seu escravo, sou obrigado a lutar com toda fúria. Livre-me do sofrimento...")
    escrever_mensagem("Sandubinha: Você também está preso a um destino que não escolheu, vou te libertar!")
    
    vitoria = batalha(sandu, "Dragão da Transmissão", 12, 3)
    if vitoria == 0:
        escrever_mensagem("Dragão: Muito obrigado, todo herói evitava essa batalha e seguia para a torre, agora sou livre!")
        escrever_mensagem("Sandubinha: Evitava? E dá para seguir sem lutar? como assim? Sandubinha ganha o artefato Azah Transmissão")
        sandu.ganhar_item("Azah Transmissão")
        return
    elif vitoria == 1:
        escrever_mensagem("Dragão - Sinto muito herói, que sua alma seja livre...")
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()
    else:
        return
    
#Fase 4: Torre de Contas a Receber
def torre_de_contas_a_receber(sandu):
    escrever_mensagem("Torre de Contas a Receber", LARGURA/2 - LARGURA/8)
    escrever_mensagem("A terrível torre é onde seres mágicos recebem o pagamento por seu árduo trabalho. Dizem que a ruína perto da torre eram a cidade mais próxima do grito, terra natal dos Analyticaes di Glosium")
    escrever_mensagem("Sandubinha chega ao primeiro andar da torre. Ele sente uma energia mágica mortífera vindo do topo. Sem dúvidas, Glozium estava lá...")
    escrever_mensagem("A parede se abre e sai dela o penúltimo monstro a ser enfrentado")
    escrever_mensagem("Sandubinha: Uma estátua na forma do último herói, por que?")
    
    vitoria = batalha(sandu, "Estátua do Último Herói", 25, 5)
    if vitoria == 0:
        escrever_mensagem("É assustador olhar para essa estátua despedaçada e ver a forma do último herói")
        sandu.ganhar_item("Colar da Estátua Sagrada")
        return
    elif vitoria == 1:
        escrever_mensagem("Estátua do último herói: ...")
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()
    else:
        return

#Batalha contra Glozium (final)
def batalha_final(sandu):
    escrever_mensagem("Batalha Final", LARGURA/2 - LARGURA/8)
    TELA.fill((200, 30, 30))
    if len(sandu._itens) == 5:
        while True:
            desenhar_texto("ATENÇÃO\nSandubinha coletou todos os itens precisos para Espada ZG" \
            "\nVocê deseja voltar e criar a arma ou seguir sem ela?" \
            "\n\n\n\nEnter para voltar e criar a espada" \
            "\nEsc para continuar sem ela")
            continuar = False

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    continuar = True
            if continuar:
                break

    escrever_mensagem("Sandubinha sente que no topo da Torre de Contas a Receber reside Glozium, é uma habilidade dos Analyticaes di Glosium")
    escrever_mensagem("Sandubinha entra na sala do chefe e se depara com a presença arrepiante de Glozium sentado no trono")
    escrever_mensagem("Glozium: Um rato invadiu meu recinto; talvez sirva de alimento para meus escravos")
    escrever_mensagem("Sandubinha: Então você é Glozium? Não é mais aterrorizante que as criaturas apodrecidas que encontrei")
    escrever_mensagem("Glozium: Ha ha ha ha! Que petulante! Chegou a época, mas mandaram um pobre coitado; péssima ideia!")
    escrever_mensagem("Sandubinha: Vou te destruir, Glozium, e garantir sua aniquilação total e permanente!")
    escrever_mensagem("Glozium: E o que um garoto com cabeça de hambúrguer pode fazer contra um monstro milenar, que presenciou eventos tão singulares, que caminhou sobre a superfície de vulcões e subjugou a humanidade?")
    escrever_mensagem("Sandubinha lança sua espada girando no ar que fere o monstro e retorna a sua mão")
    escrever_mensagem("Sandubinha: Não subestime alguém com cabeça de hambúrguer, sou um descendente dos Analyticaes di Glosium. Te procurei em cada canto do inferno para reduzir você a zero")
    escrever_mensagem("Glozium: Interessante, aceito seu pedido de batalha")
    vitoria = batalha(sandu, "Glozium", 100, 10)

    if vitoria == 0 and "Espada ZG" in sandu._itens:
        escrever_mensagem("Sandubinha: Finalmente, Glozium está eliminado por completo, irei retornar a minha família")
        escrever_mensagem("O herói derrotou Glozium, o mundo agora poderá voltar a seus tempos de alegria. Muito obrigado, herói!")
        escrever_mensagem("Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()

    elif vitoria == 0 and "Espada ZG" not in sandu._itens:
        escrever_mensagem("Glozium: Você me derrotou com armas tão simples, impressionante, mas irei retornar no ano seguinte")
        escrever_mensagem("Sandubinha - ...retornarei envergonhado para minha família, mas ao menos serei feliz")
        escrever_mensagem("Sandubinha começa a se enrijecer como pedra...")
        escrever_mensagem("Glozium: Você me derrotou, mas suguei sua energia-vital, você irá se transformar em minha estátua da entrada da torre hahaha")
        escrever_mensagem("Sandubinha - maldito!... Eu... nunc... ir... ")
        escrever_mensagem("Sandubinha se transforma em uma estátua de pedra, eternamente guardando a entrada da torre.")
        escrever_mensagem("O herói derrotou Glozium ao custo de sua alma, o mundo seguirá normalmente por mais 1 ano...")
        escrever_mensagem("Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...") 
        tela_inicial()

    elif vitoria == 1:
        escrever_mensagem("Glozium: Finalmente! um herói bosta que apenas aumentou meus poderes")
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!")
        escrever_mensagem("Pressione Enter para voltar ao menu...")
        tela_inicial()
    else:
        return
      
def menu_fases(sandu):
    while True:
        TELA.fill((30, 30, 30))
        texto = "Escolha uma fase:\n1 - Floresta do Atendimentus\n2 - Cavernas de Faturamentus\n3 - Vila da Transmissão\n4 - Torre de Contas a Receber\n5 - Glozium\n6 - Voltar ao menu"
        if len(sandu._itens) == 5 and "Espada ZG" not in sandu._itens:
            texto += "\n\n7 - Confecionar a Espada ZG!"
        desenhar_texto(texto, 100)
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
                    vila_da_trasmissao(sandu)
                elif event.key == pygame.K_4:
                    torre_de_contas_a_receber(sandu)
                elif event.key == pygame.K_5:
                    pass
                elif event.key == pygame.K_6:
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