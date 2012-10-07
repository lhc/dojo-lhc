# -*- coding: utf-8 -*-
import unittest
from tenis import *

class TenisGameTestCase(unittest.TestCase):
    def setUp(self):
        self.jogo = Jogo()

    def test_novo_jogo_tem_dois_jogadores(self):
        self.assertTrue(hasattr(self.jogo, 'p1'))
        self.assertTrue(hasattr(self.jogo, 'p2'))

    def test_jogador_tem_zero_ponto(self):
        self.assertEqual(self.jogo.pontos, [0,0])

    def test_jogador1_ganha_primeiro_ponto(self):
        self.jogo.pontua(self.jogo.p1)

        self.assertEqual(self.jogo.pontos, [15, 0])

    def test_jogador2_ganha_primeiro_ponto(self):
        self.jogo.pontua(self.jogo.p2)

        self.assertEqual(self.jogo.pontos, [0, 15])

    def test_jogador1_ganha_segundo_ponto(self):
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.assertEqual(self.jogo.pontos, [30, 0])

    def test_jogador1_ganha_terceiro_ponto(self):
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.assertEqual(self.jogo.pontos, [40, 0])

    def test_comeca_com_jogo_em_andamento(self):
        self.assertTrue(self.jogo.andamento)
        
    def test_fim_do_jogo(self):
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.assertFalse(self.jogo.andamento)

    def test_em_andamento_com_empate(self):
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        
        self.jogo.pontua(self.jogo.p2)
        self.jogo.pontua(self.jogo.p2)
        self.jogo.pontua(self.jogo.p2)
        
        self.jogo.pontua(self.jogo.p1)
        self.assertTrue(self.jogo.andamento)

    def test_em_andamento_desempate(self):
        
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        
        self.jogo.pontua(self.jogo.p2)
        self.jogo.pontua(self.jogo.p2)
        self.jogo.pontua(self.jogo.p2)
        
        self.jogo.pontua(self.jogo.p1)
        self.jogo.pontua(self.jogo.p1)
        self.assertFalse(self.jogo.andamento)


if __name__ == '__main__':
    unittest.main()
