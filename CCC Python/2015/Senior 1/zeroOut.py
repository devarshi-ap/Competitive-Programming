digits = []
n = int(input())

for i in range(n):
    d = int(input())
    if d != 0:
        digits.append(d)
    else:
        if len(digits) > 0:
            digits.pop()

sum = 0
for i in digits:
    sum += i

print(sum)
