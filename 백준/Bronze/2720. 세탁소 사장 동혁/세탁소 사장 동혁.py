how = int(input())
price = [25 ,10, 5, 1] #Q,D,N,P
time = []
real = []
for i in range(how):
    change = int(input())
    for j in price: #124
        A = change//j
        time.append(A)
        change %= j
    real.append(time)
    time = []
            
for i in real:
    for j in i:
        print(j, end = ' ')
    print()
