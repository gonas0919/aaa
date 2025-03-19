import sys
input= sys.stdin.readline
how = int(input())
start = 1
score = 0
scoreL = []
for _ in range(how):
    ask = list(input().rstrip())
    for i in ask:
        if i == 'O':
            score += 1*start
            start += 1
        elif i == 'X':
            start = 1
    start = 1

    scoreL.append(score)
    score = 0
for i in scoreL:
    print(i)