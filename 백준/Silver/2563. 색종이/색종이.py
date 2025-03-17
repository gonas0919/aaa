background = [[0] * 100 for i in range(100)]
how = int(input())
h = 0
total = 0
for i in range(how):
    x , y = map(int,input().split())
    for q in range(y,y+10):
        for p in range(x, x+10): # 3 7
            background[99-q][p] += 1 
for i in background:
    for j in i:
        if j !=0:
            total +=1
        # if j >1:
        #     h +=1
print(total)