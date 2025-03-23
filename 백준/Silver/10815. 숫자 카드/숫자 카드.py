import sys
input= sys.stdin.readline
how= int(input().rstrip())
card= list(map(int, input().rstrip().split()))
how= int(input().rstrip())
card1= list(map(int, input().rstrip().split()))
card2 = {}
card3 = {}
for i in card:
    card2[i] = i
for i in card1:
    card3[i] = i
for i in card3.keys():
    if i in card2:
        card3[i] = 1
    else:
        card3[i] = 0
for i in card3.values():
    print(i, end=' ')
