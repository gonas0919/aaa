import sys
input=sys.stdin.readline
how, num = map(int, input().rstrip().split())
list1 = list(map(int, input().rstrip().split()))
list1.sort(reverse=True) #9 8 7 6 5
total = 0 # - - -
list2 = []
for i in range(how): #
    for j in range(i+1,how):
        for m in range(j+1,how):
            if list1[i]+list1[j]+list1[m]<=num:
                list2.append(list1[i]+list1[j]+list1[m])
print(max(list2))