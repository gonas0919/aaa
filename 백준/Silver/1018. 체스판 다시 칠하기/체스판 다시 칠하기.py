import sys
input = sys.stdin.readline
n , m = map(int, input().rstrip().split())
bg = [input().rstrip() for _ in range(n)]
rwbg = ['WBWBWBWB','BWBWBWBW']*4
rbbg = ['BWBWBWBW', 'WBWBWBWB']*4
miin = 64
for i in range(n-7): #6
    for j in range(m-7): # 3
        c1 = 0
        c2 = 0
        for x in range(8):
            for y in range(8):
                if bg[i+x][j+y] != rwbg[x][y]:
                    c1 += 1
                if bg[i+x][j+y] != rbbg[x][y]:
                    c2 += 1
        miin = min(miin, c1,c2)
print(miin)