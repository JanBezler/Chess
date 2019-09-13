import pygame as pg
import sys
import time
from os import path
from os import system





class main(object):
    def __init__(self):
        self.screen = pg.display.set_mode((860,658))
        self.loadData()
        self.firstMakeMatrix()
        pg.init()
        pg.display.set_caption("Game")















    def firstMakeMatrix(self):
        self.matrix = []
        self.drawLabel = []

        for i in range(8):
            self.matrix.append([])
            for j in range(8):
                self.matrix[i].append(0)

        self.matrix[0][0] = "W1"
        self.matrix[0][1] = "S1"
        self.matrix[0][2] = "G1"
        self.matrix[0][3] = "K"
        self.matrix[0][4] = "H"
        self.matrix[0][5] = "G2"
        self.matrix[0][6] = "S2"
        self.matrix[0][7] = "W2"
        self.matrix[1][0] = "P1"
        self.matrix[1][1] = "P2"
        self.matrix[1][2] = "P3"
        self.matrix[1][0] = "P4"
        self.matrix[1][4] = "P5"
        self.matrix[1][5] = "P6"
        self.matrix[1][6] = "P7"
        self.matrix[1][7] = "P8"

        self.matrix[6][0] = "P1"
        self.matrix[6][1] = "P2"
        self.matrix[6][2] = "P3"
        self.matrix[6][3] = "P4"
        self.matrix[6][4] = "P5"
        self.matrix[6][5] = "P6"
        self.matrix[6][6] = "P7"
        self.matrix[6][7] = "P8"
        self.matrix[7][0] = "WC1"
        self.matrix[7][1] = "SC1"
        self.matrix[7][2] = "GC1"
        self.matrix[7][3] = "KC"
        self.matrix[7][4] = "HC"
        self.matrix[7][5] = "GC2"
        self.matrix[7][6] = "SC2"
        self.matrix[7][7] = "WC2"

        for i in range(len(self.matrix)):
            print(self.matrix[i])



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



if __name__ == "__main__":
    main()