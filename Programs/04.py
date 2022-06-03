def binToInt(bin):
    amount = 1; int = 0
    for i in range(len(bin), 0, -1):
        if bin[i-1] == '1':
            int += amount
        amount *= 2
    return int

print(binToInt('11111111')) #255
print(binToInt('10010101')) #149
print(binToInt('01101001')) #105
print(binToInt('00000000')) #0