import sys
input= sys.stdin.readline
list1 = [list(map(int, input().rstrip().split())) for _ in range(3)]
count = 0
list2 = [i[0] for i in list1]
list3 = [i[1] for i in list1]
x = 0
y = 0
for i in list2:
    if list2.count(i) == 1:
        x = i
for i in list3:
    if list3.count(i) == 1:
        y = i
print(x,y)