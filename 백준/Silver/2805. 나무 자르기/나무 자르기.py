import sys
input = sys.stdin.readline
k,n = map(int, input().rstrip().split())
list1 = list(map(int, input().rstrip().split()))
start = 0
end = max(list1) #(start)1 2 3 4 5(middle) 6 7 8 9 10(END) 만약 미들값보다 
result = 0
while start<=end:
    middle = (start+end)//2
    total = 0
    for i in list1:
        if i > middle:
            total += i-middle
            if total > n:
                break
    if total>=n: #잘라낸 나무가 필요한 나무보다 더큼 >> 기준을 높여야함 14 15
        result = middle
        start = middle + 1
    elif total<n:
        end = middle -1
print(result)
