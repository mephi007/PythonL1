#Write a program to find biggest of 4 number
#read 4 number using Input statment
#extend the program to 5 numbers and find biggest among them


#read 4 number using Input statment
print("Enter 4 numbers")

list = []
for i in range(4):
    x = eval(input())
    list.insert(i,x)

#find biggest among 4 number
biggest = list[0]
for i in range(1,4):
	if(list[i] > biggest):
		biggest = list[i]

print("Biggest number in given 4 numbers",biggest)

#extend the program to 5 numbers 
y = eval(input("Enter one more number"))
list.append(y)

if(biggest < list[4]):
	biggest = list[4]

print("biggest among 5 is ::", biggest)