import pygame as pg
import sys
import time
from os import path
from os import system





class main(object):
    def __init__(self):
        self.screen = pg.display.set_mode((860,658))
        self.loadData()
        pg.init()
        pg.display.set_caption("Game")
        self.firstMakeMatrix()


        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)

            self.draw()








    def draw(self):
        self.screen.fill((0, 0, 0))
        pg.draw.rect(self.screen, (112, 41, 0), pg.Rect(0, 0, 658, 658))

        colorid = 0
        for i in range(8):
            colorid += 1
            for j in range(8):
                if colorid % 2 == 0:
                    color = (90, 90, 90)
                else:
                    color = (220, 220, 220)
                colorid += 1
                pg.draw.rect(self.screen, (color), pg.Rect(i * 82 + 2, j * 82 + 2, 80, 80))

                # self.matrix[0][3].K1
                self.screen.blit(self.figureK, (1 * 82 + 2, 0 * 82 + 2))






        pg.display.flip()



    def firstMakeMatrix(self):
        self.matrix = []
        fieldID = 0

        for i in range(8):
            self.matrix.append([])
            for j in range(8):
                self.matrix[i].append(field(i,j,fieldID,self))
                fieldID += 1


    def loadData(self):
        img_dir = path.join(path.dirname(__file__), "data/")
        self.figureW = pg.image.load(img_dir + "w.png")
        self.figureWC = pg.image.load(img_dir + "wc.png")
        self.figureP = pg.image.load(img_dir + "p.png")
        self.figurePC = pg.image.load(img_dir + "pc.png")
        self.figureG = pg.image.load(img_dir + "g.png")
        self.figureGC = pg.image.load(img_dir + "gc.png")
        self.figureK = pg.image.load(img_dir + "k.png")
        self.figureKC = pg.image.load(img_dir + "kc.png")
        self.figureS = pg.image.load(img_dir + "s.png")
        self.figureSC = pg.image.load(img_dir + "sc.png")
        self.figureH = pg.image.load(img_dir + "h.png")
        self.figureHC = pg.image.load(img_dir + "hc.png")



class field(object):
    def __init__(self, x, y, typ, main):
        self.posx = x
        self.posy = y
        self.typ = typ
        self.main = main

        i=self.posy


        if self.typ == 0: self.typ = "W1"
        if self.typ == 1: self.typ = "S1"
        if self.typ == 2: self.typ = "G1"
        if self.typ == 3: self.typ = "K1"
        if self.typ == 4: self.typ = "H1"
        if self.typ == 5: self.typ = "G2"
        if self.typ == 6: self.typ = "S2"
        if self.typ == 7: self.typ = "W2"
        if self.typ == 8: self.typ = "P1"
        if self.typ == 9: self.typ = "P2"
        if self.typ == 10: self.typ = "P3"
        if self.typ == 11: self.typ = "P4"
        if self.typ == 12: self.typ = "P5"
        if self.typ == 13: self.typ = "P6"
        if self.typ == 14: self.typ = "P7"
        if self.typ == 15: self.typ = "P8"
        for i in range(32):
            if self.typ == i+16: self.typ = "free"
        if self.typ == 48: self.typ = "P1"
        if self.typ == 49: self.typ = "P2"
        if self.typ == 50: self.typ = "P2"
        if self.typ == 51: self.typ = "P3"
        if self.typ == 52: self.typ = "P4"
        if self.typ == 53: self.typ = "P5"
        if self.typ == 54: self.typ = "P6"
        if self.typ == 55: self.typ = "P7"
        if self.typ == 56: self.typ = "WC1"
        if self.typ == 57: self.typ = "SC1"
        if self.typ == 58: self.typ = "GC1"
        if self.typ == 59: self.typ = "KC1"
        if self.typ == 60: self.typ = "HC1"
        if self.typ == 61: self.typ = "GC2"
        if self.typ == 62: self.typ = "SC2"
        if self.typ == 63: self.typ = "WC2"



        if self.typ == "P1": self.P1 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P2": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P3": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P4": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P5": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P6": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P7": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "P8": self.P2 = self.main.screen.blit(self.main.figureP, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC1": self.PC1 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC2": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC3": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC4": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC5": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC6": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC7": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "PC8": self.PC2 = self.main.screen.blit(self.main.figurePC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "K1": self.K1 = self.main.screen.blit(self.main.figureK, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "KC1": self.KC1 = self.main.screen.blit(self.main.figureKC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "H1": self.H1 = self.main.screen.blit(self.main.figureH, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "HC1": self.HC1 = self.main.screen.blit(self.main.figureHC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "W1": self.W1 = self.main.screen.blit(self.main.figureW, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "W2": self.W2 = self.main.screen.blit(self.main.figureW, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "WC1": self.WC1 = self.main.screen.blit(self.main.figureWC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "WC2": self.WC2 = self.main.screen.blit(self.main.figureWC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "G1": self.G1 = self.main.screen.blit(self.main.figureG, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "G2": self.G2 = self.main.screen.blit(self.main.figureG, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "GC1": self.GC1 = self.main.screen.blit(self.main.figureGC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "GC2": self.GC2 = self.main.screen.blit(self.main.figureGC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "S1": self.S1 = self.main.screen.blit(self.main.figureS, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "S2": self.S2 = self.main.screen.blit(self.main.figureS, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "SC1": self.SC1 = self.main.screen.blit(self.main.figureSC, (self.posx * 82 + 2, self.posy * 82 + 2))
        if self.typ == "SC2": self.SC2 = self.main.screen.blit(self.main.figureSC, (self.posx * 82 + 2, self.posy * 82 + 2))












if __name__ == "__main__":
    main()