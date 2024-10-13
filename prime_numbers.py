# #exc a
# x: int = int(input("enter a number: "))
#
# if x < 1:
#     print("must be equal or grater then 1")
# elif x == 1:
#     print("1 in not prime")
# else:
#     divider: int = 2
#     while divider < x:
#         if x % divider == 0:
#             break
#         else:
#             divider += 1
#     if divider<x:
#         print (f"{x} is prime")
#     else:
#         print (f"{x} is not prime")
#
# #exc b
# prime_list: list[int] = []
# for i in range(2, 101):
#     divider: int = 2
#     while i > divider:
#         if i % divider == 0:
#             break
#         divider += 1
#     if i == divider:
#         prime_list.append(i)
# print(f"prime list: {prime_list}")


#      append (x)        for x in (2-100)               check if prime
print([x for x in [num for num in range(2, 101)] if all([x % i for i in range(2, x)])])
