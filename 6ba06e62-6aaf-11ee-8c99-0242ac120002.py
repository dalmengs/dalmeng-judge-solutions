a, b = map(int, input().split())
x = int(input())

INF = 987654321

dp = [INF for i in range(x + 1)]
dp[x] = 0

for i in range(x, 0, -1):
    # Skill 1
    y = min(i // 2 + a, x)
    if 0 <= y <= x:
        dp[y] = min(dp[y], dp[i] + 1)
    
    # Skill 2
    y = max(i - a, 0)
    if 0 <= y <= x:
        dp[y] = min(dp[y], dp[i] + 1)

print(max(0, b - dp[0] * a))
