import sys
input = sys.stdin.readline

n = int(input().rstrip())
max = len(str(n))
count = 0
k = 2
while len(str(n)) == max:
    if len(str(n)) > max:
        break
    n *= k
    count += 1
print(count-1)
