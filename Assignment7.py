# Create a list with at least 10 elements having integer values in it;
#        Print all elements
#        Perform slicing operations
#        Perform repetition with * operator
#        Perform concatenation with other list.

print('enter 10 elements to be inserted in the list')
list = []
#taking input from user
for i in range(10):
    x = eval(input("enter element at index "+str(i)))
    list.insert(i,x)
       #Print all elements
print(list)

#       Perform slicing operations

start = eval(input("enter start of the subList"))  #starting of the substring
end = eval(input("enter end of the subList, that will be excluded")) #ending of the substring
dif = eval(input("enter difference between characters, enter 1, if you do not want so"))
if(dif >= 1):
    print(list[start:end:dif])
else:
    print("minimum difference should be 1")

#         Perform repetition with * operator
#
rep = eval(input("enter how many times you wantto repeat the string"))
for i in list :
    print(str(i)*rep)
print(list*rep)



#         Perform concatenation with other list.
print("enter another list")
z = eval(input("enter the size of list 2"))
#taking input from user
list1 = []
for j in range(z):
    y = eval(input("enter element at index "+str(j)))
    list1.insert(j,y)
print(list1)

#merging two list
concatList = list+ list1

#printing concated list
print(concatList)