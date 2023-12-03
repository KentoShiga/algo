N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = [ None ] * Q
R = [ None ] * Q
for j in range(Q):
	L[j], R[j] = map(int, input().split())
S = [None] * (N + 1)
S[0] = 0

# for i in range(1, N + 1):
#   S[i] = sum(S[i - 1] + A[i - 1])
for i in range(N):
	S[i + 1] = S[i] + A[i]

for k in range(Q):
  print(S[R[k]] - S[L[k] - 1])