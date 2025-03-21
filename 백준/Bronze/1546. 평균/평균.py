import sys
input= sys.stdin.readline
total = 0
how = int(input().rstrip())
list1 = list(map(int, input().rstrip().split()))
newList = [x/max(list1)*100 for x in list1]
for i in newList:
    total += i
print(total/how)
