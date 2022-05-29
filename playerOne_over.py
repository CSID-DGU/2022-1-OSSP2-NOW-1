import pygame
import sys
import pygame
import sys

#닉네임 입력창 구현

display_width = 1200
display_height = 650
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])

def mode_screen(x,y):
    myImg = pygame.image.load('gameover_screen.png')
    SURFACE.blit(myImg,(x,y))

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
          if action == "quit" :
             pygame.quit()


#버튼 이미지 로딩
qt = pygame.image.load('quiticon.png').convert_alpha()
cqt = pygame.image.load('clickedQuitIcon.png').convert_alpha()

def gameOver_screen(indi_score=0000) :
    pygame.init()
    clock = pygame.time.Clock()
    active = False
    # basic font for user typed
    base_font = pygame.font.SysFont('malgungothic', 120)
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

        # it will set background color of screen
        SURFACE.fill((255, 255, 255))
        mode_screen(x, y)
        button(200, 600, 100, 20, WHITE, WHITE, qt, cqt, "quit")
        # 사용자 점수 나타내기
        indi_score_str = str(indi_score).zfill(6)
        indiScore_img = base_font.render(indi_score_str, True, (0,0, 0))
        SURFACE.blit(indiScore_img, (465, 360))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    gameOver_screen()