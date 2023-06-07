from array import *
stu_roll = array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
# while i<n:
#     print(stu_roll[i])
#     i +=1

print("array after insert")
stu_roll.insert(1, 106)
stu_roll.insert(3, 107)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i += 1

# print("배열 요소 삭제")
# stu_roll.remove(107)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i]);
#     i += 1;

print("배열 요소 삭제 pop() 함수")
element = stu_roll.pop()
print('element', element)
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i]);
    i += 1;
