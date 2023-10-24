import pygame
import sys
from util.http import *
from screen.game import *
from screen.screen_key import *

# 개인모드 시간표 선택 창

SURFACE = pygame.display.set_mode([display_width, display_height])
pygame.init()

# univs = get_univs()
univs: list[University] = []

def mode_screen(x, y):
    myImg = pygame.image.load(adress + 'indi_tetro_bgr.png')
    SURFACE.blit(myImg, (x, y))


def button(x, y, w, h, ic, ac, oneP, clickOne, id, action=None):
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
            if action == "one_tetro":
                game_competition(id)
            elif action == "two_tetro":
                game_competition(id)
            elif action == "three_tetro":
                game_competition(id)
            elif action == "four_tetro":
                game_competition(id)
            elif action == "quit":
                pygame.display.quit()


# 버튼 이미지 로딩
uone = pygame.image.load(adress + "univ_one.PNG").convert_alpha()
cuone = pygame.image.load(adress + "clickedUniv_one.PNG").convert_alpha()
utwo = pygame.image.load(adress + "univ_two.PNG").convert_alpha()
cutwo = pygame.image.load(adress + "clickedUniv_two.PNG").convert_alpha()
uthree = pygame.image.load(adress + "univ_three.PNG").convert_alpha()
cuthree = pygame.image.load(adress + "clickedUniv_three.PNG").convert_alpha()
ufour = pygame.image.load(adress + "univ_four.PNG").convert_alpha()
cufour = pygame.image.load(adress + "clickedUniv_four.PNG").convert_alpha()

quit = pygame.image.load(adress + "quitIcon.png").convert_alpha()
cquit = pygame.image.load(adress + "clickedQuitIcon.png").convert_alpha()


def univ_tetropool_screen(id):
    pygame.init()
    sleep(0.1)
    clock = pygame.time.Clock()
    active = False
    # basic font for user typed
    base_font = pygame.font.SysFont('malgungothic', 45)
    univ_font = pygame.font.SysFont('malgungothic', 15)
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
        button(580, 220, 100, 30, WHITE, WHITE, uone, cuone, id, "one_tetro")
        button(575, 320, 100, 30, WHITE, WHITE, utwo, cutwo, id, "two_tetro")
        button(575, 420, 100, 30, WHITE, WHITE,
               uthree, cuthree, id, "three_tetro")
        button(575, 520, 100, 30, WHITE, WHITE,
               ufour, cufour, id, "four_tetro")

        button(190, 540, 100, 20, WHITE, WHITE, quit, cquit, id, "quit")

        # 시간표 테트로미노 select 나타내기
        code, tetro_pools = get_tetro_list(univs[0].id)
        if code == 200:
            tt: list[TetroPool] = tetro_pools
            # t 는 DetailedLecture
            interval = 0
            for t in tt:
                tt_str = str(t.id) + ' ' + str(t.name) + \
                    ' ' + str(t.description)
                tt_image = univ_font.render(tt_str, True, (0, 0, 0))
                SURFACE.blit(tt_image, (520, 220+interval))
                interval += 100

        pygame.display.update()
        # clock.tick(60)


if __name__ == '__main__':
    univ_tetropool_screen(1)
