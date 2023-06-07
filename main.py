from array import *

stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])


print("배열 슬라이싱")

n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

a = stu_roll[1:5]
for i in a:
    print(i)

# 0~
a = stu_roll[0:]
for i in a:
    print(i)

# ~5
a = stu_roll[:5]
for i in a:
    print(i)

# 마지막 4개
d = stu_roll[-4:]
for i in d:
    print(i)

# 0~6 2개씩 건너뛰며
e = stu_roll[0:7:2]
for i in e:
    print(i)

# 마지막 5개중 오른쪽으로부터 2개의 요소를 출력 [-5-(-3)]
f = stu_roll[-5:-3 ]