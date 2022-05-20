import pygame
import sys

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
    myImg = pygame.image.load('nickname_bgr.png')
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
          if action == "replay" :
              game()
          elif action =="quit":
              quit()

#버튼 이미지 로딩
rep = pygame.image.load("replayicon.png").convert_alpha()
crep = pygame.image.load("clickedReplayIcon.png").convert_alpha()
qt = pygame.image.load("quiticon.png").convert_alpha()
cqt = pygame.image.load("clickedQuitIcon.png").convert_alpha()

# basic font for user typed
base_font = pygame.font.Font(None, 60)
user_text = ''

# create rectangle INPUT_RECT
input_rect = pygame.Rect(565, 300, 140, 60)
#최대 12글자까지 저장하게끔

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

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
                 user_text = user_text[:-1]
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
                #LIMIT THE INPUT_RECT CHARACTER
                #-20 FOR BORDER WIDTH
                if text_surface.get_width() > input_rect.w - 40:
                    user_text = user_text[:-1]
    # it will set background color of screen
    SURFACE.fill((255, 255, 255))
    mode_screen(x,y)
    pygame.display.flip()
    if active:
        color = color_active
    else:
        color = color_passive

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(SURFACE, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    # render at position stated in arguments
    SURFACE.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)
    button(220, 480, 180, 60, WHITE, WHITE, rep, crep, "replay")
    button(900, 480, 180, 60, WHITE, WHITE, qt, cqt, "quit")
    pygame.display.flip()
    clock.tick(60)