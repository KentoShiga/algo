def subcom(x, y ,k):
    if(y - x <= k):
        return True
    else:
        return False
    
N, K = map(int, input().split())
A = list(map(int, input().split()))

right = 0
count = 0

#大事ポイント2：leftを固定してrightを動かす。このときleftは0からN - 2までのN - 1通りの値を取ることは確定なのでループをrange(N - 1)とする
for i in range(N -1):
    left = i
    while right < N - 1 and subcom(A[left], A[right + 1], K):
      right += 1
    #大事ポイント1：right - leftで小さい数がleftのときの組み合わせ数を求められる→条件を満たす最大のrightを求めるプロセスを前に入れる
    count += right - left
print(count)