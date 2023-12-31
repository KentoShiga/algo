##これだとTLEになる
#Atcoderはwhile抜き出せないと1000ms制限に引っかかるっぽい
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

# N = 6  のとき i = 3 → A[3]<x のとき i = 4 → A[4]<x のとき i = (4 + 6)//2 = 5

# 修正一回目
# 間違い1：R = mid, L = mid としていた
# これだとN = 6のとき 初期mid = 2 → A[2]<x のとき mid = 3
# → A[3]<x のとき mid = 4 → A[4]<x のとき mid =  4 となり右端に対応できない
# midまで目的の数値がないことが分かっているので、次の探索範囲はmid+1またはmid-1からとなる

# 間違い2：while R  - L > 1: としていた
# これだとL=4, R=5のときなどに対応できない

# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# L = 0
# R = N - 1

# while R  - L > 1:
#   mid = (L + R) // 2
#   if A[mid] == X:
#     break
#   elif A[mid] > X:
#     R = mid
#   else:
#     L = mid

# print(mid + 1)

N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = N - 1

while R >= L:
    mid = (L + R) // 2
    if A[mid] == X:
        break
    elif A[mid] > X:
        R = mid - 1
    else:
        L = mid + 1

print(mid + 1)
