#Write a program to find the biggest of 3 numbers (Use If Condition)

#taking three inputs from user
print("enter three numbers")
a = input()
b = input()
c = input()

#using if to check if a is biggest
if(a>b and a>c):
	print("the biggest number among three is ::"+ str(a))

#if a is not, then checking whether b is greater than c
elif (b>c):
	print("the biggest number among three is ::"+ str(b))
#then c will be biggest
else:
	print("the biggest number among three is ::"+ str(c))