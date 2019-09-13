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


        self.active = False


        while True:
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)

            self.pos = pg.mouse.get_pos()
            pressed1, pressed2, pressed3 = pg.mouse.get_pressed()

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP: self.active = False



            self.draw()

            if pressed3: self.active = False


            if self.drawLabel[3][2].collidepoint(self.pos) and pressed1 and self.active:
                self.moveFigure(0, 3, 3, 2)
                self.active = False

                print("lol")



            if self.K1.collidepoint(self.pos) and pressed1 or self.active:
                self.active = True
                #self.K1 = self.screen.blit(self.figureK, (self.pos[0]-40, self.pos[1]-40))




            pg.display.flip()


    def moveFigure(self,fr1,fr2,to1,to2):
        if fr1 != to1 or fr2 != to2:
            if self.matrix[fr1][fr2] != 0:
                self.matrix[to2][to1] = self.matrix[fr1][fr2]
                self.matrix[fr1][fr2] = 0



    def draw(self):
        pg.draw.rect(self.screen, (112, 41, 0), pg.Rect(0, 0, 658, 658))

        colorid=0
        for i in range(8):
            colorid += 1
            for j in range(8):
                if colorid%2 == 0: color = (90, 90, 90)
                else: color = (220, 220, 220)
                colorid += 1
                self.drawLabel[i][j] = pg.draw.rect(self.screen, (color), pg.Rect(i*82+2, j*82+2, 80, 80))

        for i in range(8):
            for j in range(8):
                if self.matrix[i][j] == "P1": self.P1 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P2": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P3": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P4": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P5": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P6": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P7": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "P8": self.P2 = self.screen.blit(self.figureP, (j*82+2, i*82+2))
                if self.matrix[i][j] == "PC1": self.PC1 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC2": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC3": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC4": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC5": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC6": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC7": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "PC8": self.PC2 = self.screen.blit(self.figurePC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "K": self.K1 = self.screen.blit(self.figureK, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "KC": self.KC1 = self.screen.blit(self.figureKC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "H": self.H1 = self.screen.blit(self.figureH, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "HC": self.HC1 = self.screen.blit(self.figureHC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "W1": self.W1 = self.screen.blit(self.figureW, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "W2": self.W2 = self.screen.blit(self.figureW, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "WC1": self.WC1 = self.screen.blit(self.figureWC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "WC2": self.WC2 = self.screen.blit(self.figureWC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "G1": self.G1 = self.screen.blit(self.figureG, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "G2": self.G2 = self.screen.blit(self.figureG, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "GC1": self.GC1 = self.screen.blit(self.figureGC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "GC2": self.GC2 = self.screen.blit(self.figureGC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "S1": self.S1 = self.screen.blit(self.figureS, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "S2": self.S2 = self.screen.blit(self.figureS, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "SC1": self.SC1 = self.screen.blit(self.figureSC, (j * 82 + 2, i * 82 + 2))
                if self.matrix[i][j] == "SC2": self.SC2 = self.screen.blit(self.figureSC, (j * 82 + 2, i * 82 + 2))




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
        self.matrix[1][3] = "P4"
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

        for i in range(8):
            self.drawLabel.append([])
            for j in range(8):
                self.drawLabel[i].append(0)

        for i in range(len(self.matrix)):
            print(self.matrix[i])







if __name__ == "__main__":
    main()