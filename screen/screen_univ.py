import pygame
import sys
from util.http import *
from .screen_univ_tetro import *
from .screen_key import *

# 대학교 선택

SURFACE = pygame.display.set_mode([display_width, display_height])

# univs = get_univs()
univs: list[University] = []

def mode_screen(x, y):
    myImg = pygame.image.load(adress + 'screen_seluniv.jpg')
    SURFACE.blit(myImg, (x, y))


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
            no_univ_message = "학교를 추가해 주세요"
            no_univ_image = pygame.font.SysFont(
                'malgungothic', 28).render(no_univ_message, True, (0, 0, 0))
            if action == "one_univ":
                if (len(univs) > 0):
                    # print(univs[1].id)
                    univ_tetropool_screen(univs[1].id)
                else:
                    SURFACE.blit(no_univ_image, (520, y-9))
            elif action == "two_univ":
                if (len(univs) > 1):
                    # print(univs[1].id)
                    univ_tetropool_screen(univs[1].id)
                else:
                    SURFACE.blit(no_univ_image, (520, y-9))
            elif action == "three_univ":
                if (len(univs) > 2):
                    # print(univs[2].id)
                    univ_tetropool_screen(univs[2].id)
                else:
                    SURFACE.blit(no_univ_image, (520, y-9))
            elif action == "four_univ":
                if (len(univs) > 3):
                    # print(univs[3].id)
                    univ_tetropool_screen(univs[3].id)
                else:
                    SURFACE.blit(no_univ_image, (520, y-9))
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


def univ_screen():
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

        button(575, 220, 100, 30, WHITE, WHITE, uone, cuone, "one_univ")
        button(575, 320, 100, 30, WHITE, WHITE, utwo, cutwo, "two_univ")
        button(575, 420, 100, 30, WHITE, WHITE, uthree, cuthree, "three_univ")
        button(575, 520, 100, 30, WHITE, WHITE, ufour, cufour, "four_univ")

        button(190, 540, 100, 20, WHITE, WHITE, quit, cquit, "quit")

        # 대학교 나타내기
        for i in range(min(len(univs), 4)):
            univ_str = univs[i].name if len(univs) > 0 else "no university"
            univ_image = univ_font.render(univ_str, True, (0, 0, 0))
            SURFACE.blit(univ_image, (530, 220))

        pygame.display.update()
        # clock.tick(60)


if __name__ == '__main__':
    univ_screen()
