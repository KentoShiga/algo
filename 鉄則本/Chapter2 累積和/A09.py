H, W, N = map(int, input().split())
query = []
for i in range(0, N):
  A, B, C, D = map(int, input().split())
  query.append([A, B, C, D])
# print(query)

cumSumArray = [[0 for i in range(0, W + 2)] for j in range(0, H + 2)]

for i in range(0, N):
  cumSumArray[query[i][0]][query[i][1]] += 1
  cumSumArray[query[i][0]][query[i][3] + 1] -= 1
  cumSumArray[query[i][2]][query[i][1]] -= 1
  cumSumArray[query[i][2] + 1][query[i][3] + 1] += 1

for i in range(1, H + 1):
  for j in range(1, W + 1):
    cumSumArray[i][j] += cumSumArray[i][j - 1]

for i in range(1, W + 1):
  for j in range(1, H + 1):
    cumSumArray[j][i] += cumSumArray[j - 1][i]

# print(cumSumArray)

for i in range(1, H + 1):
  for j in range(1, W + 1):
    print(cumSumArray[i][j], end = " ")
  print()