num1: int = int(input("enter a number: "))
sum1: int = 0
while num1 > 0:
    x: int = num1 % 10
    sum1 += x
    num1 = num1 // 10
print(sum1)