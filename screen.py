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

#색깔
BLACK=( 0,0,0)
WHITE=(255,255,255)
BLUE =(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)


# 시작 화면 그리기
def start_screen(x,y):
    myImg = pygame.image.load('game_first_img.png')
    SURFACE.blit(myImg,(x,y))
    #시작 화면 버튼 그리기
    pygame.draw.rect(SURFACE,GREEN,(250,480,180,68))
    pygame.draw.rect(SURFACE,RED,(870,480,180,68))

    #마우스 갖다 대면 색 변하기
    # 마우스
    # 평소에는 파란색이다가 마우스 갖다대면 파란색으로 변함
    mouse = pygame.mouse.get_pos()
    if 250+180 > mouse [0] and 480+68 > mouse[1] > 480 :
        pygame.draw.rect(SURFACE, GREEN, (250, 480, 180, 68))
    else :
        pygame.draw.rect(SURFACE, BLUE, (250, 480, 180, 68))


# 반대편도 하려는데 동시에 start 버튼을 누르니 두 색깔이 바뀌는 오류 발생 -> 해결해봐야함
   # if 870 + 180 > mouse[0] and 480+68 > mouse[1] > 480 :
    #    pygame.draw.rect(SURFACE,RED,(870,480,180,68))
    #else:
      #  pygame.draw.rect(SURFACE,BLACK,(870,480,180,68))

def button(msg,x,y,w,h,i,a,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse [0] > x  and y+h > mouse[1] >y :
        pygame.draw.rect(SURFACE, i, (x,y,w,h))
    else :
        pygame.draw.rect(SURFACE, a, (x,y,w,h))



#event handling logic
finished = False
while not finished :
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True

    SURFACE.fill((255,255,255)) #배경색 지정
    start_screen(x,y) #이미지 그리기
    pygame.display.flip()
pygame.quit()
quit()

