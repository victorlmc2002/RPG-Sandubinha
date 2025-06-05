import random
import time
from personagem import Sandubinha

def batalha(sandubinha, nome_inimigo, vida_inimigo, numeros_por_rodada, item_em_uso=None):
    print(f"\n⚔️  Início da batalha contra {nome_inimigo}!")
    inimigo_vida = vida_inimigo

    # Sorteio dos números secretos (fixos durante a batalha)
    secreto_sandu = random.randint(1, sandubinha._vida_max)
    secreto_inimigo = random.randint(1, vida_inimigo)

    rodada = 1

    while sandubinha._vida_atual > 0 and inimigo_vida > 0:
        print(f"\n--- Rodada {rodada} ---")

        # 🎯 Turno do Sandubinha
        print("\n▶️ Turno do Sandubinha")
        qtd_numeros = 1

        # Efeitos de itens
        if item_em_uso == "Guia de Atendimento":
            qtd_numeros = 2
        elif item_em_uso == "Faturamentus":
            qtd_numeros = 4
        # Outros itens podem ser adicionados aqui futuramente

        acertos = 0
        print(f"🔢 Sorteando {qtd_numeros} número(s)...")
        for i in range(qtd_numeros):
            numero = random.randint(1, vida_inimigo)
            print(f"Número sorteado: {numero}")
            if numero == secreto_inimigo:
                acertos += 1

        dano = acertos * secreto_inimigo
        inimigo_vida -= dano
        if dano > 0: 
            print(f"💥 {nome_inimigo} sofreu {dano} de dano. Vida restante: {max(0, inimigo_vida)}")
        else:
            print(f"❌ Nenhum acerto! {nome_inimigo} não sofreu dano.")

        # Consequência do Faturamentus
        bonus_dano = False
        if item_em_uso == "Faturamentus" and acertos > 0:
            bonus_dano = True

        if inimigo_vida <= 0:
            break

        time.sleep(1)

        # 😈 Turno do inimigo
        print(f"\n▶️ Turno do {nome_inimigo}")
        inimigo_numeros = numeros_por_rodada
        acertos = 0
        for i in range(inimigo_numeros):
            numero = random.randint(1, sandubinha._vida_max)
            print(f"Número sorteado: {numero}")
            if numero == secreto_sandu:
                acertos += 1

        dano = acertos * secreto_sandu
        if bonus_dano:
            dano += 2
        if dano > 0:
            sandubinha.receber_dano(dano)
        else:
            print("Sandubinha esquivou dos ataques do inimigo!")
        
        rodada += 1
        time.sleep(1)

    print("\n🏁 Fim da batalha!")
    if sandubinha._vida_atual <= 0:
        print("☠️  Sandubinha foi derrotado...")
        return False
    else:
        print(f"🎉 {nome_inimigo} foi vencido!")
        sandubinha.aumentar_vida_max(2)
        return True