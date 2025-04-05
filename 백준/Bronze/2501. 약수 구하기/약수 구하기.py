import sys
input= sys.stdin.readline
list1 = []
num1, num2 = map(int, input().rstrip().split())
for i in range(1,num1+1):
    if num1%i == 0:
        list1.append(i)
try:
    print(list1[num2-1])
except IndexError:
    print(0)