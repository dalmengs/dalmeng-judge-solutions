n, t = map(int, input().split())
d = {}

def timeConvert(s):
    s = s.split(":")
    return int(s[0]) * 60 + int(s[1])

for _ in range(n):
    x, y = input().split()
    if y not in d:
        d[y] = {
            "isIn": True,
            "inTime": timeConvert(x),
            "total": 0
        }
    else:
        if d[y]["isIn"] == False:
            d[y]["isIn"] = True
            d[y]["inTime"] = timeConvert(x)
        else:
            d[y]["isIn"] = False
            d[y]["total"] += (timeConvert(x) - d[y]["inTime"]) * t

for i in d:
    print(i, d[i]["total"])
