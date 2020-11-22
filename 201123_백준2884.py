# 알람시계 45분 미리 울리기
a, b = input().split(' ')

a = int(a) * 60
b = int(b)

time = a + b
result = time - 45

hour = result // 60
if hour < 0:
  hour = 24 + hour
minute = result % 60

print(hour, minute)
