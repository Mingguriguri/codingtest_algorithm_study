import sys
import math
input = sys.stdin.readline

n = int(input())

# 학생 통화 시간 계산 및 저장
call_log = {}
for _ in range(n):
    time, name = map(str, input().split())
    hour, minute = map(int, time.split(":"))

    if name in call_log:
        call_log[name] += minute + hour * 60
    else:
        call_log[name] = minute + hour * 60

# 통화 요금 계산
charge = {}
for k, v in call_log.items():
    if v <= 100:
        charge[k] = 10
    else:
        charge[k] = 10 + math.ceil((v - 100) / 50) * 3

for name, value in sorted(charge.items(), key=lambda x: (-x[1], x[0])):
    print(name, value)