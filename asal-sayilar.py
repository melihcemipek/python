maks = 100

for x in range(2, maks):
    asal = True
    for y in range(2, int (x**0.5)):
        if x % y == 0:
            asal = False
            break

    if asal:
        print(x)