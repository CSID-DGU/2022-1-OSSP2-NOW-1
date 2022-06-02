import pygame
import sys
from util.http import *
from screen_univ_tetro import *

# 닉네임 입력창 구현

display_width = 1200
display_height = 650
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])
univs = get_univs()


def mode_screen(x, y):
    myImg = pygame.image.load('screen_seluniv.jpg')
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
            no_univ = str("학교를 추가해 주세요")
            no_univ_image = pygame.font.SysFont(
                'malgungothic', 28).render(no_univ, True, (0, 0, 0))
            if action == "one_univ":
                # print(univs[0].id)
                univ_tetropool_screen(univs[0].id)
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


# 버튼 이미지 로딩
uone = pygame.image.load("univ_one.PNG").convert_alpha()
cuone = pygame.image.load("clickedUniv_one.PNG").convert_alpha()
utwo = pygame.image.load("univ_two.PNG").convert_alpha()
cutwo = pygame.image.load("clickedUniv_two.PNG").convert_alpha()
uthree = pygame.image.load("univ_three.PNG").convert_alpha()
cuthree = pygame.image.load("clickedUniv_three.PNG").convert_alpha()
ufour = pygame.image.load("univ_four.PNG").convert_alpha()
cufour = pygame.image.load("clickedUniv_four.PNG").convert_alpha()


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

        button(580, 220, 100, 30, WHITE, WHITE, uone, cuone, "one_univ")
        button(575, 320, 100, 30, WHITE, WHITE, utwo, cutwo, "two_univ")
        button(575, 420, 100, 30, WHITE, WHITE, uthree, cuthree, "three_univ")
        button(575, 520, 100, 30, WHITE, WHITE, ufour, cufour, "four_univ")

        # 대학교 나타내기
        univ_str = str(univs[0].name)
        univ_image = univ_font.render(univ_str, True, (0, 0, 0))
        SURFACE.blit(univ_image, (530, 220))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    univ_screen()
