#Write a Python program to get the Fibonacci series of given range.

num=int(input("Enter number : "))
a=0
b=1
c=0
for i in range(num):
	print(c,end="  ")
	a=b             #a=1
	b=c             #b=0
	c=a+b         #c=1+0