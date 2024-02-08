n = int(input())
a = list(map(int, input().split()))
c = {0 : 1}
x = int(input())
ans, s = 0, 0
for i in a:
    s += i
    if s - x in c:
        ans += c[s - x]
    if s in c:
        c[s] += 1
    else:
        c[s] = 1
print(ans)
