import sys
from math import sqrt
from random import randint
import pygame
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_SPACE, K_UP, K_z
from getloc import *
from util.getloc2 import getloc2
from screen1 import *
from screen3 import *
from save_info import *
BLOCK_DATA = (
    (
        (0, 0, 1, \
         1, 1, 1, \
         0, 0, 0),
        (0, 1, 0, \
         0, 1, 0, \
         0, 1, 1),
        (0, 0, 0, \
         1, 1, 1, \
         1, 0, 0),
        (1, 1, 0, \
         0, 1, 0, \
         0, 1, 0),
    ), (
        (2, 0, 0, \
         2, 2, 2, \
         0, 0, 0),
        (0, 2, 2, \
         0, 2, 0, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 2, \
         0, 0, 2),
        (0, 2, 0, \
         0, 2, 0, \
         2, 2, 0)
    ), (
        (0, 3, 0, \
         3, 3, 3, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 3, 0),
        (0, 0, 0, \
         3, 3, 3, \
         0, 3, 0),
        (0, 3, 0, \
         3, 3, 0, \
         0, 3, 0)
    ), (
        (4, 4, 0, \
         0, 4, 4, \
         0, 0, 0),
        (0, 0, 4, \
         0, 4, 4, \
         0, 4, 0),
        (0, 0, 0, \
         4, 4, 0, \
         0, 4, 4),
        (0, 4, 0, \
         4, 4, 0, \
         4, 0, 0)
    ), (
        (0, 5, 5, \
         5, 5, 0, \
         0, 0, 0),
        (0, 5, 0, \
         0, 5, 5, \
         0, 0, 5),
        (0, 0, 0, \
         0, 5, 5, \
         5, 5, 0),
        (5, 0, 0, \
         5, 5, 0, \
         0, 5, 0)
    ), (
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6),
        (6, 6, 6, 6)
    ), (
        (0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0, \
         0, 7, 0, 0),
        (0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0, \
         0, 0, 7, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         7, 7, 7, 7, \
         0, 0, 0, 0)
    )
)

class Block:
    """ 블록 객체 """
    def __init__(self, count):
        self.turn = 0 #시간표 모양을 보여주기 위해서 초기 turn 값은 0으로 고정
        #self.turn = randint(0, 3)
        self.type = BLOCK_DATA[randint(0, len(BLOCK_DATA)-1)]
        #self.type = BLOCK_DATA[1]
        self.data = self.type[self.turn]
        self.size = int(sqrt(len(self.data)))
        self.xpos = 1
        self.ypos = 1 - self.size + 4 #필드에서 벗어나지 않도록 시작 위치를 아래로 내림
        self.fire = count + INTERVAL

    def update(self, count):
        """ 블록 상태 갱신 (소거한 단의 수를 반환한다) """
        # 아래로 총돌?
        erased = 0
        if is_overlapped(self.xpos, self.ypos + 1, self.turn):
            for y_offset in range(BLOCK.size):
                for x_offset in range(BLOCK.size):
                    if 0 <= self.xpos+x_offset < WIDTH and 0 <= self.ypos+y_offset < HEIGHT:
                        val = BLOCK.data[y_offset*BLOCK.size + x_offset]
                        if val != 0:
                            FIELD[self.ypos+y_offset][self.xpos+x_offset] = val
            erased = erase_line()
            go_next_block(count)

        if self.fire < count:
            self.fire = count + INTERVAL
            self.ypos += 1
        return erased

    def draw(self):
        """ 블록을 그린다 """
        for index in range(len(self.data)):
            xpos = index % self.size
            ypos = index // self.size
            val = self.data[index]
            if 0 <= ypos + self.ypos < HEIGHT and 0 <= xpos + self.xpos < WIDTH and val != 0:
                x_pos = BLOCK_SIZE + (xpos + self.xpos) * BLOCK_SIZE
                y_pos = BLOCK_SIZE + (ypos + self.ypos) * BLOCK_SIZE
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (x_pos, y_pos, BLOCK_SIZE-1, BLOCK_SIZE-1))

def erase_line():
    """ 행이 모두 찬 단을 지운다 """
    erased = 0
    ypos = HEIGHT-2
    while ypos >= 0:
        if all(FIELD[ypos]):
            erased += 1
            del FIELD[ypos]
            FIELD.insert(0, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        else:
            ypos -= 1
    return erased

def is_game_over():
    """ 게임 오버인지 아닌지 """
    filled = 0
    for cell in FIELD[0]:
        if cell != 0:
            filled += 1
    return filled > 2   # 2 = 좌우의 벽

def go_next_block(count):
    """ 다음 블록으로 전환한다 """
    global BLOCK, NEXT_BLOCK
    BLOCK = NEXT_BLOCK if NEXT_BLOCK != None else Block(count)
    NEXT_BLOCK = Block(count)

def is_overlapped(xpos, ypos, turn):
    """ 블록이 벽이나 땅의 블록과 충돌하는지 아닌지 """
    data = BLOCK.type[turn]
    for y_offset in range(BLOCK.size):
        for x_offset in range(BLOCK.size):
            if 0 <= xpos+x_offset < WIDTH and 0 <= ypos+y_offset < HEIGHT:
                if data[y_offset*BLOCK.size + x_offset] != 0 and FIELD[ypos+y_offset][xpos+x_offset] != 0:
                    return True
    return False

# 전역 변수

WIDTH = 12
HEIGHT = 32
INTERVAL = 80
FIELD = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
COLORS = ((0, 0, 0), (128, 128, 128), (205, 116, 102),(204, 168, 92), (76, 62, 34),
        (255, 165, 0), (0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 0, 255),
        (69, 36, 59), (231, 255, 0), (2, 208, 178), (57, 16, 81), (6, 38, 22),
        (161, 217, 126), (254, 198, 103), (255, 113, 103), (162, 151, 1), (200, 120, 183),
        (164, 75, 0), (189, 217, 158), (254, 190, 240), (102, 173, 255), (249, 246, 113),
        (255, 174, 207), (5, 26, 100), (0, 111, 53), (171, 228, 213), (124, 154, 126),
        (167, 202, 109), (137, 116, 193), (106, 142, 202), (110, 180, 166), (255, 178, 126),
        (255, 0, 0))
BLOCK = None
BLOCK_SIZE = 20
NEXT_BLOCK = None
cur_lecture = []


def tetris_game(cur_lecture):
    SURFACE = pygame.display.set_mode([600, 800])
    pygame.init()
    pygame.key.set_repeat(120, 120)
    SURFACE = pygame.display.set_mode([600, 800])
    FPSCLOCK = pygame.time.Clock()
    k_font = pygame.font.SysFont('malgungothic', 20)
    """ 메인 루틴 """
    global INTERVAL
    count = 0
    score = 0
    game_over = False
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_over = largefont.render("GAME OVER!!",
                                    True, (0, 255, 225))
    message_rect = message_over.get_rect()
    message_rect.center = (300, 300)

    go_next_block(INTERVAL)

    for ypos in range(HEIGHT):
        for xpos in range(WIDTH):
            FIELD[ypos][xpos] = 1 if xpos == 0 or xpos == WIDTH - 1 else 0
    for index in range(WIDTH):
        FIELD[HEIGHT-1][index] = 1

    while True:
        key = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key

        game_over = is_game_over()
        if not game_over:
            count += 5
            if count % 1000 == 0:
                INTERVAL = max(1, INTERVAL - 2)
            erased = BLOCK.update(count)

            if erased > 0:
                score += (2 ** erased) * 100

            # 키 이벤트 처리
            next_x, next_y, next_t = \
                BLOCK.xpos, BLOCK.ypos, BLOCK.turn
            if key == K_UP:
                next_t = (next_t + 1) % 4
            elif key == K_z:
                next_t = (next_t - 1) % 4
            elif key == K_RIGHT:
                next_x += 1
            elif key == K_LEFT:
                next_x -= 1
            elif key == K_DOWN:
                next_y += 1


            if not is_overlapped(next_x, next_y, next_t):
                BLOCK.xpos = next_x
                BLOCK.ypos = next_y
                BLOCK.turn = next_t
                BLOCK.data = BLOCK.type[BLOCK.turn]

        # 전체&낙하 중인 블록 그리기
        SURFACE.fill((0, 0, 0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                val = FIELD[ypos][xpos]
                pygame.draw.rect(SURFACE, COLORS[val],
                                 (xpos*BLOCK_SIZE + BLOCK_SIZE, ypos*BLOCK_SIZE + BLOCK_SIZE, BLOCK_SIZE-1, BLOCK_SIZE-1))
        BLOCK.draw()

        temp = 0
        # 다음 블록 그리기
        for ypos in range(NEXT_BLOCK.size):
            for xpos in range(NEXT_BLOCK.size):
                val = NEXT_BLOCK.data[xpos + ypos*NEXT_BLOCK.size]
                temp = max(temp, val)
                pygame.draw.rect(SURFACE, COLORS[val], (xpos*BLOCK_SIZE + 460, ypos*BLOCK_SIZE + BLOCK_SIZE*4, BLOCK_SIZE-1, BLOCK_SIZE-1))

        # 점수 나타내기
        score_str = str(temp).zfill(6)
        score_image = smallfont.render(score_str, True, (0, 255, 0))
        SURFACE.blit(score_image, (500, 30))

        lec_name_str = str(cur_lecture[temp - 3].name)
        lec_name_image = k_font.render(lec_name_str, True, (0, 255, 0))

        lec_professor_str = str(cur_lecture[temp - 3].professor)
        lec_professor_image = k_font.render(lec_professor_str, True, (0, 255, 0))

        SURFACE.blit(lec_name_image, (375, 240))
        SURFACE.blit(lec_professor_image, (375, 300))

        if game_over:
            SURFACE.blit(message_over, message_rect)

        pygame.display.update()

        # 게임 속도 조절 및 중복 입력 방지
        FPSCLOCK.tick(60)


def game_personal(id, pw):
    #개인모드
    global BLOCK_DATA
    #get_block_personal(id, pw) 이 부분에 UI에서 받아온 값을 넣어야함.
    cur_lecture, _BLOCK_DATA = get_blocks_personal(id, pw)
    BLOCK_DATA = _BLOCK_DATA
    tetris_game(cur_lecture)

def game_competition(info = 1):
    #경쟁모드
    #get_blocks_competition(id) 에서 id에 UI에서 받아온 값을 넣어야함. 1~4임
    global BLOCK_DATA
    cur_lecture, _BLOCK_DATA = get_blocks_competition(info)
    print(_BLOCK_DATA)
    BLOCK_DATA = _BLOCK_DATA
    tetris_game(cur_lecture)

if __name__ == '__main__':
    #강의 정보 불러오기
    tetris_game(get_blocks_competition(1)[0])
