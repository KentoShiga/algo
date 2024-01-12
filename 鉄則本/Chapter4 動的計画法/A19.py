N, W = map(int, input().split())
itemlist = []
dp = [ [ 0 for i in range(W + 1)] for j in range(N + 1)]
for i in range(N):
    w, v = map(int, input().split())
    itemlist.append([w, v])

dp[0][0] = 0
for i in range(1, W + 1):
    dp[0][i] = 0

for i in range(1, N + 1):
    for j in range(W + 1):
        if j - itemlist[i - 1][0] < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            #dp[i - 1][j - itemlist[i - 1][0]](今の商品を入れる前の価値) + itemlist[i - 1][1](今の商品の価値)が悩んだ
            #値段が高い方を選べばよいというロジックも悩んだ
            dp[i][j] = max(dp[i - 1][j],dp[i -1][j - itemlist[i - 1][0]] + itemlist[i - 1][1])

print(max(dp[N]))