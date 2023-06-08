#Write a Python program to get the Factorial number of given number.

i=int(input("enter number: "))
fac=1
while(i>0):
	fac=fac*i
	i=i-1
	
	print("factorial=", fac)