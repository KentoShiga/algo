N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ 0 for i in range(N)]

dp[0] = 0
dp[1] = A[0]

root = []
root.append(N)

for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])
# print(dp[N - 1])

j = N - 1

while j > 0:
    if dp[j] == dp[j - 1] + A[j - 1]:
        root.append(j)
        j -= 1
    else:
        root.append(j - 1)
        j -= 2
print(len(root))
for i in range(len(root)):
    print(root[len(root) - 1 - i], end = " ")
print()