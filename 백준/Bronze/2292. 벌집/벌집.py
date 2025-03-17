where = int(input()) #13
start = 1
count = 0
mul = 1
while True:
    if where <= start:
        count+=1
        break
    elif where> start:
        start +=6*mul
        count+=1
        mul+=1
        continue
print(count)