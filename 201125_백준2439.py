# # 별찍기 - 2
# # 오른쪽에서 거꾸로 찍기
a = int(input())
for i in range(a):
  print('{}{}'.format(' ' * (a-1-i), '*' * (i+1)))
