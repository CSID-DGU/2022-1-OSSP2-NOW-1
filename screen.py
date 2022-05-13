import pygame
from random import *
from pygame.locals import *
import sys

pygame.init()
#display_width, display_height 고정
display_width = 1200
display_height = 650

# 이미지 위치 지정
x = (display_width* 0.00000000000000002)
y = (display_height*0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])
startImg = pygame.image.load("starticon.png")
clickStartImg = pygame.image.load("clickedStartIcon.png")
quitImg = pygame.image.load("quiticon.png")
clickQuitImg = pygame.image.load("clickedQuitIcon.png")
pygame.display.set_caption("시간표팡")

#색깔
BLACK=( 0,0,0)
WHITE=(255,255,255)
BLUE =(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)


# 시작 화면 그리기
def start_screen(x,y):
    myImg = pygame.image.load('bgrIMG.png')
    SURFACE.blit(myImg,(x,y))
    #시작 화면 버튼 그리기
    #pygame.draw.rect(SURFACE,GREEN,(250,480,180,68))
    #pygame.draw.rect(SURFACE,RED,(870,480,180,68))

    #마우스 갖다 대면 색 변하기
    # 마우스
    # 평소에는 파란색이다가 마우스 갖다대면 파란색으로 변함



# 반대편도 하려는데 동시에 start 버튼을 누르니 두 색깔이 바뀌는 오류 발생 -> 해결해봐야함
   # if 870 + 180 > mouse[0] and 480+68 > mouse[1] > 480 :
    #    pygame.draw.rect(SURFACE,RED,(870,480,180,68))
    #else:
      #  pygame.draw.rect(SURFACE,BLACK,(870,480,180,68))

def button(x,y,w,h,ic,ac,img,imgon,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x,y,w,h)
    on_button = rect.collidepoint(mouse)
    if on_button :
        pygame.draw.rect(SURFACE, ac, rect)
        SURFACE.blit (imgon,imgon.get_rect(center = rect.center))
    else :
        pygame.draw.rect(SURFACE, ic, (x,y,w,h))
        SURFACE.blit (img,img.get_rect(center = rect.center))

    if on_button :
      if click[0]==1 and action != None:
          if action == "continue" :
              game()


img = pygame.image.load("starticon.png").convert_alpha()
imgOn = pygame.image.load("clickedStartIcon.png").convert_alpha()

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
    button(250, 480, 180, 68, WHITE, WHITE, img, imgOn, "continue")
    pygame.display.update()

