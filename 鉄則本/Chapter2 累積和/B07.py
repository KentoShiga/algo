T = int(input())
N = int(input())
cumSum = [0] * (T + 1)

for i in range(N):
    start, end = map(int, input().split())
    cumSum[start] += 1
    cumSum[end] -= 1
    
for k in range(T):
    if(k == 0):
       print(cumSum[k])
    else:
        cumSum[k] = cumSum[k] + cumSum[k - 1]
        print(cumSum[k])