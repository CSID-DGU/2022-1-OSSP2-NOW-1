import pygame
from random import *
from pygame.locals import *
from screen.screen3 import *
from screen.screen_univ import *
from screen.screen_key import *

# 모드 선택 이미지
SURFACE = pygame.display.set_mode([display_width, display_height])
pygame.init()
# 시작 화면 그리기


def mode_screen(x, y):
    myImg = pygame.image.load(adress + 'ttpang3_bgr.PNG')
    SURFACE.blit(myImg, (x, y))

# 버튼


def button(x, y, w, h, ic, ac, oneP, clickOne, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)
    if on_button:
        pygame.draw.rect(SURFACE, ac, rect)
        SURFACE.blit(clickOne, clickOne.get_rect(center=rect.center))
    else:
        pygame.draw.rect(SURFACE, ic, (x, y, w, h))
        SURFACE.blit(oneP, oneP.get_rect(center=rect.center))

# 버튼 클릭 수행
    if on_button:
        if click[0] == 1 and action != None:
            if action == "playerOne":
                login_screen()
            elif action == "playerMulti":
                # 닉네임 만들기 전에, 학교 입력 받고, 강의풀 선택하는 창이 먼저 필요함.
                univ_screen()


oneP = pygame.image.load(adress + "mode_1icon.png").convert_alpha()
multiP = pygame.image.load(adress + "mode_2Icon.png").convert_alpha()
clickOne = pygame.image.load(adress + "clickedMode_1Icon.png").convert_alpha()
clickMulti = pygame.image.load(
    adress + "clickedMode_2Icon.png").convert_alpha()
prev = pygame.image.load(adress + "quitIcon.png").convert_alpha()
cprev = pygame.image.load(adress + "clickedQuitIcon.png").convert_alpha()


def mode_select_screen():
    # 모드 선택
    pygame.init()
    # pygame 창이름 설정
    pygame.display.set_caption("시간표 테트리스, 시간표팡!")
    # 색깔 : 흰색만 사용
    WHITE = (255, 255, 255)
    # event handling logic
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == QUIT:
                finished = True
                pygame.quit()
                quit()

        SURFACE.fill((255, 255, 255))  # 배경색 지정
        mode_screen(x, y)  # 이미지 그리기
        button(570, 320, 180, 68, WHITE, WHITE, oneP, clickOne, "playerOne")
        button(550, 490, 180, 68, WHITE, WHITE,
               multiP, clickMulti, "playerMulti")
        button(220, 600, 100, 20, WHITE, WHITE, prev, cprev, "prev")
        pygame.display.update()


if __name__ == '__main__':
    mode_select_screen()
