import random
import time

def batalha(sandubinha, nome_inimigo, vida_inimigo, numeros_por_rodada, item_em_uso=None):
    from historia import escrever_mensagem, desenhar_texto
    escrever_mensagem(f"\n⚔️  Início da batalha contra {nome_inimigo}!")
    inimigo_vida = vida_inimigo

    # Sorteio dos números secretos (fixos durante a batalha)
    secreto_sandu = random.randint(1, sandubinha._vida_max)
    secreto_inimigo = random.randint(1, vida_inimigo)
    escrever_mensagem(f"O número secreto do Sandubinha: {secreto_sandu}")
    rodada = 1

    while sandubinha._vida_atual > 0 and inimigo_vida > 0:
        desenhar_texto(f"\n                                                          Rodada {rodada}")

        #Turno do Sandubinha
    
        qtd_numeros = 1

        #Efeitos de itens
        if item_em_uso == "Guia de Atendimento":
            qtd_numeros = 2
        elif item_em_uso == "Faturamentus":
            qtd_numeros = 4
        #Outros itens podem ser adicionados aqui futuramente

        acertos = 0
        escrever_mensagem(f"▶Turno do Sandubinha")
        escrever_mensagem(f"Sorteando {qtd_numeros} número(s)...")
        for i in range(qtd_numeros):
            numero = random.randint(1, vida_inimigo)
            escrever_mensagem(f"Número sorteado: {numero}")
            if numero == secreto_inimigo:
                acertos += 1

        dano = acertos * secreto_inimigo
        inimigo_vida -= dano
        if dano > 0: 
            escrever_mensagem(f"💥 {nome_inimigo} sofreu {dano} de dano. Vida restante: {max(0, inimigo_vida)}")
        else:
            escrever_mensagem(f"❌ Nenhum acerto! {nome_inimigo} não sofreu dano.")

        # Consequência do Faturamentus
        bonus_dano = False
        if item_em_uso == "Faturamentus" and acertos > 0:
            bonus_dano = True

        if inimigo_vida <= 0:
            break

        time.sleep(1)

        # Turno do inimigo
        escrever_mensagem(f"▶ Turno do {nome_inimigo}")
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

    escrever_mensagem("\n🏁 Fim da batalha!")
    if sandubinha._vida_atual <= 0:
        escrever_mensagem("☠️  Sandubinha foi derrotado...")
        return False
    else:
        escrever_mensagem(f"🎉 {nome_inimigo} foi vencido!")
        sandubinha.aumentar_vida_max(2)
        return True