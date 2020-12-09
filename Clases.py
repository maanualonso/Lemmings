# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:24:01 2020

@author: CASA
"""
import random as rnd


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
        for i in range(len(self.matrizTerreno)):
            print(self.matrizTerreno[i])
            
           

