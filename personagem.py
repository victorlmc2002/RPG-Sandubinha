class Sandubinha:
    def __init__(self):
        self._vida_max = 5
        self._vida_atual = self._vida_max
        self._items = []

    def ganhar_item(self, item):
        self._items.append(item)
        print(f"{item} adicionado ao inventário!")
    
    def receber_dano(self, dano):
        self._vida_atual -= dano
        if self._vida_atual < 0:
            self._vida_atual = 0
        print(f"Sandubinha perdeu {dano} de vida! E agora tem {self._vida_atual} PV!")

    def curar(self, cura):
        self._vida_atual += cura
        if self._vida_atual > self._vida_max:
            self._vida_atual = self._vida_max
        print(f"Sandubinha curou {cura} PV! E agora tem {self._vida_atual} PV!")

    def aumentar_vida_max(self, aumento):
        self._vida_max += aumento
        self._vida_atual = self._vida_max
        print(f"Vida máxima aumentada para {self._vida_max} PV!")

    def usar_item(self, item):
        print(f"Usando item: {item}")
