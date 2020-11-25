ct = []
while True:
  a, b = input().split()

  if a == '0' and b == '0':
    break
  else:
    s = int(a) + int(b)
    ct.append(s)

for i in ct:
  print(i)
