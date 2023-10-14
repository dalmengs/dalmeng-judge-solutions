# pre-defined
MOD = 100000007
SIZE = 100000

n = input()

b = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1] # b[k] = k일때 박수를 치는지

dp = [0 for i in range(SIZE)] # dp[k] = 1부터 k자리 수(pow(10, k) - 1)까지 박수 횟수
dp[1] = 3

p = [1 for i in range(SIZE)] # p[k] = pow(10, k)
for i in range(1, SIZE):
    p[i] = (p[i - 1] * 10) % MOD

for i in range(2, SIZE):
    dp[i] = (((10 * dp[i - 1]) % MOD) + (3 * p[i - 1]) % MOD) % MOD

chk, ans = 0, 0
for i in range(len(n)):
    first = int(n[i])
   
    for j in range(first):
        ans += dp[len(n) - 1 - i] % MOD
        ans += (b[j] * p[len(n) - i - 1]) % MOD
   
    ans += ((int(n[i]) * p[len(n) - i - 1]) % MOD * chk) % MOD
   
    if b[int(n[i])] == 1:
        chk += 1

ans = (ans + chk) % MOD

print(ans)
