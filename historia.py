import pygame
import sys
from personagem import Sandubinha
from batalha import batalha
from interface import *

f1 = pygame.image.load("img/fase1.jpg").convert()
f1 = pygame.transform.scale(f1, (LARGURA, ALTURA))
f2 = pygame.image.load("img/fase2.jpg").convert()
f2 = pygame.transform.scale(f2, (LARGURA, ALTURA))
f3 = pygame.image.load("img/fase3.jpg").convert()
f3 = pygame.transform.scale(f3, (LARGURA, ALTURA))
f4 = pygame.image.load("img/fase4.jpg").convert()
f4 = pygame.transform.scale(f4, (LARGURA, ALTURA))
ff = pygame.image.load("img/fasef.jpg").convert()
ff = pygame.transform.scale(ff, (LARGURA, ALTURA))

mn = pygame.image.load("img/menu.jpg").convert()
mn = pygame.transform.scale(mn, (LARGURA, ALTURA))
mapa = pygame.image.load("img/mapa.png").convert()
mapa = pygame.transform.scale(mapa, (LARGURA, ALTURA))
montanha = pygame.image.load("img/montanha.png").convert()
montanha = pygame.transform.scale(montanha, (LARGURA, ALTURA))
glozium = pygame.image.load("img/Glozium.png").convert()
glozium = pygame.transform.scale(glozium, (LARGURA, ALTURA))
pessoas = pygame.image.load("img/pessoas.png").convert()
pessoas = pygame.transform.scale(pessoas, (LARGURA, ALTURA))
sanduba = pygame.image.load("img/Sandubinha.png").convert()
sanduba = pygame.transform.scale(sanduba, (LARGURA, ALTURA))

#Fase 1: Floresta do Atendimentus
def floresta_do_atendimentus(sandu):
    escrever_mensagem("Floresta do Atendimentus", LARGURA/2 - LARGURA/8, fundo=f1)
    escrever_mensagem("Um lugar encantado,dizem que pessoas doentes ou com almas feridas podem ir a floresta para serem curadas.", fundo=f1)
    escrever_mensagem("Sandubinha percorre a floresta e encontra um monstro tenebroso.", fundo=f1)
    escrever_mensagem("Sandubinha: Então você é meu primeiro desafio nessa floresta encantada?", fundo=f1)
    escrever_mensagem("Processus: Bem-vindo, vejo que você é um dos escolhidos para enfraquecer Glozium, meu nome é Processus ministerii.", fundo=f1)
    escrever_mensagem("Processus: Sou o ser mágico que atende as almas feridas, envio os informativos disso as cavernas de Faturamentus.", fundo=f1)
    escrever_mensagem("Processus: Você não irá lutar comigo, mas sim contra esse ser criado por Glozium chamado Monstrengo.", fundo=f1)
    escrever_mensagem("Seres mágicos do meu tipo não podem ser afetados por Glozium, mas também não podem lutar contra, ele me atrapalha me desconcentrando e provocando erros.", fundo=f1)
    escrever_mensagem("Surge entre as pernas do grande monstro um ser humanoide, da altura de Sandubinha.", fundo=f1)
    escrever_mensagem("Sandubinha: Primeiro, não é enfraquecer, vou dar um fim total em Glozium... Venha monnstro gigante!", fundo=f1)
    desenhar_texto("Pressione Enter para iniciar a batalha...", fundo=f1)

    vitoria = batalha(sandu, "Monstrengo", 3, 1, f1)
    if vitoria == 0:
        escrever_mensagem("Processus: Muito obrigado, tome o artefato 'Guia de Atendimento' e siga para o próximo desafio.", fundo=f1)
        sandu.ganhar_item("Guia de Atendimento", fundo=f1)

        
        return
    elif vitoria == 1:
        escrever_mensagem("Processus: Oh não... o mundo será mais uma vez destruído por Glozium...", fundo=f1)
        escrever_mensagem("O mundo foi destruído por Glozium. Fim de jogo!", fundo=f1)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=f1)
        tela_inicial()
    else:
        return


#Fase 2: Cavernas de Faturamentus
def cavernas_de_faturamentus(sandu):
    escrever_mensagem("Cavernas de Faturamentus", LARGURA/2 - LARGURA/8, fundo=f2)
    escrever_mensagem("Existe sempre um preço a se pagar pela cura do corpo e da alma...", fundo=f2)
    escrever_mensagem("Após a floresta do atendimentus, o preço é calculado pelo tipo de contrato divino.", fundo=f2)
    escrever_mensagem("Percorrendo a caverna segurando uma tocha.", fundo=f2)
    escrever_mensagem("Sandubinha escuta grunhidos e vê fantasmas anotando coisas em pergaminhos.", fundo=f2)
    escrever_mensagem("O cenário é iluminado por minérios misteriosos. Anciões fantasmas anotam diversas coisas em pergaminhos, estão todos muito ocupados para falar algo a Sandubinha", fundo=f2)
    escrever_mensagem("Um monstro em forma de urso surge e diz a Sandubinha:", fundo=f2)
    escrever_mensagem("Urso Sangrento: Finalmente diversão! Vamos lutar heroizinho!", fundo=f2)
    escrever_mensagem("Sandubinha: Criatura desagradável, nem me deu tempo de tomar uma água!", fundo=f2)

    vitoria = batalha(sandu, "Urso Sangrento", 6, 2, f2)
    if vitoria == 0:
        escrever_mensagem("Ancião Faturador: Muito obrigado, mas tô ocupado demais para agradecimentos longos, tome o artefato sagrado e siga em frente.", fundo=f2)
        sandu.ganhar_item("Faturamentus", fundo=f2)
        return
    elif vitoria == 1:
        escrever_mensagem("Ancião Faturador: Herói merda, nem para cumprir o trabalho dele, estamos perdidos!", fundo=f2)
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!", fundo=f2)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=f2)
        tela_inicial()
    else: 
        return

#Fase 3: Vila da Transmissão
def vila_da_transmissao(sandu):
    escrever_mensagem("Vila da Transmissão", LARGURA/2 - LARGURA/8, fundo=f3)
    escrever_mensagem("Uma vila mágica que recebe cobranças vindas das cavernas de Faturamentus. Os moradores entregam as mensagens na Torre", fundo=f3)
    escrever_mensagem("Sandubinha é bem recebido em sua chegada. Ele é convidado para um jantar ritualístico com comidas típicas", fundo=f3)
    escrever_mensagem("Os moradores contam que o monstro a ser enfrentado é um ser que voa. Para atacá-lo, o Sandubinha terá que derrubar o monstro e usar sua espada. Então, dão a ele um item, o Estilingue Mágico", fundo=f3)
    sandu.ganhar_item("Estilingue Mágico", fundo=f3)
    escrever_mensagem("Logo, um monstro em forma de dragão surge voando...", fundo=f3)
    escrever_mensagem("Dragão da transmissão: Você já tem sua arma... já fui guardião dessas terras e transmitia as mensagens à torre. Mas milénios atrás Glozium me tornou seu escravo, sou obrigado a lutar com toda fúria. Livre-me do sofrimento...", fundo=f3)
    escrever_mensagem("Sandubinha: Você também está preso a um destino que não escolheu, vou te libertar!", fundo=f3)
    
    vitoria = batalha(sandu, "Dragão da Transmissão", 12, 3, f3)
    if vitoria == 0:
        escrever_mensagem("Dragão: Muito obrigado, todo herói evitava essa batalha e seguia para a torre, agora sou livre!", fundo=f3)
        escrever_mensagem("Sandubinha: Evitava? E dá para seguir sem lutar? como assim? Sandubinha ganha o artefato Azah Transmissão", fundo=f3)
        sandu.ganhar_item("Azah Transmissão", fundo=f3)
        return
    elif vitoria == 1:
        escrever_mensagem("Dragão - Sinto muito herói, que sua alma seja livre...", fundo=f3)
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!", fundo=f3)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=f3)
        tela_inicial()
    else:
        return
    
#Fase 4: Torre de Contas a Receber
def torre_de_contas_a_receber(sandu):
    escrever_mensagem("Torre de Contas a Receber", LARGURA/2 - LARGURA/8, fundo=f4)
    escrever_mensagem("A terrível torre é onde seres mágicos recebem o pagamento por seu árduo trabalho. Dizem que a ruína perto da torre eram a cidade mais próxima do grito, terra natal dos Analyticaes di Glosium", fundo=f4)
    escrever_mensagem("Sandubinha chega ao primeiro andar da torre. Ele sente uma energia mágica mortífera vindo do topo. Sem dúvidas, Glozium estava lá...", fundo=f4)
    escrever_mensagem("A parede se abre e sai dela o penúltimo monstro a ser enfrentado", fundo=f4)
    escrever_mensagem("Sandubinha: Uma estátua na forma do último herói, por que?", fundo=f4)
    
    vitoria = batalha(sandu, "Estátua do Último Herói", 25, 5, f4)
    if vitoria == 0:
        escrever_mensagem("É assustador olhar para essa estátua despedaçada e ver a forma do último herói", fundo=f4)
        sandu.ganhar_item("Colar da Estátua Sagrada", fundo=f4)
        return
    elif vitoria == 1:
        escrever_mensagem("Estátua do último herói: ...", fundo=f4)
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!", fundo=f4)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=f4)
        tela_inicial()
    else:
        return

#Batalha contra Glozium (final)
def batalha_final(sandu):
    escrever_mensagem("Batalha Final", LARGURA/2 - LARGURA/8, fundo=ff)
    TELA.fill((200, 200, 30))
    if sandu._vida_max < 10:
        while True:
            desenhar_texto("ATENÇÃO\nSandubinha no momento está muito fraco para enfrentar Glozium" \
            "\nVocê deseja voltar ao menu ou continuar?" \
            "\n\n\n\nEnter para voltar ao menu" \
            "\nEsc para continuar", fundo=ff)
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
    if len(sandu._itens) == 5:
        while True:
            desenhar_texto("ATENÇÃO\nSandubinha coletou todos os itens precisos para Espada ZG" \
            "\nVocê deseja voltar e criar a arma ou seguir sem ela?" \
            "\n\n\n\nEnter para voltar e criar a espada" \
            "\nEsc para continuar sem ela", fundo=ff)
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

    escrever_mensagem("Sandubinha sente que no topo da Torre de Contas a Receber reside Glozium, é uma habilidade dos Analyticaes di Glosium", fundo=ff)
    escrever_mensagem("Sandubinha entra na sala do chefe e se depara com a presença arrepiante de Glozium sentado no trono", fundo=ff)
    escrever_mensagem("Glozium: Um rato invadiu meu recinto; talvez sirva de alimento para meus escravos", fundo=ff)
    escrever_mensagem("Sandubinha: Então você é Glozium? Não é mais aterrorizante que as criaturas apodrecidas que encontrei", fundo=ff)
    escrever_mensagem("Glozium: Ha ha ha ha! Que petulante! Chegou a época, mas mandaram um pobre coitado; péssima ideia!", fundo=ff)
    escrever_mensagem("Sandubinha: Vou te destruir, Glozium, e garantir sua aniquilação total e permanente!", fundo=ff)
    escrever_mensagem("Glozium: E o que um garoto com cabeça de hambúrguer pode fazer contra um monstro milenar, que presenciou eventos tão singulares, que caminhou sobre a superfície de vulcões e subjugou a humanidade?", fundo=ff)
    escrever_mensagem("Sandubinha lança sua espada girando no ar que fere o monstro e retorna a sua mão", fundo=ff)
    escrever_mensagem("Sandubinha: Não subestime alguém com cabeça de hambúrguer, sou um descendente dos Analyticaes di Glosium. Te procurei em cada canto do inferno para reduzir você a zero", fundo=ff)
    escrever_mensagem("Glozium: Interessante, aceito seu pedido de batalha", fundo=ff)

    vitoria = batalha(sandu, "Glozium", 100, 10, ff)
    if vitoria == 0 and "Espada ZG" in sandu._itens:
        escrever_mensagem("Sandubinha: Finalmente, Glozium está eliminado por completo, irei retornar a minha família", fundo=ff)
        escrever_mensagem("O herói derrotou Glozium, o mundo agora poderá voltar a seus tempos de alegria. Muito obrigado, herói!", fundo=ff)
        escrever_mensagem("Fim de jogo!", fundo=ff)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=ff)
        tela_inicial()

    elif vitoria == 0 and "Espada ZG" not in sandu._itens:
        escrever_mensagem("Glozium: Você me derrotou com armas tão simples, impressionante, mas irei retornar no ano seguinte", fundo=ff)
        escrever_mensagem("Sandubinha - ...retornarei envergonhado para minha família, mas ao menos serei feliz", fundo=ff)
        escrever_mensagem("Sandubinha começa a se enrijecer como pedra...", fundo=ff)
        escrever_mensagem("Glozium: Você me derrotou, mas suguei sua energia-vital, você irá se transformar em minha estátua da entrada da torre hahaha", fundo=ff)
        escrever_mensagem("Sandubinha - maldito!... Eu... nunc... ir... ", fundo=ff)
        escrever_mensagem("Sandubinha se transforma em uma estátua de pedra, eternamente guardando a entrada da torre.", fundo=ff)
        escrever_mensagem("O herói derrotou Glozium ao custo de sua alma, o mundo seguirá normalmente por mais 1 ano...", fundo=ff)
        escrever_mensagem("Fim de jogo!", fundo=ff)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=ff) 
        tela_inicial()

    elif vitoria == 1:
        escrever_mensagem("Glozium: Finalmente! um herói bosta que apenas aumentou meus poderes", fundo=ff)
        escrever_mensagem("O mundo foi destruído por Glozium, uma fatalidade terrível...Fim de jogo!", fundo=ff)
        escrever_mensagem("Pressione Enter para voltar ao menu...", fundo=ff)
        tela_inicial()
    else:
        return
      
def verificar_opcao_espada_zg(sandu):
    if len(sandu._itens) == 5 and "Espada ZG" not in sandu._itens:
        return "\n\n7 - Confecionar a Espada ZG!"
    return ""

def menu_fases(sandu):
    while True:
        TELA.blit(mapa, (0, 0))
        texto = "Escolha uma fase:\n1 - Floresta do Atendimentus\n2 - Cavernas de Faturamentus\n3 - Vila da Transmissão\n4 - Torre de Contas a Receber\n5 - Glozium\n6 - Voltar ao menu"
        texto += verificar_opcao_espada_zg(sandu)
        desenhar_texto(texto, 300, fundo=mapa)
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
                    vila_da_transmissao(sandu)
                elif event.key == pygame.K_4:
                    torre_de_contas_a_receber(sandu)
                elif event.key == pygame.K_5:
                    batalha_final(sandu)
                elif event.key == pygame.K_6:
                    if alerta():
                        tela_inicial()
                    else:
                        continue
                elif event.key == pygame.K_7:
                    sandu.espada_zg(mn)
def alerta():
    desenhar_texto("            Atenção!\n\n Se você voltar ao menu," \
    " perderá o progresso atual." \
    "\n\nPressione Enter para continuar..." \
    "\n\nPressione qualquer outra tecla para continuar...", fundo=mn)

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
        desenhar_texto("A Jornada Do Sandubinha\n\n1 - Começar a aventura\n2 - Introdução\n3 - Sair", 300, fundo=mn)
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
    escrever_mensagem("Vindo de onde os olhos não conseguiam alcançar, com um som alto, passando pelas montanhas e vales, pelos rios e florestas. Todos no mundo puderam ouvir uma voz que parecia um estrondo, que dizia:", fundo=montanha)
    escrever_mensagem("Contemplem seu novo mestre, Glozium...Demonstrativus potentiaaam!!", fundo=glozium)
    escrever_mensagem("O terror recaiu sobre as pessoas e o mundo foi tomado por uma neblina que provocou todo tipo de mazela. Alguns morreram, outros tornaram-se monstros, animais sofreram mutações.", fundo=pessoas)
    escrever_mensagem("Mas após a dissolução dessa terrível onda mortífera, era possível ver em meio a neblina o que pareciam estátuas em pé, onde o som foi mais intenso...", fundo=pessoas)
    escrever_mensagem("Agora, m um mundo ameaçado por forças sombrias, o aprendiz de guerreiro Sandubinha é convocado pela antiga guilda de Zerum Glozium para impedir que a escuridão se espalhe pela província de hospitalis.", fundo=sanduba)
    escrever_mensagem("Para isso, ele deverá explorar terras perigosas, resolver enigmas mágicos, fazer alianças, enfrentar criaturas e tomar decisões que definirão o destino do reino.", fundo=sanduba)
    desenhar_texto("Aperte Enter para voltar ao Menu...", fundo=sanduba)
    esperar_enter()

def iniciar_jogo():
    sandu = Sandubinha()
    escrever_mensagem("Você acorda com uma sensação estranha... É hora de iniciar sua missão épica!", fundo=mn)
    desenhar_texto("Pressione Enter para continuar...", fundo=mn)
    esperar_enter()
    menu_fases(sandu)