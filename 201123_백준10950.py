# 다수의 입력을 받아서 덧셈 결과 출력하기 
a = int(input())
result = []
for i in range(a):
  b, c = input().split(" ")
  m = int(b) + int(c)
  result.append(m)

for i in result:
  print(i)
