import sys
input=sys.stdin.readline
num, base = map(int, input().rstrip().split())
sen = ''
bases = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while num>0:
    sen += bases[num%base]
    num //= base

print(sen[::-1])