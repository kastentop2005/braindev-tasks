num = int(input())

if len(str(num)) != 3:
  print("Нужно трёхзначное число")
  exit(1)

print((num // 100) + (num // 10 % 10) + (num % 10))