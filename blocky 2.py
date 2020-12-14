from numbers import Number

num = None


num = 1
for count in range(5):
  num = (num if isinstance(num, Number) else 0) + 2
  print(num)