n = int(input())
k = []

for i in range(n):
    x, y = map(int, input().split())
    k.append([x, y])
    
k = sorted(k)

l, r = 0, 0
for i in range(1, n):
    r += abs(k[i][0] - k[0][0])

ans = l + r
for i in range(1, n):
    ans = min(ans, l + r)
    diff = abs(k[i][0] - k[i - 1][0])
    l += diff * i
    r -= diff * (n - i)

ans = min(ans, l + r)
print(ans)
