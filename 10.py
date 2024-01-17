a = input()
b = input()

try:
    num1 = float(a)
    num2 = float(b)
    if num1.is_integer() and num2.is_integer():
      result = int(num1 + num2)
    else:
      result = num1 + num2
except ValueError:
    result = a + b

print(result)