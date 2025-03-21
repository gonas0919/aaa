N = int(input())
l = list(map(int, input().split()))
totalscore= 0
maxscore = max(l)
for i in range(len(l)):
    l[i] = (l[i]/maxscore)*100
    totalscore += l[i]
print(totalscore/N)