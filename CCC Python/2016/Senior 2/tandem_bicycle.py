question = int(input())
n = int(input())

dmojSpeeds = list(map(int, str(input()).split()))
pegSpeeds = list(map(int, str(input()).split()))

dmojSpeeds.sort()
pegSpeeds.sort()

if question == 1:
    minPairs = list(zip(dmojSpeeds, pegSpeeds))
    minSum = 0
    for i in minPairs:
        minSum += max(i)
    print(minSum)

if question == 2:
    pegSpeeds.sort(reverse=True)
    maxPairs = list(zip(dmojSpeeds, pegSpeeds))
    maxSum = 0
    for i in maxPairs:
        maxSum += max(i)
    print(maxSum)
