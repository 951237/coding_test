i_d = input()
a, b = i_d.split(" ")
if int(a) > int(b):
  print('>')
elif int(a) < int(b):
  print('<')
else:
  print('==')
