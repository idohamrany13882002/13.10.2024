# input a number and print how many digit is it
num: int = int(input("enter a number: "))
counter: int = 0
while num > 0:
    num = num//10
    counter += 1
if counter != 0:
    print(counter)
else:
    print (1)