# 2개으 숫자를 입력받고 첫번째 입력받은 숫자만큼 숫라를 입력하면 두번ㅉ 입력한 숫자보다 크기가 작은 값을 출력
from random import *

a, b = input().split(' ')

result = []

r = list(map(int, input().split())) # 입력받은 텍스트를 나눠서 숫자로 리스틍 저장

# print(r)

lst_min = []
for i in r:
  if i < int(b):
    lst_min.append(i)

for i in lst_min:
  print(i, end=' ')

# 참고코드
# for i in range(a):
#   k = list(map(int, sys.stdin.readline().split())) # 여러줄을 입력받아 숫자로 바꿔서 리스트로 만들기
#   result.append(k)
