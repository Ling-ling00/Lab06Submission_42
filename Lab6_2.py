import sys 
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.colorR = 255
        self.colorG = 100
        self.colorB = 100
    def draw(self, screen):
        pg.draw.rect(screen, (self.colorR, self.colorG, self.colorB), (self.x, self.y, self.w, self.h))
    def changeColor(self, colorR, colorG, colorB):
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB
    def plusPosX(self):
        self.x += 1
    def minPosX(self):
        self.x -= 1
    def plusPosY(self):
        self.y -= 1
    def minPosY(self):
        self.y += 1

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
rec = Rectangle(20,20,100,100)
changeTypeX = 0
changeTypeY = 0
changeTypeS = 0

while(run):
    screen.fill((255, 255, 255))
    rec.draw(screen)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            changeTypeX = 1
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม A
            changeTypeX = -1
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
            changeTypeY = 1
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นปุ่ม S
            changeTypeY = -1
        if event.type == pg.KEYDOWN and event.key == pg.K_q: #ปุ่มถูกกดลงและเป็นปุ่ม Q
            changeTypeS = -1
        if event.type == pg.KEYDOWN and event.key == pg.K_e: #ปุ่มถูกกดลงและเป็นปุ่ม E
            changeTypeS = 1
        if event.type == pg.KEYUP and (event.key == pg.K_d or event.key == pg.K_a):
            changeTypeX = 0
        if event.type == pg.KEYUP and (event.key == pg.K_w or event.key == pg.K_s):
            changeTypeY = 0
        if event.type == pg.KEYUP and (event.key == pg.K_q or event.key == pg.K_e):
            changeTypeS = 0

    
    if changeTypeX == 1:
        rec.plusPosX()
    elif changeTypeX == -1:
        rec.minPosX()
    if changeTypeY == 1:
        rec.plusPosY()
    elif changeTypeY == -1:
        rec.minPosY()
    if changeTypeS == 1:
        rec.w += 1
        rec.h += 1
    elif changeTypeS == -1:
        rec.w -= 1
        rec.h -= 1

    if rec.x < 0:
        rec.plusPosX()
    elif rec.x + rec.w > win_x:
        rec.minPosX()
    if rec.y < 0:
        rec.minPosY()
    elif rec.y + rec.h > win_y:
        rec.plusPosY()
    if rec.w <= 0:
        rec.w += 1
        rec.h += 1
    elif rec.y + rec.h > win_y or rec.x + rec.w > win_x:
        rec.w -= 1
        rec.h -= 1