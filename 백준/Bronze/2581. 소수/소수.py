import sys
input= sys.stdin.readline
num1 = int(input().rstrip())
num2 = int(input().rstrip())
count = 0
total = 0
numList = []
for i in range(num1, num2+1):
    for j in range(1,i+1):
        if i%j == 0:
            count+=1
    if count == 2:
        total += 1
        numList.append(i)
    count = 0
if total != 0:
    print(sum(numList))
    print(min(numList))
else:
    print(-1)