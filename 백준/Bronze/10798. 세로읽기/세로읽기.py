A = []
for i in range(5):
    a = list(map(str, input()))
    A.append(a)
for i in range(15):
    for j in range(5):
        try:
            print(A[j][i], end='')
        except IndexError:
            print('' ,end='')