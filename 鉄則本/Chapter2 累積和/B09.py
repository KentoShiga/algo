N = int(input())
mapArray = [[0 for i in range(0, 1503)] for j in range(0, 1503)]
# mapArray = [[0 for i in range(0, 10)] for j in range(0, 10)]


targetArray = []
for i in range(0, N):
    a, b, c, d = map(int, input().split())
    targetArray.append([a + 1, b + 1, c + 1, d + 1])

for i in range(0, N):
    mapArray[targetArray[i][0]][targetArray[i][1]] += 1
    mapArray[targetArray[i][0]][targetArray[i][3]] -= 1
    mapArray[targetArray[i][2]][targetArray[i][1]] -= 1
    mapArray[targetArray[i][2]][targetArray[i][3]] += 1

for i in range(1, 1502):
    for j in range(1, 1502):
        mapArray[i][j] += mapArray[i][j - 1]

for i in range(1, 1502):
    for j in range(1, 1502):
        mapArray[i][j] += mapArray[i - 1][j]

# for i in range(0, 10):
#   for j in range(0, 10):
#     mapArray[i][j] += mapArray[i][j - 1]

# for i in range(0, 10):
#   for j in range(0, 10):
#     mapArray[i][j] += mapArray[i - 1][j]

# print(mapArray)

squareCount = 0
for i in range(1, 1502):
    for j in range(1, 1502):
        if mapArray[i][j] > 0:
            squareCount += 1
print(squareCount)
