import pygame
from random import *
from pygame.locals import *
import sys

pygame.init()
clock = pygame.time.Clock()

#basic type for user typed
base_font = pygame.font.Font(None,32)
user_id = ''
user_pw = ''

#display_width, display_height 고정, 색 설정, 창 이름 설정
display_width = 1200
display_height = 650
WHITE=(255,255,255)
pygame.display.set_caption("시간표 테트리스, 시간표팡!")


# 배경 이미지 위치 지정
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])


# 시작 화면 그리기
def mode_screen(x,y):
    myImg = pygame.image.load('everytime_bgr.png')
    SURFACE.blit(myImg,(x,y))

def user_input(user_id,user_pw) :
    # input_id 받을 사각형 그리기
    input_id = pygame.Rect(200, 200, 140, 32)
    input_pw = pygame.Rect(200, 300, 140, 32)

    # 사용자에 의해 input 박스가 눌러졌을 때 활성화 될 색깔 설정
    color_active = pygame.Color('lightskyblue3')
    # input 박스 자체의 색깔 설정
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if input_id.collidepoint(event.pos):
            active = True
        else:
            active = False
        if input_pw.collidepoint(event.pos):
            active = True
        else:
            active = False

    if event.type == pygame.KEYDOWN :
        #CHECK FOR BACKSPACE
        if event.key == pygame.K_BACKSPACE :
          #GET TEXT INPUT FROM 0 TO -1 I.E. END.
           user_id = user_id[:-1]
           user_pw = user_pw[:-1]
        else :
            #UNICODE STANDARD IS USED FOR STRING
            #FORMATION
          user_id += event.unicode
          user_pw += event.unicode

    pygame.draw.rect(SURFACE, WHITE,input_id)
    pygame.draw.rect(SURFACE, WHITE,input_pw)
    text_surface1 = base_font.render(user_id,True,WHITE)
    text_surface2 = base_font.render(user_pw,True,WHITE)

    #render at position
    SURFACE.blit(text_surface1,(input_id.x+5, input_id.y+5))
    SURFACE.blit(text_surface2,(input_pw.x+5, input_pw.y+5))

    #set width of text_field so that text cannot get outside of user's text output
    input_id.w = max(100,text_surface1.get_width()+10)
    input_pw.w = max(100,text_surface2.get_width()+10)


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
    user_input(user_id,user_pw) # 아이디입력하기
    pygame.display.flip()
    button(920,530,180,68,WHITE,WHITE,qt,cqt,"quit")
    pygame.display.update()
