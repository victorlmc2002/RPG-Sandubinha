
class Sandubinha:
    
    def __init__(self):
        self._vida_max = 5
        self._vida_atual = self._vida_max
        self._items = []

    def ganhar_item(self, item):
        from historia import escrever_mensagem, desenhar_texto
        self._items.append(item)
        escrever_mensagem(f"{item} adicionado ao inventário!")
    
    def receber_dano(self, dano):
        from historia import escrever_mensagem, desenhar_texto
        self._vida_atual -= dano
        if self._vida_atual < 0:
            self._vida_atual = 0
        escrever_mensagem(f"Sandubinha não consegiu se defender do ataque e perdeu {dano} de vida! E agora tem {self._vida_atual} PV!")

    def curar(self, cura):
        from historia import escrever_mensagem, desenhar_texto
        self._vida_atual += cura
        if self._vida_atual > self._vida_max:
            self._vida_atual = self._vida_max
        escrever_mensagem(f"Sandubinha curou {cura} PV! E agora tem {self._vida_atual} PV!")

    def aumentar_vida_max(self, aumento):
        from historia import escrever_mensagem, desenhar_texto
        self._vida_max += aumento
        self._vida_atual = self._vida_max
        escrever_mensagem(f"Vida máxima aumentada para {self._vida_max} PV!")

    def usar_item(self, item):
        print(f"Usando item: {item}")
