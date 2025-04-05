import sys
input= sys.stdin.readline
num1 = int(input().rstrip())
numList = []
a = 2
while num1 > 1:
    if num1%a == 0:
        numList.append(a)
        num1 = num1//a
    elif num1%a !=0:
        a +=1
for i in numList:
    print(i)