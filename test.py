def getNth(nth):
    num1 = 0
    num2 = 1

    for _ in range(nth-1):
        tmpnum1 = num1
        num1 = num2
        num2 = tmpnum1 + num2

    return num1 + num2

n = 1
nth = getNth(n)
sum = 0

while nth < 4000000:
    if nth % 2 == 0:
        sum += nth
    n += 1
    nth = getNth(n)

print(sum)
