import sys
input=sys.stdin.readline
how = int(input().rstrip())
numIndex = 0
list1 = list(map(int, input().rstrip().split()))
new = sorted(list(set(list1))) # 999 1000
dic = {}
for i in range(len(new)):
    dic[new[i]] = i
for i in list1:
    print(dic[i], end = ' ')