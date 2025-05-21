import sys
input = sys.stdin.readline

def func(list1):
    a = len(list1)
    dp = [1] * a #10 20 10 30 20 50
    for i in range(a): #6
        for j in range(i): 
            if list1[j] < list1[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
b = int(input().rstrip())
list1 = list(map(int, input().rstrip().split()))
print(func(list1)) 