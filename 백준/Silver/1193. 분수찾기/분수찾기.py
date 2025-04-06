import sys
input = sys.stdin.readline
num = int(input().rstrip())
a = 1
b = 1
count = 1
while num>a:
    num -=a
    count+=1
    a+=1
if count%2 == 0:
    for _ in range(1,num):
        count -=1
        b +=1
    print(f'{num}/{count}')
elif count%2 != 0:
    for _ in range(1,num):
        count -=1
        b +=1
    print(f'{count}/{num}')