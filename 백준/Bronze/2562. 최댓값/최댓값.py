import sys
input= sys.stdin.readline
list1 = []
for _ in range(9):
    list1.append(int(input().rstrip()))
print(max(list1))
print(list1.index(max(list1))+1)
