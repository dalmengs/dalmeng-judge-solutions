n = int(input())
score = [[False, 0]]

for i in range(n):
    x, y = map(str, input().split())
    if x == "O":
        x = True
    else:
        x = False
    score.append([x, int(y)])

dp = [[0, 0] for _ in range(n + 1)]

# dp[idx][0] : idx번째 문제를 (idx - 1)번째와 안 바꾼 경우 
# dp[idx][1] : idx번째 문제를 (idx - 1)번째와 바꾼 경우

if score[1][0] == True:
    dp[1][0] = score[1][1]
    
for i in range(2, n + 1):
    # 점수를 바꾸지 않는 경우 
    dp[i][0] = max(dp[i - 1][0] + (score[i][1] if score[i][0] else 0), dp[i - 1][1] + (score[i][1] if score[i][0] else 0))

    # 점수를 바꾸는 경우 
    gain = (score[i][1] if score[i - 1][0] else 0) + (score[i - 1][1] if score[i][0] else 0)
    dp[i][1] = max(dp[i - 2][0] + gain, dp[i - 2][1] + gain)

print(max(dp[n][0], dp[n][1]))
