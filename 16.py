from math import pi

def Triangle():
  a = int(input())
  b = int(input())
  c = int(input())
  
  ph = (a + b + c) / 2
  s = (ph * (ph - a) * (ph - b) * (ph - c))**0.5
  
  return int(s)

def Rectangle():
  a = int(input())
  b = int(input())
  
  s = a * b
  
  return int(s)

def Circle():
  r = int(input())
  
  s = pi * r**2
  
  return round(s, 2)

choice = str(input())

if choice == "Прямоугольник":
  print(Rectangle())
elif choice == "Треугольник":
  print(Triangle())
elif choice == "Круг":
  print(Circle())  