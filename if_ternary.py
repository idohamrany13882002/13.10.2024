x: int = int(input("enter x: "))

print(f"{x} is {"Even" if x % 2 == 0 else "Odd"}")

# input a height between 0.1-2.8
# print you are tall (if height > 1.8)
# print you are not tall (if height <=1.8)
height: float = float(input("enter height: "))
while not 0.1<=height<=2.8:
    print (f"the height {height} is not valid")
    height: float = float(input("enter height: "))
else:
    print (f"you are {""if height>1.8 else "not "}tall")

# input a number between 0-99
# print - the number is 1 digit
# print - the number is 2 digits
num: int = int(input("enter a number: "))
print (f"{num} is a {"1 digit" if num/10 <1 else "2 digits"} number")