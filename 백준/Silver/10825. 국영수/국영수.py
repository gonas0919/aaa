import sys
input=sys.stdin.readline
how = int(input().rstrip())
list1 = []
for _ in range(how):
    name, ko, eng, mat = input().rstrip().split()
    list2 = [name, int(ko), int(eng), int(mat)]
    list1.append(list2)
result = sorted(list1, key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in result:
    print(i[0])
