n = int(input())
a, b = map(int, input().split())

if a + b > n: # 첫 턴도 하지 못 하고 게임이 끝나는 경우 
    print("Draw")
else: # 한 번이라도 돌을 가져가면 승패가 난다 
    if a > b:
        print("Dalmeng")
    elif a < b:
        print("Manbo")
    else:
        print("Draw")
