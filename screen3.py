import pygame
import sys

#에브리타임 로그인창
pygame.init()
clock = pygame.time.Clock()
display_width = 1200
display_height = 650
WHITE = (255,255,255)
x = (display_width * 0.00000000000000002)
y = (display_height * 0.00000000000000002)
SURFACE = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption("시간표 테트리스, 시간표팡!")

def mode_screen(x,y):
    myImg = pygame.image.load('ttpang2_bgr.PNG')
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
          if action == "prev" :
              game()
          elif action =="save":
              saveUser()

#버튼 이미지 로딩
prev = pygame.image.load("prevIcon.png").convert_alpha()
cprev= pygame.image.load("clickedPrevIcon.png").convert_alpha()
evrysav = pygame.image.load("evryLogicon.png").convert_alpha()
evrycsav = pygame.image.load("clickedEvryLogicon.png").convert_alpha()

#-----------------------------------------------텍스트 입력받는 부분 코드---------------------------------
# basic font for user typed
base_font = pygame.font.Font(None, 45)

user_text = ''
pwww_text = ''

# create rectangle INPUT_RECT
input_rect = pygame.Rect(410, 260, 140, 50)
inputpw_rect = pygame.Rect(410, 410, 140, 50)
color_active = pygame.Color((255,255,255))
color_passive = pygame.Color((255,255,255))
color = color_passive

active = False
input_enter = False

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputpw_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if input_enter == False :
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                elif event.key == pygame.K_RETURN:
                    input_enter = True
                else:
                    user_text += event.unicode
                    if len(user_text) > 20:
                        user_text = user_text[0:20]

        if input_enter == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pwww_text = pwww_text[:-1]
                elif event.key != pygame.K_RETURN:
                    pwww_text += event.unicode
                    if len(pwww_text) > 20:
                        pwww_text = pwww_text[0:20]

    # it will set background color of screen
    SURFACE.fill((255, 255, 255))
    mode_screen(x,y)
    if active:
        color = color_active
    else:
        color = color_passive

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(SURFACE, color, input_rect)
    pygame.draw.rect(SURFACE, color, inputpw_rect)
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    text_surface2 = base_font.render(pwww_text,True,(0,0,0))
    # render at position stated in arguments
    SURFACE.blit(text_surface, (input_rect.x + 1, input_rect.y + 1))
    SURFACE.blit(text_surface2,(inputpw_rect.x+1, inputpw_rect.y+1))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)
    button(220, 600, 100, 20, WHITE, WHITE, prev, cprev, "prev")
    button(620, 500, 50, 30, WHITE, WHITE, evrysav, evrycsav,"save")
    pygame.display.update()