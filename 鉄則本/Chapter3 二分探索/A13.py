def subcom(x, y ,k):
    if(y - x <= 1):
        return True
    else:
        return False
    
N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 1
count = 0

while right - left > 1:
    if(subcom(A[left], A[right], K)):
        count += 1
        if(A[right] < N - 1):
            right += 1
        else:
            break
    else:
        left += 1
        count += right - left + 1
print(count)