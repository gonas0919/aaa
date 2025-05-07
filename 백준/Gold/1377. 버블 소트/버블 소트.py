import sys
input=sys.stdin.readline

how = int(input())
list1 = []
for i in range(how):
    list1.append([int(input().rstrip()), i])
list2 = sorted(list1, key= lambda x: x[0])
num1 = []
for i in range(how):
    num = list2[i][1]-i+1
    num1.append(num)
print(max(num1))