a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4 * a * c

if d > 0:
  x1 = ((-b + d**0.5) / (2 * a))
  x2 = ((-b - d**0.5) / (2 * a))
  print(int(x1))
  print(int(x2))
elif d == 0:
  x = ((-b + d**0.5) / (2 * a))
  print(int(x))
elif d < 0:
  print("Дискрминант меньше нуля")
  exit(1)