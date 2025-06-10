from interface import *
class Sandubinha:
    
    def __init__(self):
        self._vida_max = 5
        self._vida_atual = self._vida_max
        self._itens = []
        self._itens_ativos = []

    def ganhar_item(self, item, fundo=None):
        if item in self._itens:
            return
        self._itens.append(item)
        self._itens_ativos.append("Desativado")
        escrever_mensagem(f"{item} adicionado ao inventário!", fundo=fundo)
    
    def receber_dano(self, dano, fundo=None):
        self._vida_atual -= dano
        if self._vida_atual < 0:
            self._vida_atual = 0
        escrever_mensagem(f"Sandubinha não consegiu se defender do ataque e perdeu {dano} de vida! E agora tem {self._vida_atual} PV!", fundo=fundo)

    def aumentar_vida_max(self, aumento, fundo=None):
        self._vida_max += aumento
        self._vida_atual = self._vida_max
        escrever_mensagem(f"Vida máxima aumentada para {self._vida_max} PV!", fundo=fundo)
    
    def espada_zg(self, fundo=None):
        if len(self._itens) == 5:
            self._itens = ["Espada ZG"]
            self._itens_ativos = ["Desativado"]
            escrever_mensagem("A lendária Espada ZG foi confeccionada! Sandubinha agora pode derrotar Glozium de uma vez por todas!", fundo=fundo)
        else:
            return
