import sys
input= sys.stdin.readline
ask = list(input().rstrip()) #0011000
how = 0
for i in range(len(ask)-1): #3
    if ask[i] != ask[i+1]: # 1 0
        how += 1
if how == 1:
    print(how)
else:
    print((how+1)//2)