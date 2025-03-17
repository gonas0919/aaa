import math
how = int(input())
dot = 2
for i in range(1,how+1):
    dot = math.sqrt((dot+(dot-1)) **2)
print(int(dot**2))