a, b = map(int, input().split())
x = int(input())

cnt = 0
while x > 0:
    x = min(x // 2 + a, x - a)
    cnt += 1

print(max(0, b - cnt * a))
