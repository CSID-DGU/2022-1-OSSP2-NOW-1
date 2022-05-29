import pygame
import sys
from game import *
from util.http import *
from util.getloc2 import *
#개인모드 시간표 선택 창
display_width = 1200
display_height = 650
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])

def mode_screen(x,y):
    myImg = pygame.image.load('indi_tetro_bgr.png')
    SURFACE.blit(myImg,(x,y))

def button(x,y,w,h,ic,ac,oneP,clickOne,user_text, pwww_text,action = None):
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
            if action == "one_tetro" :
                game_personal(user_text, pwww_text, 0)
            elif action =="two_tetro":
                game_personal(user_text, pwww_text, 1)
            elif action == "three_tetro":
                game_personal(user_text, pwww_text, 2)
            elif action =="four_tetro":
                game_personal(user_text, pwww_text, 3)



#버튼 이미지 로딩
uone = pygame.image.load("univ_one.PNG").convert_alpha()
cuone = pygame.image.load("clickedUniv_one.PNG").convert_alpha()
utwo = pygame.image.load("univ_two.PNG").convert_alpha()
cutwo = pygame.image.load("clickedUniv_two.PNG").convert_alpha()
uthree = pygame.image.load("univ_three.PNG").convert_alpha()
cuthree = pygame.image.load("clickedUniv_three.PNG").convert_alpha()
ufour = pygame.image.load("univ_four.PNG").convert_alpha()
cufour = pygame.image.load("clickedUniv_four.PNG").convert_alpha()

def indi_tetropool_screen(user_text, pwww_text) :
    pygame.init()
    clock = pygame.time.Clock()
    active = False
    # basic font for user typed
    base_font = pygame.font.SysFont('malgungothic', 45)
    univ_font = pygame.font.SysFont('malgungothic', 28)
    winner_text = ''
    WHITE = (255, 255, 255)
    pygame.display.set_caption("시간표 테트리스, 시간표팡!")

    # create rectangle INPUT_RECT
    input_rect = pygame.Rect(540, 250, 140, 50)
    color_active = pygame.Color((255, 255, 255))
    color_passive = pygame.Color((255, 255, 255))
    color = color_passive
    while True:
        for event in pygame.event.get():

            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

        # it will set background color of screen
        SURFACE.fill((255, 255, 255))
        mode_screen(x, y)
        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        button(580, 220, 100, 30, WHITE, WHITE, uone, cuone, user_text, pwww_text, "one_tetro",)
        button(575, 320, 100, 30, WHITE, WHITE, utwo, cutwo, user_text, pwww_text, "two_tetro")
        button(575, 420, 100, 30, WHITE, WHITE, uthree, cuthree, user_text, pwww_text, "three_tetro")
        button(575, 520, 100, 30, WHITE, WHITE, ufour, cufour, user_text, pwww_text, "four_tetro")

        # 시간표 테트로미노 select 나타내기
        table_str1 = str("1번 시간표")
        table_image1 = univ_font.render(table_str1, True, (0, 0, 0))
        SURFACE.blit(table_image1, (530, 220))

        table_str2 = str("2번 시간표")
        table_image2 = univ_font.render(table_str2, True, (0, 0, 0))
        SURFACE.blit(table_image2, (530, 320))

        table_str3 = str("3번 시간표")
        table_image3 = univ_font.render(table_str3, True, (0, 0, 0))
        SURFACE.blit(table_image3, (530, 420))

        table_str4 = str("4번 시간표")
        table_image4 = univ_font.render(table_str4, True, (0, 0, 0))
        SURFACE.blit(table_image4, (530, 520))



        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    indi_tetropool_screen("leeminsuok", "052978a")