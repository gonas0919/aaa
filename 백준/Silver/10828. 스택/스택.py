import sys
input = sys.stdin.readline
stack = []
how = int(input().rstrip())
for _ in range(how):
    ask = input().split()
    if ask[0] == 'push':
        stack.append(ask[1])
    elif ask[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)
    elif ask[0] == 'size':
        print(len(stack))
    elif ask[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ask[0] == 'top':
        if len(stack) >= 1:
            print(stack[-1])
        if len(stack) == 0:
            print(-1)
