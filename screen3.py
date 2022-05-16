import pygame
from random import *
from pygame.locals import *
import sys

pygame.init()
clock = pygame.time.Clock()
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

#display_width, display_height 고정, 색 설정, 창 이름 설정
display_width = 1200
display_height = 650
WHITE=(255,255,255)
pygame.display.set_caption("시간표 테트리스, 시간표팡!")


# 배경 이미지 위치 지정
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])

class InputBox :
    def __init__(self,x,y,w,h, text = ''):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text,True,self.color)
        self.active = False

    def handle_event(self,event):
        if event.type ==pygame.MOUSEBUTTONDOWN:
            #IF THE USER CLICKED ON THE INPUT_BOX RECT
          if self.rect.collidepoint(event.pos):
              #TOGGLE THE ACTIVE VARIABLE
             self.active = not self.active
          else :
              self.active = False
          #CHANGE THE COLOR OF THE INPUT BOX
          self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type ==pygame.KEYDOWN:
            if self.active :
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key ==pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text +=event.unicode
                #RE-RENDER THE TEXT
                self.txt_surface = FONT.render(self.text,True, self.color)

    def update(self):
        #RESIZE THE BOX IF THE TEXT IS TOO LONG
        width = max(200,self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, SURFACE):
        #BLIT THE TEXT
        SURFACE.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        #BLIT THE RECT
        pygame.draw.rect(SURFACE, self.color, self.rect, 2)

# 시작 화면 그리기
def mode_screen(x,y):
    myImg = pygame.image.load('everytime_bgr.png')
    SURFACE.blit(myImg,(x,y))

# 버튼 (only for quit)
def button(x,y,w,h,ic,ac,quit,cquit,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x,y,w,h)
    on_button = rect.collidepoint(mouse)
    if on_button :
        pygame.draw.rect(SURFACE, ac, rect)
        SURFACE.blit (cquit,cquit.get_rect(center = rect.center))
    else :
        pygame.draw.rect(SURFACE, ic, (x,y,w,h))
        SURFACE.blit (quit,quit.get_rect(center = rect.center))

#버튼 클릭 수행
    if on_button :
      if click[0]==1 and action != None:
          if action == "quit" :
              quit

qt = pygame.image.load("quiticon.png").convert_alpha()
cqt = pygame.image.load("clickedQuitIcon.png").convert_alpha()
input_id = InputBox(250,250,140,32)
input_pw = InputBox(500,500,140,32)
input_boxes = [input_id, input_pw]

#event handling logic
finished = False
while not finished :
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
            #pygame.quit()
            #quit()
        for box in input_boxes:
            box.handle_event(event)

    for box in input_boxes:
        box.update()

    SURFACE.fill((255,255,255)) #배경색 지정
    SURFACE.fill((30,30,30))
    for box in input_boxes:
        box.draw(SURFACE)
    mode_screen(x,y) #이미지 그리기
    pygame.display.flip()
    button(920,530,180,68,WHITE,WHITE,qt,cqt,"quit")
    pygame.display.update()