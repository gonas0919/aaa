import sys
input = sys.stdin.readline
how = int(input().rstrip())
for _ in range(how):
    w_len = int(input().rstrip())
    fs_key = list(map(str, input().rstrip().split()))
    sc_key = list(map(str, input().rstrip().split()))
    sk_key = list(map(str, input().rstrip().split()))
    sc_key2 = []
    for i in sc_key:
        a = fs_key.index(i)
        sc_key2.append([i,a])
    sk_key2 = []
    for i in range(w_len):
        sk_key2.append([sk_key[i],sc_key2[i][1]])
    sk_key2.sort(key=lambda x: x[1])
    for i in range(w_len):
        print(sk_key2[i][0], end=' ')
    print()