n = int(input())
up, down = input(), input()

maxH = [[0 for i in range(n)] for j in range(2)]

for i in range(1, n):
    if up[i] == "1" or up[i] == "2":
        maxH[0][i] = maxH[0][i - 1] + 1
    if down[i] == "1" or down[i] == "2":
        maxH[1][i] = maxH[1][i - 1] + 1

INF = 987654321
dp = [[[INF for i in range(141)] for k in range(n)]  for j in range(2)]

dp[0][0][0] = dp[1][0][0] = 1
for i in range(n):
    # 윗줄
    for j in range(141):
        # 대각선에서 오는 경우
        if i - 1 >= 0:
            # 윗줄
            if up[i] == "2" or up[i] == "3":
                dp[0][i][0] = min(dp[0][i][0], dp[1][i - 1][j] + 1)
            if up[i] == "1" or up[i] == "2":
                dp[0][i][1] = min(dp[0][i][1], dp[0][i - 1][j] + 1)
            # 아랫줄
            if down[i] == "2" or down[i] == "3":
                dp[1][i][0] = min(dp[1][i][0], dp[0][i - 1][j] + 1)
            if down[i] == "1" or down[i] == "2":
                dp[1][i][1] = min(dp[1][i][1], dp[1][i - 1][j] + 1)
        # 직선에서 오는 경우 & 추진력을 받는 경우 
        if i - j >= 0:
            # 윗줄
            if maxH[0][i] >= j:
                dp[0][i][j] = min(dp[0][i][j], dp[0][i - j][j - 1] + 1)
            # 아랫줄
            if maxH[1][i] >= j:
                dp[1][i][j] = min(dp[1][i][j], dp[1][i - j][j - 1] + 1)

ans = INF
for i in range(141):
    ans = min(ans, dp[0][n - 1][i] + 1, dp[1][n - 1][i] + 1)

print(ans if ans < INF else 0)
