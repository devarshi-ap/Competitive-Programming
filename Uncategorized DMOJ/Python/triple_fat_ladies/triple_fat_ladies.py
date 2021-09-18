def findNext(num):
    x = num
    while True:
        cube = x**3
        if str(cube)[-3:] == "888":
            return x
        x += 1

t = int(input())
for i in range(t):
    k = int(input())
    print(findNext(k))
