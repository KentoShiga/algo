#そもそもこの解放が思いつかなかった
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [ [ 0 for i in range(S + 1)] for j in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = True

for i in range(1, S + 1):
    dp[0][i] = False

for i in range(1, N + 1):
    for j in range(1, S + 1):
        if j - A[i - 1] < 0:
            if(dp[i - 1][j]):
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            #dp[i - 1][j - A[i - 1]]が悩んだ
            #なぜA[i - 1]なのか：例えば1行目はA[0]を使っているように、i行目はA[i - 1]を使っているから。j - A[i - 1]はその前のカードまででj - A[i - 1]を作れるかどうかを判定している
            if(dp[i - 1][j] or dp[i - 1][j - A[i - 1]]):
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S]:
    print("Yes")
else:
    print("No")