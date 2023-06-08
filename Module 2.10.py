#Write a Python program that will return true if the two given integer  values are equal or their sum or difference is 5


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x == y or abs(x - y) == 5 or (x + y) == 5:
    print("True")
else:
    print("False")
