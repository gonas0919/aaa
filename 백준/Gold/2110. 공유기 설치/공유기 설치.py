import sys
input=sys.stdin.readline
how, c = map(int,input().rstrip().split())
list1 = [int(input().rstrip()) for i in range(how)]
list1.sort()
a = 1 # 1
b = max(list1) - min(list1)
result = 0
while a<=b:
    middle = (a+b)//2 #4
    count = 1
    where = list1[0]
    for i in range(1,how):
        if list1[i]-where >= middle:
            count += 1
            where = list1[i]
    if count >= c: #탐색이 더 많음. 시작위치 변경
        result = middle
        a = middle + 1
    else: #더 작으면 거리 좁혀
        b = middle -1
print(result)
