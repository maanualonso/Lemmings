# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:27:12 2020

@author: CASA
"""
import pyxel
import random
from Clases import Interfaz

class Game:
    def __init__(self):
        pyxel.init(256, 256)
        pyxel.load('Assets/Interfaz.pyxres')
        self.contador = 0
        pyxel.run(self.update, self.draw)
        #self.color = random.randint(0, 15)
        self.terreno = Interfaz
        
        
        
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #self.color = random.randint(0, 15)
    def draw(self):
        pyxel.cls(0)
        pyxel.text(4, 4, "Nivel:", 7)
        pyxel.text(50, 4, "Vivos:", 7)
        pyxel.text(90, 4, "Muertos:", 7)
        pyxel.text(140, 4, "Salvados:", 7)
        '''
        for x in self.terreno.matrizTerreno:
            for y in x:
                if y == 1:
                    pyxel.blt(
                        (self.terreno.matrizTerreno.index(x)*16),
                        (self.terreno.matrizTerreno[x].index(y)*16),
                        1,
                        (random.randint(0,15)*16),
                        64,
                        16,
                        8,
                        0
                        )'''
        pyxel.blt(0, 0, 0, 0, 0, 256, 256, 0)
        
Game()