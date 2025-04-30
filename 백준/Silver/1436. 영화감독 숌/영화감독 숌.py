import sys
input = sys.stdin.readline
how = int(input())
new = 0
new1 = 0
while True:
    if '666' in str(new):
        new1 += 1
        if new1 == how:
            break
    new += 1
print(new)