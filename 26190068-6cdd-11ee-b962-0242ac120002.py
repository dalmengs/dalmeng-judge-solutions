def decimalToHex(n, base = 16):
    ret = []
        
    while n:
        ret.append(n % base)
        n //= base
        
    return "".join(reversed(list(map(str, ret))))

n = int(input())
s = decimalToHex(n)
n = len(s)

dp = [[-1 for j in range(n + 5)] for i in range(16)]
ans = dp[0][len(s) - 1] = int(s[-1])

for i in range(1, 16):
    for j in range(len(s) - 1, -1, -1):
        if dp[i - 1][j + 1] != -1:
            dp[i][j] = max(dp[i][j], (dp[i - 1][j + 1] + 16**i * int(s[j])))
        if dp[i - 1][j + 2] != -1 and s[j] == "1" and s[j + 1] in "012345":
            dp[i][j] = max(dp[i][j], (dp[i - 1][j + 2] + 16**i * int(s[j] + s[j + 1])))
        ans = max(ans, dp[i][j])

print(ans)
