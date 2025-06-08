import random
import time
from interface import *

def batalha(sandubinha, nome_inimigo, vida_inimigo, numeros_por_rodada, item_em_uso=None):
    escrever_mensagem(f"Início da batalha contra {nome_inimigo}!")
    inimigo_vida = vida_inimigo

    # Sorteio dos números secretos (fixos durante a batalha)
    secreto_sandu = random.randint(1, sandubinha._vida_max)
    secreto_inimigo = random.randint(1, vida_inimigo)
    escrever_mensagem(f"O número secreto do Sandubinha: {secreto_sandu}")
    rodada = 1

    while sandubinha._vida_atual > 0 and inimigo_vida > 0:
        desenhar_texto(f"\n                                                          Rodada {rodada}")
        time.sleep(2)
        escolha_item(sandubinha)
        escrever_mensagem(f"Turno do Sandubinha")
        #Turno do Sandubinha
    
        qtd_numeros = 1

        #Efeitos de itens
        if item_em_uso == "Guia de Atendimento":
            qtd_numeros = 2
        elif item_em_uso == "Faturamentus":
            qtd_numeros = 4
        #Outros itens podem ser adicionados aqui futuramente

        acertos = 0
        escrever_mensagem(f"Turno do Sandubinha")
        escrever_mensagem(f"Sorteando {qtd_numeros} número(s)...")
        for i in range(qtd_numeros):
            numero = secreto_inimigo #random.randint(1, vida_inimigo)
            escrever_mensagem(f"Número sorteado: {numero}")
            if numero == secreto_inimigo:
                acertos += 1

        dano = acertos * secreto_inimigo
        inimigo_vida -= dano
        if dano > 0: 
            escrever_mensagem(f"{nome_inimigo} sofreu {dano} de dano. Vida restante: {max(0, inimigo_vida)}")
        else:
            escrever_mensagem(f" Nenhum acerto! {nome_inimigo} não sofreu dano.")

        # Consequência do Faturamentus
        bonus_dano = False
        if item_em_uso == "Faturamentus" and acertos > 0:
            bonus_dano = True

        if inimigo_vida <= 0:
            break

        time.sleep(1)

        # Turno do inimigo
        escrever_mensagem(f"Turno do {nome_inimigo}")
        inimigo_numeros = numeros_por_rodada
        acertos = 0
        for i in range(inimigo_numeros):
            numero = random.randint(1, sandubinha._vida_max)
            escrever_mensagem(f"O inimigo sorteiou o número: {numero}")
            if numero == secreto_sandu:
                acertos += 1

        dano = acertos * secreto_sandu
        if bonus_dano:
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
    msg = "Você deseja alterar seu equipamento? Atualmente você " \
    f"possui os \nseguintes itens: "
    for i in range(len(sandubinha._itens)):
        msg += "\n" + str(i+1) + sandubinha._itens[i]
    while True:
        desenhar_texto(msg)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and len(sandubinha._itens) >= 1:
                    print(sandubinha._itens[0])
                    if sandubinha._itens_ativos[0] == True:
                        sandubinha._itens_ativos[0] = False
                    else:
                        sandubinha._itens_ativos[0] = True
                    return
                elif event.key == pygame.K_2 and len(sandubinha._itens) >= 2:
                    if sandubinha._itens_ativos[1] == True:
                        sandubinha._itens_ativos[1] = False
                    else:
                        sandubinha._itens_ativos[1] = True
                    return
                elif event.key == pygame.K_3 and len(sandubinha._itens) >= 3:
                    if sandubinha._itens_ativos[2] == True:
                        sandubinha._itens_ativos[2] = False
                    else:
                        sandubinha._itens_ativos[2] = True
                    return
                elif event.key == pygame.K_4 and len(sandubinha._itens) >= 4:
                    if sandubinha._itens_ativos[3] == True:
                        sandubinha._itens_ativos[3] = False
                    else:
                        sandubinha._itens_ativos[3] = True
                    return