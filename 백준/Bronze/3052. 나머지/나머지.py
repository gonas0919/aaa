a = set()
for i in range(1,11):
    b = int(input())
    c = b%42
    a.add(c)
print(len(a))