# -*- coding: utf-8 -*-
class Jogo(object):

    PONTOS = {
        0: 0, 
        1: 15, 
        2: 30, 
        3: 40, 
        4: 'd', 
        5: 'a', 
        6: 'w'
    }

    def __init__(self):
        self.p1 = 0
        self.p2 = 1

        self.pontos = [0, 0]
        self.andamento = True

    def pontua(self, jogador):
        


        if self.pontos[jogador] > 40:
            if 40 not in self.pontos:

                self.status = Jogo.FIM

