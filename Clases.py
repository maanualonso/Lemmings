# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:24:01 2020

@author: CASA
"""
import random as rnd
import pyxel

class Interfaz():
    
    nivel: int
    salvados: int
    muertos: int
    vivos: int
    escaleras: int
    paraguas: int
    bloqueadores: int
    
    def __init__(self):
        self.matrizTerreno = []
        self.filas = 14
        self.columnas = 16
        
        for fila in range(self.filas):
            auxlst = []
            for columna in range(self.columnas):
                auxlst.append(0)
            self.matrizTerreno.append(auxlst)
    '''
    def rellenarTerreno(self):
        self.plataformas = []
        numeroPlataformas = 7
            
        for _ in range(numeroPlataformas):
            casillas = rnd.randint(5, 10)
                
            plataforma = []
            for _ in range(casillas):
                plataforma.append(1)
                    
            self.plataformas.append(plataforma)
     '''           
    def rellenarTerrenoJuego(self):
        numeroPlataformas = 7
        for i in range(numeroPlataformas):
            tamaño = rnd.randint(5, 10)
            casilla_x = rnd.randint(0,11)
            while casilla_x > 16 - tamaño:
                tamaño = rnd.randint(5, 10)
                casilla_x = rnd.randint(0,11)
            for a in range(tamaño):
                self.matrizTerreno[i*2 + 1][casilla_x + a] = 1
        print(self.matrizTerreno)
            
a = Interfaz()
a = a.rellenarTerrenoJuego()
#print(a)