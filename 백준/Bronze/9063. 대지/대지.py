import sys
input= sys.stdin.readline
how = int(input().rstrip())
list1 = [list(map(int, input().rstrip().split())) for _ in range(how)]
list2 = [i[0] for i in list1]
list3 = [i[1] for i in list1]
x = max(list2)-min(list2)
y = max(list3)-min(list3)
print(x*y)