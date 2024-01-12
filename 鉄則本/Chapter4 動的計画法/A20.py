S = input()
T = input()

dp = [ [ 0 for i in range(len(T) + 1)] for j in range(len(S) + 1)]

for i in range(len(T) + 1):
    dp[0][i] = 0
    dp[i][0] = 0

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if(S[i - 1] == T[j - 1]):
            dp[i][j] = max(dp[i][j - 1] + 1, dp[i - 1][j])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp)

print(dp[len(S)][len(T)])


#これはひとつ上の値をコピーした場合が左の値をコピーした場合よりも大きい場合が考慮されていない
# for i in range(1, len(S) + 1):
#     for j in range(1, len(T) + 1):
#         dp[i][j] = dp[i - 1][j]
#         if(S[i - 1] == T[j - 1]):
#                 dp[i][j] = dp[i][j - 1] + 1
#         else:
#             dp[i][j] = dp[i][j - 1]
#         print(dp)

# print(dp[len(S)][len(T)])