n = int(input())
heights = list(map(int, str(input()).split()))
widths = list(map(int, str(input()).split()))
area = 0
i = 0

for h1, h2 in zip(heights, heights[1:]):
    area += widths[i]*(h1 + h2)/2
    i+=1

print(area)
