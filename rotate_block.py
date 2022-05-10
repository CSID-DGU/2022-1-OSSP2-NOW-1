'''
정사각형 배열을 회전시키거나, 해당 배열의 1차원 및 2차원 좌표 변환 기능을 제공하는 모듈
'''

from math import sqrt
# 한쪽 길이는 3/4/5 중 하나

class NotSquareError(Exception):
    '''
    @desc 배열이 정사각형이 아닐때 발생하는 오류
    '''
    def __init__(self):
        super().__init__('배열이 정사각형이 아닙니다.')

def check_square(row_len: int, length: int):
    '''
    @desc 배열이 정사각형인지 검사.
    @input row_len 배열의 한 변 길이 (get_row로 구함)
    @input length 배열 전체의 길이
    @error 정사각형 배열이 아닌 경우
    '''
    if row_len**2 != length:
        raise NotSquareError

def get_row(length: int):
    '''
    @desc 배열에 대해 정사각형의 한변 길이 반환
    @input length 배열 전체의 길이 (파이썬 len 함수의 결과)
    @error 정사각형 배열이 아닌 경우
    @return 정사각형 한변의 길이
    '''
    row_len = int(sqrt(length))
    check_square(row_len, length)
    return row_len


def print_square(arr: tuple):
    '''
    @desc 정사각형 모양 출력
    @arr 대상 배열 
    @error 정사각형 배열이 아닌 경우
    '''
    row_len = get_row(len(arr))

    for i in range(0, len(arr), row_len):
        print(arr[i:i+row_len], sep='\t')
    print()

def idx2loc(row: int, col: int, row_len: int):
    '''
    @desc 2차원 배열 기준 인덱스를 1차원 배열의 인덱스로 변환
    @input row 1차원 기준 x 좌표
    @input col 1차원 기준 y 좌표
    @input row_len 정사각형의 한변 길이
    @return 1차원 배열 형태에서의 인덱스
    '''
    return row * row_len + col


def loc2idx(loc: int, row_len: int):
    '''
    @desc 1차원 배열 기준 인덱스를 2차원 배열의 인덱스로 변환
    @input loc 1차원 배열 기준 인덱스
    @input row_len 정사각형 한 변 길이. (get_row로 구함)
    @return 2차원 배열 형태의 인덱스
    '''
    row = int(loc / row_len)
    col = loc % row_len
    return (row, col)

def cc_rotate(arr: tuple):
    '''
    @desc 배열을 반시계방향으로 회전
   
    for i = 0 ~ len
      for j = 0 ~ len
          dest[len - 1 - j, i] = arr[i, j]
    @input 대상 배열
    @error 정사각형 배열이 아닌 경우
    @return 반시계 방향으로 회전한 배열
    '''
    
    row_len = get_row(len(arr))
    ri = row_len - 1 # for문마다 1씩 빼기 싫어서 추가한 변수

    dest = [0 for _ in range(len(arr))]  # 리턴 대상 배열

    for i in range(0, row_len):
        for j in range(0, row_len):
            dest[idx2loc(ri - j, i, row_len)] = arr[idx2loc(i, j, row_len)]
    return dest

def c_rotate(arr: tuple):
    '''
    @desc 배열을 시계방향으로 회전  
    
    for i = 0 ~ len
      for j = 0 ~ len
          dest[j, len - i - 1] = arr[i, j]
    @input 대상 배열
    @error 정사각형 배열이 아닌 경우
    @return 반시계 방향으로 회전한 배열
    '''
    row_len = get_row(len(arr))
    ri = row_len - 1

    dest = [0 for _ in range(len(arr))]  # 대상 배열

    for i in range(0, row_len):
        for j in range(0, row_len):
            dest[idx2loc(j, ri - i, row_len)] = arr[idx2loc(i, j, row_len)]
    return dest

'''
if __name__ == '__main__':
    fig1 = [i for i in range(0, 9)]
    fig2 = [i for i in range(0, 16)]
    fig3 = [i for i in range(0, 25)]

    fig12 = c_rotate(fig1)
    # 3 X 3 블럭
    print_square(fig1)
    print_square(fig12)

    fig22 = c_rotate(fig2)
    # 4 X 4 블럭
    print_square(fig2)
    print_square(fig22)

    fig32 = c_rotate(fig3)
    # 5 x 5 블럭
    print_square(fig3)
    print_square(fig32)
    # 이론상 모든 정사각형 배열에 대해 사용 가능.
'''

def rotate_block(fig: list) :
    return c_rotate(fig)
