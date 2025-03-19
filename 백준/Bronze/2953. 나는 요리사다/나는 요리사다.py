import sys
input= sys.stdin.readline
score = []
value = 0
for _ in range(5):
    p1 = list(map(int, input().rstrip().split()))
    for i in p1:
        value += i
    score.append(value)
    value = 0
print(score.index(max(score))+1 , max(score))