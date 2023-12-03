# H, W = map(int, input().split())
# column = [None] * W
# array = []
# cumArray =[]

# for i in range(H):
#     column[i] = list(map(int, input().split()))
#     array.append(column[i])

# Q  = int(input())
# query = [None] * Q
# for j in range(Q):
#     query[j] = list(map(int, input().split()))

# for k in range(H):
#     value = 0
#     cumColumn = []
#     for l in range(W):
#         value = value + array[k][l]
#         cumColumn.append(value)
#     cumArray.append(cumColumn)
    
# for m in range(W):
#     for n in range(1, H):
#         cumArray[n][m] = cumArray[n][m] + cumArray[n-1][m]
# print(cumArray)

# for o in range(Q):
#     if(query[o][0] == 1 and query[o][1] == 1):
#         print(cumArray[query[o][2] - 1][query[o][3] - 1])
#     else:
#         x1 = cumArray[query[o][0] - 2][query[o][1] - 2]
#         x2 = cumArray[query[o][2] - 1][query[o][3] - 1]
#         x3 = cumArray[query[o][0] - 2][query[o][3] - 1]
#         x4 = cumArray[query[o][2] - 1][query[o][1] - 2]
#         print(x2 - x3 - x4 + x1)

# 入力（前半）
H, W = map(int, input().split())
X = [ None ] * (H)
Z = [ [ 0 ] * (W + 1) for i in range(H + 1) ]
for i in range(H):
	X[i] = list(map(int, input().split()))

# 入力（後半）
Q = int(input())
A = [ None ] * Q
B = [ None ] * Q
C = [ None ] * Q
D = [ None ] * Q
for i in range(Q):
	A[i], B[i], C[i], D[i] = map(int, input().split())

# 配列 Z は既に初期化済み
# 横方向に累積和をとる
# X[i-1][j-1] などになっているのは、配列が 0 番目から始まるため
for i in range(1, H+1):
	for j in range(1, W+1):
		Z[i][j] = Z[i][j-1] + X[i-1][j-1]

# 縦方向に累積和をとる
for j in range(1, W+1):
	for i in range(1, H+1):
		Z[i][j] = Z[i-1][j] + Z[i][j]

# 答えを求める
for i in range(Q):
	print(Z[C[i]][D[i]] + Z[A[i]-1][B[i]-1] - Z[A[i]-1][D[i]] - Z[C[i]][B[i]-1])