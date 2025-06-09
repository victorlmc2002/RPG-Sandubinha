import random
import time
from interface import *

def batalha(sandubinha, nome_inimigo, vida_inimigo, numeros_por_rodada):
    escrever_mensagem(f"Início da batalha contra {nome_inimigo}!")
    inimigo_vida = vida_inimigo

    # Sorteio dos números secretos (fixos durante a batalha)
    secreto_sandu = random.randint(1, sandubinha._vida_max)
    secreto_inimigo = random.randint(1, vida_inimigo)
    escrever_mensagem(f"O número secreto do Sandubinha: {secreto_sandu}")
    rodada = 1

    #Loop da batalha
    while sandubinha._vida_atual > 0 and inimigo_vida > 0:
        desenhar_texto(f"\n                                                          Rodada {rodada}")
        time.sleep(2)

        #Variáveis
        qtd_numeros = 1
        acertos = 0
        erros = 0
        atordoado = False
        voando = False

        escolha_item(sandubinha)

        #Regula a quantidade números sorteados com base nos itens equipados
        for i in sandubinha._itens:
            if i == "Guia de Atendimento" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros = 2
            elif i == "Faturamentus" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros = 4
            elif i == "Estilingue Magico" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros = int(vida_inimigo / 2)
                atordoado = True
            elif i == "Azah Transmissão" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros += 10
            elif i == "Colar da Estátua Sagrada" and sandubinha._itens_ativos[sandubinha._itens.index(i)] == "Ativado":
                qtd_numeros += 10

        #Turno do Sandubinha    
        escrever_mensagem(f"Turno do Sandubinha")
    
        escrever_mensagem(f"Sorteando {qtd_numeros} número(s)...")

        #Cálculo da quantidade de acertos
        for i in range(qtd_numeros):
            numero = random.randint(1, vida_inimigo)
            escrever_mensagem(f"Número sorteado: {numero}")
            if numero == secreto_inimigo:
                acertos += 1

        #Cálculo do dano ao inimigo
        if "Azah Transmissão" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Azah Transmissão")] == "Ativado":
                dano = acertos
            if dano == 0:
                ultimo = numero
        else:
            dano = acertos * secreto_inimigo
            inimigo_vida -= dano
        if dano > 0: 
            if "Estilingue Magico" in sandubinha._itens:
                if sandubinha._itens_ativos[sandubinha._itens.index("Estilingue Magico")] == "Ativado" and acertos <= 0:
                    escrever_mensagem("O Estilingue Mágico acerta e atordoa o inimigo!")
            escrever_mensagem(f"{nome_inimigo} sofreu {dano} de dano. Vida restante: {max(0, inimigo_vida)}")
        else:
            escrever_mensagem(f"Nenhum acerto! {nome_inimigo} não sofreu dano.")

        #Consequência do Faturamentus
        bonus_dano = False
        if "Faturamentus" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Faturamentus")] == "Ativado" and acertos <= 0:
                bonus_dano = True
        #Consequência do Estilingue Mágico
        if "Estilingue Magico" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Estilingue Magico")] == "Ativado" and acertos <= 0:
                if erros >= 3:
                    escrever_mensagem("O Estilingue Mágico não conseguiu acertar o inimigo 3 vezes! E Sandubinha perdeu 1 de pv!")
                    sandubinha.receber_dano(1)
        # Consequência do Colar da Estátua Sagrada
        if "Colar da Estátua Sagrada" in sandubinha._itens:
            if sandubinha._itens_ativos[sandubinha._itens.index("Colar da Estátua Sagrada")] == "Ativado":
                sandubinha.receber_dano(3)
        
        #Condição de derrota
        if sandubinha._vida_atual <= 0:
            escrever_mensagem("Sandubinha foi derrotado...")
            return False
        #Condição vitória
        if inimigo_vida <= 0:
            break

        time.sleep(1)

        # Turno do inimigo
        escrever_mensagem(f"Turno do {nome_inimigo}")
        inimigo_numeros = numeros_por_rodada
        acertos = 0

        #Verifica se inimigo está atordoado pelo Estilingue Mágico
        if atordoado:
            escrever_mensagem("O inimigo está atordoado")

        else:
            #Cácula os acertos do inimigo
            for i in range(inimigo_numeros):
                numero = random.randint(1, sandubinha._vida_max)
                escrever_mensagem(f"O inimigo sorteiou o número: {numero}")
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
            sandubinha.receber_dano(dano)
        else:
            escrever_mensagem("Sandubinha esquivou dos ataques do inimigo!")
        
        rodada += 1
        time.sleep(1)  

    escrever_mensagem("Fim da batalha!")
    if sandubinha._vida_atual <= 0:
        escrever_mensagem("Sandubinha foi derrotado...")
        return False
    else:
        escrever_mensagem(f"{nome_inimigo} foi vencido!")
        sandubinha.aumentar_vida_max(2)
        return True
    
def escolha_item(sandubinha):
    if len(sandubinha._itens) <= 0:
        return
    
    while True:
        msg = "Você deseja alterar seu equipamento? Atualmente você " \
        f"possui os \nseguintes itens: "
        for i in range(len(sandubinha._itens)):
            msg += "\n" + str(i+1) + " - " + sandubinha._itens[i] + " - " + str(sandubinha._itens_ativos[i])
        msg += "\n Aperte Enter para voltar"

        desenhar_texto(msg)
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