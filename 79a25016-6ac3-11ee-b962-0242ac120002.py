MOD = 100000007

n = int(input())
dp = [[0 for i in range(2)] for j in range(max(4, n + 1))]

# dp[idx][0] : idx까지 게임을 진행했을 때 짝수번에 게임이 끝나는 경우의 수 
# dp[idx][1] : idx까지 게임을 진행했을 때 홀수번에 게임이 끝나는 경우의 수 

dp[1][0] = 0
dp[1][1] = 1

dp[2][0] = 1
dp[2][1] = 1

# 문제에서 n이 3인 경우를 제시해줬음; 짝수 2번, 홀수 2번
dp[3][0] = 2
dp[3][1] = 2

for i in range(4, n + 1, 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 2][1] + dp[i - 3][1]) % MOD
    dp[i][1] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 3][0]) % MOD

# 달맹이 승리하려면 게임이 짝수번에 끝나야 한다
print(dp[n][0])
