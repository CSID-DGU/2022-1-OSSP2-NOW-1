import pygame
from random import *
from pygame.locals import *
import sys

pygame.init()
#display_width, display_height 고정
display_width = 1200
display_height = 650

# 배경 이미지 위치 지정
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])

# 버튼 이미지 불러오기
startImg = pygame.image.load("starticon.png")
clickStartImg = pygame.image.load("clickedStartIcon.png")
quitImg = pygame.image.load("quiticon.png")
clickQuitImg = pygame.image.load("clickedQuitIcon.png")

#pygame 창이름 설정
pygame.display.set_caption("시간표 테트리스, 시간표팡!")

#색깔 : 흰색만 사용
WHITE=(255,255,255)

# 시작 화면 그리기
def start_screen(x,y):
    myImg = pygame.image.load('first_bgr.png')
    SURFACE.blit(myImg,(x,y))
    #시작 화면 버튼 그리기 (버튼 위치 참고용)
    #pygame.draw.rect(SURFACE,GREEN,(250,480,180,68))
    #pygame.draw.rect(SURFACE,RED,(870,480,180,68))

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
              game()


strt = pygame.image.load("starticon.png").convert_alpha()
cstrt = pygame.image.load("clickedStartIcon.png").convert_alpha()
qt = pygame.image.load("quiticon.png").convert_alpha()
cqt = pygame.image.load("clickedQuitIcon.png").convert_alpha()

#event handling logic
finished = False
while not finished :
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
            pygame.quit()
            quit()

    SURFACE.fill((255,255,255)) #배경색 지정
    start_screen(x,y) #이미지 그리기
    pygame.display.flip()
    button(250, 480, 180, 68, WHITE, WHITE, strt, cstrt, "continue")
    button(870,480,180,68,WHITE,WHITE,qt,cqt,"quit")
    pygame.display.update()

