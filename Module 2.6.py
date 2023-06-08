#Write python program that swap two number with temp variable and without temp variable.

a=10
b=20
print("before swapping values")
print("a:" ,a)
print("b:" ,b)

#using temp variable
temp =a
a=b;
b=temp
print("after swapping values")
print("a:" ,a)
print("b:" ,b)

#without using temp variable

a=a+b; #a=30
b=a-b   #b=30-20   b=10
a=a-b   #a=30-10   a=20

print("after swapping values")
print("a:" ,a)
print("b:" ,b)