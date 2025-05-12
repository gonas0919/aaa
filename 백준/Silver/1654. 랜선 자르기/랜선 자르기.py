import sys
input = sys.stdin.readline
k,n = map(int, input().rstrip().split())
list1 = [int(input().rstrip()) for _ in range(k)]
start = 1
end = max(list1)
result = 0
while start<=end:
    middle = (start+end)//2
    total = 0
    for i in list1:
        total += i//middle
    if total >= n: # 구해진게 크면 
        result = middle
        start = middle + 1
    elif total < n:
        end = middle - 1
print(result)