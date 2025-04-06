import sys
input= sys.stdin.readline
angList = []
angList.append(int(input().rstrip()))
angList.append(int(input().rstrip()))
angList.append(int(input().rstrip()))
if sum(angList) == 180:
    if len(set(angList)) == 3:
        print('Scalene')
    elif len(set(angList)) == 2:
        print('Isosceles')
    elif len(set(angList)) == 1:
        print('Equilateral')
else:
    print('Error')

