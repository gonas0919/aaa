import sys
input= sys.stdin.readline
list1 = [i for i in range(1,31)]
for i in range(28):
    num = int(input().rstrip())
    list1.remove(num)
for i in list1:
    print(i)
