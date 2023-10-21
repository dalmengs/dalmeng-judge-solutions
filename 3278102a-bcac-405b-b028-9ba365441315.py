n = int(input())

s = []
for i in range(3):
    s.append(input())

# 전광판의 상태
# 숫자 2로는 바꿀 일이 없으므로 빈 문자열로 정의 
k = ["OOOO OOOO", " O  O  O ", "", "OOO OOOOO", "O OOOO  O", "OOO O OOO", "O  OOOOOO", "OOO  O  O", "OOOOOOOOO", "OOOOOO  O"]

ans = ""
for i in range(n):
    x = i * 3
    y = s[0][x:x+3] + s[1][x:x+3] + s[2][x:x+3]
    for j in range(len(k)):
        if k[j] == y:
            ans += str(j)

print(ans)
