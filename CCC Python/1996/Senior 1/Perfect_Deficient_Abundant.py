def identify(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print("{x} is a perfect number.".format(x=num))
    elif sum > num:
        print("{x} is an abundant number.".format(x=num))
    else:
        print("{x} is a deficient number.".format(x=num))

t = int(input())
for i in range(t):
    n = int(input())
    identify(n)
