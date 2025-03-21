import sys
input= sys.stdin.readline
row, column = map(int,input().rstrip().split())
list1 = [list(map(int, input().rstrip().split())) for _ in range(row)]
list2 = [list(map(int, input().rstrip().split())) for _ in range(row)]
list3 = []
for i in range(row):
    for j in range(column):
        print(list1[i][j]+list2[i][j], end= ' ')
    print()