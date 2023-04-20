import sys
import pygame as pg
pg.init()

class TextBox:
    def __init__(self, x, y, text=''):
        self.color = textColor
        self.text = FONT.render(text, True, self.color)
        self.textRect = (x, y)
    def draw(self,screen):
        screen.blit(self.text, self.textRect)
    def changeText(self,text):
        self.text = FONT.render(text, True, self.color)
    
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def number_check(self):
        if(self.text[-1:].isnumeric()):
            pass
        else:
            self.text = self.text[:-1]
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Button:
    def __init__(self, x, y, text=''):
        self.color = buttonColor
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.rect = pg.Rect(x, y, self.txt_surface.get_width()+10, self.txt_surface.get_height()+10)
    
    def isMousePress(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
    
    def draw(self, Screen):
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = (245, 202, 195)
COLOR_ACTIVE = (242, 132, 130)
FONT = pg.font.Font(None, 32)
textColor = (132, 165, 157)
buttonColor = (246, 189, 96)
returnText = ''

text1 = TextBox(100, 50, "First name")
text2 = TextBox(100, 150, "Last name")
text3 = TextBox(100, 250, "Age")
text4 = TextBox(100, 350, returnText)
text_boxes = [text1, text2, text3, text4]
input_box1 = InputBox(100, 75, 140, 32)
input_box2 = InputBox(100, 175, 140, 32)
input_box3 = InputBox(100, 275, 140, 32)
input_boxes = [input_box1, input_box2, input_box3]
button = Button(500, 175, 'Submit')
run = True

while run:
    screen.fill((247, 237, 226))
    button.draw(screen)
    for text in text_boxes:
        text.draw(screen)
    for box in input_boxes:
        box.update()
        box.draw(screen)
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        input_box3.number_check()
        if button.isMousePress(event):
            returnText = 'Hello '+ input_box1.text + ' ' + input_box2.text + '! You are ' + input_box3.text + ' years old.'
            text4.changeText(returnText)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    pg.time.delay(1)
    pg.display.update()
