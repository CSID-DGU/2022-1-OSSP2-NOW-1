import pygame
from random import *
from pygame.locals import *
import sys
from screen3 import *

# display_width, display_height 고정
display_width = 1200
display_height = 650

# 배경 이미지 위치 지정
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])

# 시작 화면 그리기
def start_screen(x,y):
    myImg = pygame.image.load('ttpang1_bgr.PNG')
    SURFACE.blit(myImg,(x,y))

# 버튼
def button(x,y,w,h,ic,ac,strt,cstrt,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x,y,w,h)
    on_button = rect.collidepoint(mouse)
    if on_button :
        pygame.draw.rect(SURFACE, ac, rect)
        SURFACE.blit (cstrt,cstrt.get_rect(center = rect.center))
    else :
        pygame.draw.rect(SURFACE, ic, (x,y,w,h))
        SURFACE.blit (strt,strt.get_rect(center = rect.center))

#버튼 클릭 수행
    if on_button :
      if click[0]==1 and action != None:
          if action == "continue" :
            rogin_screen() #다음모드로 넘어가게
          elif action == "quit":
            pygame.quit()


# 버튼이미지로딩
strt = pygame.image.load("starticon.png").convert_alpha()
cstrt = pygame.image.load("clickedStartIcon.png").convert_alpha()
qt = pygame.image.load("quiticon.png").convert_alpha()
cqt = pygame.image.load("clickedQuitIcon.png").convert_alpha()


def screen1() :
    # event handling logic
    pygame.init()
    finished = False
    # 색깔 : 흰색만 사용
    WHITE = (255, 255, 255)
    # pygame 창이름 설정
    pygame.display.set_caption("시간표 테트리스, 시간표팡!")
    while not finished:
        for event in pygame.event.get():
            if event.type == QUIT:
                finished = True
                pygame.quit()
                quit()

        SURFACE.fill((255, 255, 255))  # 배경색 지정
        start_screen(x, y)  # 이미지 그리기
        button(250, 480, 180, 68, WHITE, WHITE, strt, cstrt, "continue")
        button(870, 480, 180, 68, WHITE, WHITE, qt, cqt, "quit")
        pygame.display.update()

#screen1()
