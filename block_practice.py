#튜플 연산불가
# 리스트형
data_list = [[0, 4.0, 5.0], [2, 3.0, 4.0]]
print("Data List", str(data_list))
# code to split it into 3 lists (요일리스트, 시작교시리스트, 끝교시리스트)
day_b = [i[0] for i in data_list]
sts = [i[1] for i in data_list]
end = [i[2] for i in data_list]

print("Day", str(day_b))
print("aclass",str(sts))
print("bclass",str(end))

height = day_b[1]-day_b[0]
 ##비교하기부터



# printing result




