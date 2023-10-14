m = int(input())
k = []
for i in range(2):
    k.append(input())
    
# 인덱스를 1부터 시작하게 하기 위해 임의의 문자를 추가합니다.
k[0] = " " + k[0]
k[1] = " " + k[1]

# dp[state][idx] : state 값에 따라 idx번째 땅까지 블록을 채우는 경우의 수 
dp = [[0 for i in range(m + 1)] for j in range(3)]

# 모듈러
mod = 100000007

# 초기값 설정 
dp[0][0] = 1
dp[1][0] = 1
dp[2][0] = 1

if k[0][1] == k[1][1] == " ":
    dp[2][1] = 1

for i in range(2, m + 1):
    if k[0][i] == k[1][i] == " ":
        dp[2][i] = (dp[2][i] + dp[2][i - 1]) % mod
        if k[0][i - 1] == k[1][i - 1] == " ":
            dp[2][i] = (dp[2][i] + dp[2][i - 2]) % mod
            dp[0][i] = (dp[0][i] + dp[1][i - 1]) % mod
            dp[1][i] = (dp[1][i] + dp[0][i - 1]) % mod

        elif k[0][i - 1] == " " and k[1][i - 1] == "*":
            dp[1][i] = (dp[1][i] + dp[2][i - 2]) % mod

        elif k[0][i - 1] == "*" and k[1][i - 1] == " ":
            dp[0][i] = (dp[0][i] + dp[2][i - 2]) % mod

    elif k[0][i] == " " and k[1][i] == "*":
        dp[2][i] = (dp[2][i] + dp[0][i - 1]) % mod
        dp[0][i] = (dp[0][i] + dp[2][i - 1]) % mod
    
    elif k[0][i] == "*" and k[1][i] == " ":
        dp[2][i] = (dp[2][i] + dp[1][i - 1] % mod)
        dp[1][i] = (dp[1][i] + dp[2][i - 1] % mod)
    
    else:
        if dp[2][i - 1] != 0:
            dp[2][i] = (dp[2][i] + dp[2][i - 1]) % mod
        else:
            dp[2][i] = (dp[2][i] + 1) % mod

print(dp[2][m])