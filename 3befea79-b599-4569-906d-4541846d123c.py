n = int(input())
s = [input(), input()]

s1, s2 = "", ""
for i in range(n): # 지그재그 이진 문자열로 변환 
    s1 += s[i % 2][i]
    s2 += s[(i + 1) % 2][i]

ans = 0

cnt, prev = 0, s1[0]
for i in s1: # 위층 지그재그 이진 문자열 그룹화
    if i == prev:
        cnt += 1
    else:
        prev = i
if s1[0] == "0":
    ans += cnt // 2
else:
    ans += (cnt + 1) // 2

cnt, prev = 0, s2[0]
for i in s2: # 아래층 지그재그 이진 문자열 그룹화
    if i == prev:
        cnt += 1
    else:
        prev = i
if s2[0] == "1":
    ans += cnt // 2
else:
    ans += (cnt + 1) // 2

print(ans)
