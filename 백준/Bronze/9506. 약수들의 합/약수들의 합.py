import sys
input= sys.stdin.readline
dict1 = {}
while True:
    num1= int(input().rstrip())
    
    for i in range(1,num1):
        if num1 % i == 0:
            dict1[i] = i
    if num1 == -1:
        break
    elif num1 == sum(dict1.values()): 
        print(f'{num1} = ', end='')
        result = ' + '.join(str(i) for i in dict1.values())
        print(result)
    elif num1 != sum(dict1.values()):
        print(f'{num1} is NOT perfect.')
    dict1.clear()
