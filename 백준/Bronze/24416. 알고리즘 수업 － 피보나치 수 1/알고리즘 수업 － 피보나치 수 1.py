import sys
input = sys.stdin.readline

def fib(a):
    list1 = [0] * (a+1)
    list1[1] = 1
    list1[2] = 1
    for i in range(3, a+1):
        list1[i] = list1[i-1] + list1[i-2]
    return list1[i]

a = int(input())
print(fib(a), a-2)