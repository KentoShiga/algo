N = int(input())
A = list(map(int, input().split()))
B = A.copy()
B.sort()

setB = set(B)
dicB = {}
Answer = []
for i, item in enumerate(setB):
    dicB[item] = i + 1

for i in range(N):
    print(dicB[A[i]], end = " ")
print()