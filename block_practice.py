import numpy as np
#튜플 연산불가
# 리스트형, 근데 2배씩 하면 이렇게 계속 진행해도 되는가
data_list = [[0, 4.0, 5.0], [2, 3.0, 4.0]]
print("Data List", str(data_list))
# code to split it into 3 lists (요일리스트, 시작교시리스트, 끝교시리스트)
day_b = [i[0] for i in data_list]
sts = [i[1] for i in data_list]
end = [i[2] for i in data_list]

print("Day", str(day_b))
print("aclass",str(sts))
print("bclass",str(end))

#정사각형 배열 만들기
height = day_b[1]-day_b[0]+1
if end[0]-sts[0] > end[1]-sts[1] :
    width = end[0]-sts[0]
else:
    width = end[1]-sts[1]
# 0벡터 만들기
if height > width :
  basic = np.zeros((height,height))
  print(basic)
else :
    basic = np.zeros((width,width))
    print(basic)




#def square(height):
 #   if height == 2 :
  #      block=
  #  elif height ==3:

   # elif height==4:

    #elif height==5:

  #  else:

