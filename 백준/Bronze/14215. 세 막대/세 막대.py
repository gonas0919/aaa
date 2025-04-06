import sys
input= sys.stdin.readline
angList = list(map(int, input().rstrip().split()))
if sum(angList)-max(angList) <= max(angList):
    angList[angList.index(max(angList))] = sum(angList)-max(angList)-1
print(sum(angList))
