# Write a program to create two list A & B such that List A contains Employee Id, 
# List B contain Employee name (minimum 10 entries in each list) & perform following operation
#Print all names on to screen
#Read the index from the  user and print the corresponding name from both list
#Print the names from 4th position to 9th position
#Print all names from 3rd position till end of the list
#Repeat list elements by specified number of times (N- times, where N is entered by user)
#Concatenate two lists and print the output.
#Print element of list A and B side by side.(i.e. List-A First element, List-B First element)


#create two list A & B such that List A contains Employee Id, 
# List B contain Employee name 
listA = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
listB = ["sumit", "sam", "sameer", "mayank", "naman", "vishal", "deepti", "sagarika", "vinod", "raju"]

#Print all names on to screen
for i in range(10):
	print(listB[i])

#Read the index from the  user and print the corresponding name from both list
x = eval(input("Enter a index whose detail you want to see"))
print(listA[x],"  ",listB[x])

#Print the names from 4th position to 9th position
print("printing names from 4th position to 9th position")
print(listA[4:9]," ",listB[4:9])

#Print all names from 3rd position till end of the list
print("printing names from 3rd position till the end")
print(listA[3::]," ",listB[3::])

#Repeat list elements by specified number of times (N- times, where N is entered by user)
y = eval(input("Enter how many times do you want to repeat list elements"))
print(listA*y, " ", listB*y)

#Concatenate two lists and print the output.
listConcat = listA+ listB
print("Concated list :: ", listConcat)

#Print element of list A and B side by side.(i.e. List-A First element, List-B First element)
print("print elements of both the list side by side")
for i in range(10):
	print(listA[i], " ", listB[i])
