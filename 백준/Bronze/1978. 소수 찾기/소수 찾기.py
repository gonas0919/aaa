import sys
input= sys.stdin.readline
count = 0
total = 0
how  = input().rstrip()
num1= list(map(int, input().rstrip().split()))
for i in num1: # 3 5 7
    if i == 1:
        pass
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        total += 1
    count = 0
print(total)