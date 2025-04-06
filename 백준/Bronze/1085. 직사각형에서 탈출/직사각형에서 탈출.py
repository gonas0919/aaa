import sys
input= sys.stdin.readline
num1 = list(map(int, input().rstrip().split()))
list1 = []
list1.append(min(num1))
list1.append(num1[2]-num1[0])
list1.append(num1[3]-num1[1])
print(min(list1))
