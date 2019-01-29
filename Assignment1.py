#Write a program to Add, Subtract, Multiply, and Divide 2 numbers

a = input("enter first number")
b = input("enter second number")

#addition of two number
c= a+b
print("Addition of two number is ::"+ str(c))

#subtraction of two number
if(a>b):
	c=a-b
else:
	c=b-a

print("Subtraction of two number is::"+ str(c))

#multiply of two number
c=a*b
print("Multiplication of two number is::"+ str(c))

#division of two number
c= a/b
print("division of two number is::"+ str(c))
