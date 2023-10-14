m = int(input())
k = []

for i in range(2):
    k.append(input())

# 인덱스를 1부터 시작하게 하기 위해 임의의 문자를 추가합니다.
k[0] = " " + k[0]
k[1] = " " + k[1]

mod = 100000007

# 미리 피보나치 수열을 구해놓습니다.
dp = [0, 1, 2]
for i in range(m + 1):
    dp.append((dp[-1] + dp[-2]) % mod)

ans = 1

# mode = 1 : 위 아래로 모두 비어있는 구간 
# mode = 2 : 위에만 블록이 채워져 있는 시작 구간
# mode = 3 : 아래만 블록이 채워져 있는 시작 구간 
mode = 0

r = 0
start = 0

i = 1
while i <= m:
    if mode == 0:
        if k[0][i] == k[1][i] == " ":
            mode = 1
            r += 1
        elif k[0][i] == "*" and k[1][i] == " ":
            mode = 2
            start = i
        elif k[0][i] == " " and k[1][i] == "*":
            mode = 3
            start = i
    
    elif mode == 1:
        if k[0][i] == k[1][i] == " ":
            r += 1
            if i == m:
                ans = (ans * dp[r]) % mod
        else:
            ans = (ans * dp[r]) % mod
            mode = 0
            r = 0
            i -= 1
    
    elif mode == 2:
        if k[0][i] == k[1][i] == "*":
            ans = 0
            break
        elif k[0][i] == " " and k[1][i] == "*":
            x = i - start
            if x % 2 == 0:
                r = 0
                mode = 0
            else:
                ans = 0
                break
        elif k[0][i] == "*" and k[1][i] == " ":
            x = i - start
            if x % 2 == 0:
                ans = 0
                break
            else:
                r = 0
                mode = 0
    
    elif mode == 3:
        if k[0][i] == k[1][i] == "*":
            ans = 0
            break
        elif k[0][i] == " " and k[1][i] == "*":
            x = i - start
            if x % 2 == 0:
                ans = 0
                break
            else:
                r = 0
                mode = 0
        elif k[0][i] == "*" and k[1][i] == " ":
            x = i - start
            if x % 2 == 0:
                r = 0
                mode = 0
            else:
                ans = 0
                break
    i += 1
    
print(ans)
