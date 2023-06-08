#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    sum = 0
    print("Two or more numbers are equal, so the sum is:", sum)
else:
    total = num1 + num2 + num3
    print("The sum is:", total)
