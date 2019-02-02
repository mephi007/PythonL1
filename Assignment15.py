#Create a list of 5 names and check given name exist in the List.
#Use membership operator (IN) to check the presence of an element.
#Perform above task without using membership operator.


#Create a list of 5 names 
Names = ["sumit", "sam", "sameer", "mayank", "naman"]

#check given name exist in the List.
str = input("enter a name to be searched in list")
print("searching usin membership operator IN")
if str in Names:
	print("Found")
else:
	print("Not found")

#Perform above task without using membership operator.
print("searching wihout IN membership operator")
for name in Names:
	if(str == name):
		print("Found")
		break
	else:
		print("not found")