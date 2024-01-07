def printer(second, A):
    printNum = 0
    for i in range(len(A)):
        printNum += second  // A[i]
    return printNum

N, K = map(int, input().split())
A = list(map(int, input().split()))
right = 10 ** 9
left = 1

for i in range(30):
    second = (right + left) // 2
    printNum = printer(second, A)
    if(printNum < K):
        left = second + 1
    else:
        right = second

print(right)