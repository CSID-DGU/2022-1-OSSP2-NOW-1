import pygame, random
from pygame.locals import *

FONT_SIZE = 60

def name():
    display_width = 1200
    display_height = 650
    WHITE = (255, 255, 255)
    x = (display_width * 0.00000000000000002)
    y = (display_height * 0.00000000000000002)
    SURFACE = pygame.display.set_mode([display_width, display_height])
    pygame.display.set_caption("시간표 테트리스, 시간표팡!")
    name = ""
    lol = random.randint(0, 100)
    font = pygame.font.SysFont(None, FONT_SIZE)

    while True:
        #  readlines returns a list; having this in
        #  loop allows pygame to draw recently added
        #  string; no need to close and open a window
        namefile = open('test.txt', 'r')
        names = namefile.readlines()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    if event.unicode == 3:
                        name += 0
                    else:
                        name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_RETURN:
                    f = open("test.txt", "a")
                    f.write(str(name) + " " + str(lol) + "\n")
                    f.close()
                    name = ""
            elif event.type == QUIT:
                return

        #  create a Rectangle container, where yours
        #  text variable will be drawn
        #  Rect(left, top, width, height)
        textrect = Rect(0, 0, 100, FONT_SIZE)
        SURFACE.fill((0, 0, 0))
        for i in names:
            #  iterate through lines from text file (it is stored
            #  in names variable and it is a list)

            #  create text variable and draw it to textrect
            text = font.render(i[:-1], True, (255,0,0), (0,0,0))
            SURFACE.blit(text, textrect)
            #  change y coordinate of textrect; in next iteration
            #  next line will appear below the previous line
            textrect.centery += FONT_SIZE

        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = SURFACE.get_rect().center
        SURFACE.blit(block, rect)
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    name()
    pygame.quit()