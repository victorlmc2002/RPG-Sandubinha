import random
import time
from interface import *

def batalha(sandubinha, nome_inimigo, vida_inimigo, numeros_por_rodada, img):
    desenhar_texto(f"Início da batalha contra {nome_inimigo}!",LARGURA/2 - LARGURA/6,  fundo=img)
    time.sleep(2)
    inimigo_vida = vida_inimigo

    # Sorteio dos números secretos
    secreto_sandu = random.randint(1, sandubinha._vida_max)
    secreto_inimigo = random.randint(1, vida_inimigo)
    escrever_mensagem(f"O número secreto do Sandubinha: {secreto_sandu}", fundo=img)
    rodada = 1

    #Loop da batalha
    while sandubinha._vida_atual > 0 and inimigo_vida > 0:
        desenhar_texto(f"\nRodada {rodada}", LARGURA/2 - LARGURA/10, fundo=img)
        time.sleep(2)

        #Variáveis
        qtd_numeros = 1
        acertos = 0
        erros = 0
        atordoado = False
        voando = False

        if escolha_item(sandubinha, img) == False:
            escrever_mensagem("Sandubinha decide fazer uma 'retirada estratégica'...", fundo=img)
            return 2
        
        #Regula a quantidade números sorteados com base nos itens equipados
        for i in sandubinha._itens:
            if i == "Guia de Atendimento" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros = 2
            elif i == "Faturamentus" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros = 4
            elif i == "Estilingue Mágico" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros = int(vida_inimigo / 2)
                atordoado = True
            elif i == "Azah Transmissão" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros += 10
            elif i == "Colar da Estátua Sagrada" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros += 10
            elif i == "Espada ZG" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                escrever_mensagem("A Espada ZG brilha intensamente, Sandubinha está pronto para a batalha!", fundo=img)
                qtd_numeros = 40

        #Turno do Sandubinha    
        escrever_mensagem(f"Turno do Sandubinha", fundo=img)
    
        escrever_mensagem(f"Sorteando {qtd_numeros} número(s)...", fundo=img)

        #Cálculo da quantidade de acertos
        if nome_inimigo == "Dragão da Transmissão" and sandubinha._itens_ativos[sandubinha._itens.index("Estilingue Mágico")] != "Ativado":
            if not voando:
                escrever_mensagem("Sandubinha se prepara para atacar, mas o Dragão levanta voo e desvia dos ataques", fundo=img)
            if voando:
                escrever_mensagem("Sua espada não consegue alcançar o Dragão", fundo=img)
            escrever_mensagem("Sandubinha percebe o Estilingue que recebeu dos moradores...", fundo=img)
        else:
            for i in range(qtd_numeros):
                numero = random.randint(1, vida_inimigo)
                if qtd_numeros < 20:
                    escrever_mensagem(f"Número sorteado: {numero}", fundo=img)
                if numero == secreto_inimigo:
                    acertos += 1
            if qtd_numeros > 20:
                escrever_mensagem(f"Sandubinha sorteou {qtd_numeros} números, e acertou {acertos} vezes!", fundo=img)

        #Cálculo do dano ao inimigo
        if "Azah Transmissão" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Azah Transmissão")] == "Ativado":
                dano = acertos
            if dano == 0:
                ultimo = numero
            else:
                inimigo_vida -= dano
        else:
            dano = acertos * secreto_inimigo
            inimigo_vida -= dano
        if dano > 0: 
            if "Estilingue Mágico" in sandubinha._itens:
                if sandubinha._itens_ativos[sandubinha._itens.index("Estilingue Mágico")] == "Ativado" and acertos <= 0:
                    escrever_mensagem("O Estilingue Mágico acerta e atordoa o inimigo!", fundo=img)
                    if voando:
                        escrever_mensagem("O Dragão despenca ao chão", fundo=img)
            escrever_mensagem(f"{nome_inimigo} sofreu {dano} de dano. Vida restante: {max(0, inimigo_vida)}", fundo=img)
        else:
            escrever_mensagem(f"Nenhum acerto! {nome_inimigo} não sofreu dano.", fundo=img)

        #Consequência do Faturamentus
        bonus_dano = False
        if "Faturamentus" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Faturamentus")] == "Ativado" and acertos <= 0:
                bonus_dano = True
        #Consequência do Estilingue Mágico
        if "Estilingue Mágico" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Estilingue Mágico")] == "Ativado" and acertos <= 0:
                if erros >= 3:
                    escrever_mensagem("O Estilingue Mágico não conseguiu acertar o inimigo 3 vezes! E Sandubinha perdeu 1 de pv!", fundo=img)
                    sandubinha.receber_dano(1)
        # Consequência do Colar da Estátua Sagrada
        if "Colar da Estátua Sagrada" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Colar da Estátua Sagrada")] == "Ativado":
                sandubinha.receber_dano(3)
        
        #Condição de derrota
        if sandubinha._vida_atual <= 0:
            break
        #Condição vitória
        if inimigo_vida <= 0:
            break

        time.sleep(1)

        #Turno do inimigo
        escrever_mensagem(f"Turno do {nome_inimigo}", fundo=img)
        inimigo_numeros = numeros_por_rodada
        acertos = 0

        #Verifica se inimigo está atordoado pelo Estilingue Mágico
        if atordoado:
            escrever_mensagem("O inimigo está atordoado", fundo=img)

        else:
            #Cácula os acertos do inimigo
            for i in range(inimigo_numeros):
                numero = random.randint(1, sandubinha._vida_max)
                escrever_mensagem(f"O inimigo sorteiou o número: {numero}", fundo=img)
                if numero == secreto_sandu:
                    acertos += 1

        #Cácula o dano
        if "Azah Transmissão" in sandubinha._itens and acertos > 0:
            if sandubinha._itens_ativos[sandubinha._itens.index("Azah Transmissão")] == "Ativado":
                dano = sandubinha._vida_atual - ultimo
        else:
            dano = acertos * secreto_sandu
        if bonus_dano and dano > 0:
            dano += 2
        if dano > 0:
            sandubinha.receber_dano(dano, fundo=img)
        else:
            escrever_mensagem("Sandubinha esquivou dos ataques do inimigo!", fundo=img)
        
        rodada += 1
        time.sleep(1)  

    #Fim da batalha
    escrever_mensagem("Fim da batalha!", fundo=img)
    if sandubinha._vida_atual <= 0:
        escrever_mensagem("Sandubinha foi derrotado...", fundo=img)
        return 1
    else:
        escrever_mensagem(f"{nome_inimigo} foi vencido!", fundo=img)
        sandubinha.aumentar_vida_max(2, fundo=img)
        return 0
    
def escolha_item(sandubinha, img):

    while True:
        if len(sandubinha._itens) <= 0:
            msg = "Atualmente você não possui equipamentos\n\n"
        else:
            msg = "Você deseja alterar seu equipamento? Atualmente você " \
                f"possui os \nseguintes itens: "
        for i in range(len(sandubinha._itens)):
            msg += "\n" + str(i+1) + " - " + sandubinha._itens[i] + " - " + str(sandubinha._itens_ativos[i])
        msg += "\n\n\n\n\nAperte Enter para voltar\nEsc para fugir da batalha"

        desenhar_texto(msg, fundo=img)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and len(sandubinha._itens) >= 1:
                    if sandubinha._itens_ativos[0] == "Ativado":
                        sandubinha._itens_ativos[0] = "Desativado"
                    else:
                        sandubinha._itens_ativos[0] = "Ativado"
                elif event.key == pygame.K_2 and len(sandubinha._itens) >= 2:
                    if sandubinha._itens_ativos[1] == "Ativado":
                        sandubinha._itens_ativos[1] = "Desativado"
                    else:
                        sandubinha._itens_ativos[1] = "Ativado"
                elif event.key == pygame.K_3 and len(sandubinha._itens) >= 3:
                    if sandubinha._itens_ativos[2] == "Ativado":
                        sandubinha._itens_ativos[2] = "Desativado"
                    else:
                        sandubinha._itens_ativos[2] = "Ativado"
                elif event.key == pygame.K_4 and len(sandubinha._itens) >= 4:
                    if sandubinha._itens_ativos[3] == "Ativado":
                        sandubinha._itens_ativos[3] = "Desativado"
                    else:
                        sandubinha._itens_ativos[3] = "Ativado"
                elif event.key == pygame.K_4 and len(sandubinha._itens) >= 5:
                    if sandubinha._itens_ativos[4] == "Ativado":
                        sandubinha._itens_ativos[4] = "Desativado"
                    else:
                        sandubinha._itens_ativos[4] = "Ativado"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return False