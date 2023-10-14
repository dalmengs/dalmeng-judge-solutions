MOD = 100000007

n = int(input())

# 문자열을 수정할 수 있도록 리스트 형식으로 바꿨습니다.
arr = [[], []]

q1 = input()
q2 = input()

for i in range(len(q1)):
    arr[0].append(q1[i])
    arr[1].append(q2[i])

for j in range(n-1) :
    if arr[0][j] == '*' and arr[1][j] == ' ' : arr[1][j] = '*'; arr[1][j+1] = '*'
    if arr[0][j] == ' ' and arr[1][j] == '*' : arr[0][j] = '*'; arr[0][j+1] = '*'

if arr[0][n-1] != arr[1][n-1] : print(0)
else :
    dp = [0 for _ in range(n+2)]
    dp[1] = 1
    for j in range(2,n+2) :
        dp[j] = dp[j-1] 
        if arr[0][j-2] != '*' and arr[0][j-3] != '*' : dp[j] += dp[j-2]
        dp[j] %= MOD

    print(dp[n+1])
