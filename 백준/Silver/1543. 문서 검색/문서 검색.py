import sys
input= sys.stdin.readline
ask = input().rstrip()
what = input().rstrip()
how = 0
while what in ask:
    how += 1
    ask = ask[ask.index(what)+len(what):]
print(how)