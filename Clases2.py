# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:58:35 2020

@author: CASA
"""
import random
import pyxel

class App:
    WIDTH = 256
    HEIGHT = 256
    SEPERACION_MARCADOR = 3
    SEPERACION_PLATAFORMAS = 2
    
    def __init__(self):
        # Se da valor al ancho y alto del escenario 
        pyxel.init(App.WIDTH, App.HEIGHT)
        # Se cargan los recursos gráficos para el juego
        pyxel.load('Assets/Interfaz.pyxres')
        # Se inician los métodos 'upadte' y 'draw'
        
        numPlataformas = 7
        self.plataformas = self.__crearPlataformas(numPlataformas)
        self.marcador = Marcador()
        self.cuadrado = Cuadrado()
        
        pyxel.run(self.update, self.draw)
        
    
    # Método update, se encargará de la parte 'lógica' del juego
    #def update(self):
    def update(self):
        self.plataformas[0][0].update()
        self.cuadrado.update()

    # Método draw, se encargará de la parte gráfica del juego
    def draw(self):
        pyxel.cls(0)
        
        for plataforma in self.plataformas:
            for bloque in plataforma:
                bloque.draw()
        self.marcador.draw()
        self.cuadrado.draw()
        
        
        
        
    def __crearPlataformas(self, numPlataformas):
        """Mediante este método el juego crea y sitúa las plataformas, siguiendo
        este orden lógico:
        Plataformas[Plataforma[Bloque1(x,y), Bloque2(x,y), ...]]"""
        plataformas = list()
        
        # Se crearan tantas plataformas como indique el parámetro.
        # El primer for se encarga de añadir las plataformas ya creadas a la
        # lista, mientras que el segundo se encarga de crear las plataformas.
        # Crear una plataforma signfica crear posiciones siguiendo las
        # restricciones físicas para el correcto funcionamiento
        for vuelta in range(numPlataformas):
            plataforma = list()
            numBloques = random.randint(5, 10)

            # Se genera la posición del extremo izquierdo de la plataforma
            # de tal forma que el extremo derecho no se salga del tablero
            pos_x = random.randint(0, App.WIDTH - Bloque.WIDTH * numBloques)
            # Además de una posición que este dentro del tablero y respete
            # la casilla de salida y el espacio para los Lemmings, dejando 3
            # bloques libres por arriba. Las plataformas se generaran alternando
            # entre filas, siendo la primera en la que se generará una plataforma
            # la tercera fila
            pos_y = (App.SEPERACION_MARCADOR * Bloque.HEIGHT + vuelta * 
                     (Bloque.HEIGHT * App.SEPERACION_PLATAFORMAS))
                
            # En este momento el programa ya ha generado una posición valida
            # Se generarán numBloques bloques 'pegados', es decir con una
            # diferencia de 16, en el eje x, entre ambos extremos izquierdos
            # La pos_y será una constante para todos los bloques dentro de una
            # plataforma
            for bloque in range(numBloques):
                b = Bloque(pos_x + Bloque.WIDTH * bloque, pos_y)
                plataforma.append(b)
            
            # Por último se añade la plataforma a la lista plataformas
            plataformas.append(plataforma)
            
        return plataformas

class Marcador:
    def __init__(self):
        self.nivel = 0
        self.salvados = 0
        self.muertos = 0
        self.vivos = 0
        self.escaleras = 0
        self.paraguas = 0
        self.bloqueadores = 0
        self.cuadrado = Cuadrado()
    def update(self):
        self.nivel = self.nivel
        self.salvados = self.salvados
        self.muertos = self.muertos
        self.vivos = self.vivos
        self.escaleras = self.escaleras
        self.paraguas = self.paraguas
        self.bloqueadores = self.bloqueadores
        self.cuadrado.x = self.cuadrado.x
        self.cuadrado.y = self.cuadrado.y
    def draw(self):
        pyxel.text(4, 4, "Nivel: " + str(self.nivel), 7)
        pyxel.text(40, 4, "Vivos: " + str(self.vivos), 7)
        pyxel.text(80, 4, "Muertos: " + str(self.muertos), 7)
        pyxel.text(130, 4, "Salvados: " + str(self.salvados), 7)
        pyxel.text(185, 4, "Escaleras: " + str(self.escaleras), 7)
        pyxel.text(185, 10, "Paraguas: " + str(self.paraguas), 7)
        pyxel.text(185, 16, "Bloqueadores: " + str(self.bloqueadores), 7)
        pyxel.text(185, 24, "X: " + str(self.cuadrado.x), 7)
        pyxel.text(185, 30, "Y: " + str(self.cuadrado.y), 7)
        
class Cuadrado:
    def __init__(self):
        self.__width = 16
        self.__height = 16
        self.x = 0
        self.y = 32
    def update(self):
        self.__movimiento()
        
    def draw(self):
        pyxel.blt(self.x, self.y, 1, 48, 16, self.__width, self.__height, 0)
    
    def __movimiento(self):
        self.__andando = False
        
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - self.__width, 0)

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + self.__width, pyxel.width - self.__width)
            
        if pyxel.btn(pyxel.KEY_UP):
            self.y = max(self.y - self.__height, 32)
        
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = min(self.y + self.__height, pyxel.height - self.__height)
    
        
class Bloque:
    WIDTH = 16
    HEIGHT = 16
    
    def __init__(self, x, y):
        # Los únicos atributos de un bloque serán su posición respecto al eje x
        # e y
        self.x = x
        self.y = y
        
    def update(self):
        self.x = self.x
    def draw(self):
        pyxel.blt(self.x, self.y, 1, 80, 64, Bloque.WIDTH, Bloque.HEIGHT, 0)


        
App()
