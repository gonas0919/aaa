import sys
input = sys.stdin.readline

def lis(list1): # 15 11 4 5 8 5 2 4
    n = len(list1)
    dp = [1] * n
    for i in range(n): # 7
        for j in range(i):
            if list1[i] < list1[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

a = int(input())
list1 = list(map(int, input().rstrip().split()))
print(len(list1) - lis(list1))