N = int(input())
Xarray = []
Yarray = []
query = []
column = 0
row = 0
for i in range(0, N):
  X, Y = map(int, input().split())
  Xarray.append(X)
  Yarray.append(Y)

Q = int(input())
for i in range(0, Q):
  a, b, c, d = map(int, input().split())
  query.append([a, b, c, d])
  if(column < c):
    column = c
  if(row < d):
    row = d
  

cumsumArray = [[0 for i in range(0, column + 1)] for j in range(0, row + 1)]

for i in range(0, N):
  cumsumArray[Yarray[i]][Xarray[i]] += 1


for i in range(1, row + 1):
  for j in range(1, column + 1):
    cumsumArray[i][j] += cumsumArray[i][j - 1]

for i in range(1, column + 1):
  for j in range(1, row + 1):
    cumsumArray[j][i] += cumsumArray[j - 1][i]
    
# print(cumsumArray)
    
for i in range(0, Q):
  point1 = cumsumArray[query[i][3]][query[i][2]] + cumsumArray[query[i][1] - 1][query[i][0] - 1]
  point2 = cumsumArray[query[i][3]][query[i][0] - 1] + cumsumArray[query[i][1] - 1][query[i][2]]
  print(point1 - point2)