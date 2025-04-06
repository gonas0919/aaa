import sys
input= sys.stdin.readline
while True:
    angList = list(map(int, input().rstrip().split()))
    if sum(angList) == 0:
        break
    if sum(angList)-max(angList) > max(angList):
        if len(set(angList)) == 3:
            print('Scalene')
        elif len(set(angList)) == 2:
            print('Isosceles')
        elif len(set(angList)) == 1:
            print('Equilateral')
    else:
        print('Invalid')