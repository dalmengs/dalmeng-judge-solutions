n = int(input()) // 2
m = int(input())
k = list(map(int, input().split()))

t = [[0 for i in range(n)] for j in range(2)]
for i in k:
    x = (i - 1) // 2
    y = (i - 1) % 2
    t[y][x] = 1

INF = 987654321

dp = [[INF for i in range(n)] for j in range(2)]

l, r = 0, n - 1
for i in range(n):
    if t[0][i] == 1 or t[1][i] == 1:
        break
    l += 1
for i in range(n - 1, -1, -1):
    if t[0][i] == 1 or t[1][i] == 1:
        break
    r -= 1

if t[0][l] == t[1][l] == 1:
    dp[0][l] = dp[1][l] = 1
elif t[0][l] == 1 and t[1][l] == 0:
    dp[0][l] = 0
    dp[1][l] = 1
elif t[0][l] == 0 and t[1][l] == 1:
    dp[0][l] = 1
    dp[1][l] = 0

for i in range(l + 1, r + 1):
    if t[1][i] == 1:
        dp[0][i] = min(dp[0][i - 1] + 2, dp[1][i - 1] + 2)
    else:
        dp[0][i] = min(dp[0][i - 1] + 1, dp[1][i - 1] + 2)
    
    if t[0][i] == 1:
        dp[1][i] = min(dp[0][i - 1] + 2, dp[1][i - 1] + 2)
    else:
        dp[1][i] = min(dp[0][i - 1] + 2, dp[1][i - 1] + 1)

print(min(dp[0][r], dp[1][r]))
