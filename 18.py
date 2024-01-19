num = float(input())
approx = float(input())

absmarg = abs(approx - num)
relmarg = (abs(absmarg / approx)) * 100

print(f"{int(relmarg)}%")