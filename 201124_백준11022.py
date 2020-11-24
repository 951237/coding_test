# 빠른 합
import sys

result = []
a = int(input()) # 입력횟수 입력받기
for i in range(a):
  k = list(map(int, sys.stdin.readline().split())) # 여러줄을 입력받아 숫자로 바꿔서 리스트로 만들기
  result.append(k)

# print(result)

for i in range(a):
  sum = result[i][0] + result[i][1] # 입력받은 리스트 내의 리스트의 숫자의 합
  print(f'Case #{i+1}: {result[i][0]} + {result[i][1]} = {sum}')
