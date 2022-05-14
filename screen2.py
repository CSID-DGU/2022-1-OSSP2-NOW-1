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

# 모드 버튼 이미지 확장자명
#playerOneImg = pygame.image.load("mode_1icon.png")
#playerMultiImg = pygame.image.load("mode_2icon.png")
#clickOneImg = pygame.image.load("clickedMode_1Icon.png")
#clickMultiImg = pygame.image.load("clickedMode_2Icon.png")

#pygame 창이름 설정
pygame.display.set_caption("시간표 테트리스, 시간표팡!")

#색깔 : 흰색만 사용
WHITE=(255,255,255)

# 시작 화면 그리기
def mode_screen(x,y):
    myImg = pygame.image.load('mode_bgr.png')
    SURFACE.blit(myImg,(x,y))

# 버튼
def button(x,y,w,h,ic,ac,oneP,clickOne,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x,y,w,h)
    on_button = rect.collidepoint(mouse)
    if on_button :
        pygame.draw.rect(SURFACE, ac, rect)
        SURFACE.blit (clickOne,clickOne.get_rect(center = rect.center))
    else :
        pygame.draw.rect(SURFACE, ic, (x,y,w,h))
        SURFACE.blit (oneP,oneP.get_rect(center = rect.center))


#버튼 클릭 수행
    if on_button :
      if click[0]==1 and action != None:
          if action == "playerOne" :
              playeronegame()
          elif action =="playerMulti":
              playertwogame()



oneP = pygame.image.load("mode_1icon.png").convert_alpha()
multiP = pygame.image.load("mode_2Icon.png").convert_alpha()
clickOne = pygame.image.load("clickedMode_1Icon.png").convert_alpha()
clickMulti = pygame.image.load("clickedMode_2Icon.png").convert_alpha()

#event handling logic
finished = False
while not finished :
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
            pygame.quit()
            quit()

    SURFACE.fill((255,255,255)) #배경색 지정
    mode_screen(x,y) #이미지 그리기
    pygame.display.flip()
    button(570, 320, 180, 68, WHITE, WHITE, oneP, clickOne , "playerOne")
    button(550,490,180,68,WHITE,WHITE,multiP,clickMulti,"playerMulti")
    pygame.display.update()

