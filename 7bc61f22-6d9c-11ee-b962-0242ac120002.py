s = input()

# 연산 기호를 기준으로 나누기
s = s.split("-")
for i in range(len(s)):
    s[i] = s[i].split("+")

# 수식을 넣으면 num 함수의 반환 값을 돌려줌 
def parse(s):
    ret = 0
    
    # 1. 함수 이름(num) 없애기
    # 2. 양쪽에 있는 괄호 없애기 
    s = s[3:].strip("(").strip(")")
    
    # int num(String n)의 경우 
    if s[0] == "\"":
        s = s[1:-1]
        for i in s:
            ret += int(i)
    # int num(int n)의 경우 
    else:
        for i in s:
            ret = max(ret, int(i))
    
    return ret

ans = 0
for i in s:
    temp = 0
    for j in i:
        temp += parse(j)
    ans -= k if ans != 0 else -k

print(ans)
