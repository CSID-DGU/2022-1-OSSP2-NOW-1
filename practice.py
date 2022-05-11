
import pygame
from pygame.locals import *
import ctypes  # 해상도 구하는 용도

surface = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == ord('f'):  # f 키를 눌렀을 때
                user32 = ctypes.windll.user32
                screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)  # 해상도 구하기
                surface = pygame.display.set_mode(screensize, FULLSCREEN)  # 전체화면으로 전환

    pygame.display.update()
    surface.fill((255, 255, 255))