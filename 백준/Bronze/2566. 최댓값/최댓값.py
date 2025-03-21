import sys
input= sys.stdin.readline
list1 = [list(map(int, input().rstrip().split())) for _ in range(9)]
maxList = [max(list1[i]) for i in range(9)]
print(max(maxList))
print(maxList.index(max(maxList))+1,list1[maxList.index(max(maxList))].index(max(maxList))+1)
