import sys
input= sys.stdin.readline
list1 = [list(input().rstrip()) for _ in range(5)]
maxLen = max([len(list1[i])for i in range(5)])

for i in range(maxLen):
    for j in range(5):
        try:
            print(list1[j][i], end='')
        except IndexError:
            print('', end='')
