import pygame
import sys
from util.http import *

# 랭킹 창 구현

display_width = 1250  # 1250
display_height = 700  # 700
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])


def mode_screen(x, y):
    myImg = pygame.image.load('ranking_screen.png')
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
            if action == "quit":
                pygame.init()
                pygame.quit()


# 버튼 이미지 로딩
qt = pygame.image.load("quiticon.png").convert_alpha()
cqt = pygame.image.load("clickedQuitIcon.png").convert_alpha()


def rank_screen():
    pygame.init()
    clock = pygame.time.Clock()
    active = False
    # basic font for user typed
    base_font = pygame.font.SysFont('malgungothic', 40)
    WHITE = (255, 255, 255)
    code, val = get_scores(1)
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
        button(180, 600, 100, 20, WHITE, WHITE, qt, cqt, "quit")
        # 사용자 이름, 점수 출력하기
        if code == 200:
            val: list[UserScore]
            interval = 0
            count = 0
            for score in val:
                if count < 7:  # 7등 까지만 보여주기
                    user_str = str(score.name)+' ' + str(score.score)
                    user_image = base_font.render(user_str, True, (0, 0, 0))
                    SURFACE.blit(user_image, (480, 100+interval))
                    interval += 75
                    count += 1

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    rank_screen()
