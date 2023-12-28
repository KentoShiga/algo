##これだとTLEになる
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# i = N // 2

# while True:
#   if(A[i] == X):
#     #何番目かなので出力はインデックス+1
#     print(i + 1)
#     break
#   elif (A[i] > X):
#     i = i // 2
#   else:
#     i = (N + i) // 2

N, X = map(int, input().split())
A = list(map(int, input().split()))

def serch(x, N, Array):
  while True:
    if(Array[N // 2] == x):
      return N // 2
    elif (Array[N // 2] > x):
      N = N // 2
    else:
      N = (N + N // 2) // 2

print(serch(X, N, A) + 1)