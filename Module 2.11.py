#Write a python program to sum of the first n positive integers.

n = int(input("Enter a number: "))

if n <= 0:
    print("Enter a positive number!")
else:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print("Sum of the first", n, "positive integers is", total_sum)
