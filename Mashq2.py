son = int(input("Son kiriting: "))
kopaytma = 1

for i in range(1, son+1):
    kopaytma *= i

print(f"Ko'paytma: {kopaytma}")