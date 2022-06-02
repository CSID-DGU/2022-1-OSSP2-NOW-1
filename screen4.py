import pygame
import sys
from screen5 import *
from util.http import *

# 닉네임 입력창 구현

display_width = 1200
display_height = 650
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])


def mode_screen(x, y):
    myImg = pygame.image.load('ttpang4_bgr.PNG')
    SURFACE.blit(myImg, (x, y))


def button(x, y, w, h, ic, ac, oneP, clickOne, action=None, score=None, pool_info=None, nick=None):
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
            if action == "replay":
                # 리플레이 불가능
                game()
            elif action == "quit":
                pygame.quit()
            elif action == "save":
                set_score(pool_info, nick, score)
                univ_screen()


# 버튼 이미지 로딩
rep = pygame.image.load("replayicon.png").convert_alpha()
crep = pygame.image.load("clickedReplayIcon.png").convert_alpha()
qt = pygame.image.load("quiticon.png").convert_alpha()
cqt = pygame.image.load("clickedQuitIcon.png").convert_alpha()
sav = pygame.image.load("saveicon.png").convert_alpha()
csav = pygame.image.load("clickedSaveIcon.png").convert_alpha()


def nick_screen(score, pool_info):
    pygame.init()
    clock = pygame.time.Clock()
    active = False
    # basic font for user typed
    base_font = pygame.font.Font(None, 45)
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

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    winner_text = winner_text[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    winner_text += event.unicode
                    if len(winner_text) > 11:
                        winner_text = winner_text[0:11]

        # it will set background color of screen
        SURFACE.fill((255, 255, 255))
        mode_screen(x, y)
        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(SURFACE, color, input_rect)
        text_surface = base_font.render(winner_text, True, (0, 0, 0))
        # render at position stated in arguments
        SURFACE.blit(text_surface, (input_rect.x + 1, input_rect.y + 1))
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)
        button(260, 500, 150, 50, WHITE, WHITE, rep, crep, "replay")
        button(900, 500, 180, 60, WHITE, WHITE, qt, cqt, "quit")
        button(600, 350, 100, 30, WHITE, WHITE,
               sav, csav, "save", score, pool_info, winner_text)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    nick_screen(0, 0)
