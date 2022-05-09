import pygame
from pygame.locals import *
import sys

pygame.init()
#게임 윈도우는 700 800으로 초기 설정되어 있었음.
display_width = 1200
display_height = 650

SURFACE = pygame.display.set_mode([display_width, display_height])
myImg = pygame.image.load('game_first_img.png')
# 버튼 객체
class button(pygame.sprite.Sprite):
    def __init__(self,text,x,y):
        super().__init__()
        font = pygame.font.SysFont("none",20)
        self.image = font.render(str(text),True,black)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
#마우스 포인터 커서 sprite 생성
class point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([1,1],pygame.SRCALPHA,32) #1x1px 짜리 투명한 sprite 생성
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]

if __name__ == "__main__":









def myimage(x,y):
    SURFACE.blit(myImg,(x,y))
#이미지 위치 지정
x = (display_width* 0.00000000000000002)
y = (display_height*0.00000000000000002)

#event handling logic
finished = False
while not finished :
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True

    SURFACE.fill((255,255,255)) #배경색 지정
    myimage(x,y) #이미지 그리기
    pygame.display.flip()
pygame.quit()
quit()

