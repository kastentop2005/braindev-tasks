a = int(input(), 2)
b = int(input(), 2)

first = str(bin(a | b))
second = str(bin(a & b))
third = str(bin(a ^ b))

print(first)
print(second)
print(third)