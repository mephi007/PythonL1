#Write a program to find the number is Prime or not.


# taking input from user
print("Enter a number")
a = input()

#checking whether the number is prime or not.
#for prime, the number will have only 2 factors, that is the number will be divisible by 1 and by itself only
flag =0

for i in range(1,a+1):
	if(a%i == 0):
		flag = flag+1

if(flag == 2):
	print("the given number is PRIME")
else:
	print("the given number is NOT prime")