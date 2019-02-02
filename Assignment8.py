# Create a tuple with at least 10 elements having integer values in it;
#        Print all elements
#        Perform slicing operations
#        Perform repetition with * operator
#        Perform concatenation with other tuple.

print('enter 10 elements to be inserted in the tuple')
tuple = ()
#taking input from user
for i in range(10):
    x = eval(input("enter element at index "+str(i)))
    tuple = tuple + (x,)
       #Print all elements
print(tuple)

#       Perform slicing operations

start = eval(input("enter start of the subtuple"))  #starting of the substring
end = eval(input("enter end of the subTuple, that will be excluded")) #ending of the substring
dif = eval(input("enter difference between characters, enter 1, if you do not want so"))
if(dif >= 1):
    print(tuple[start:end:dif])
else:
    print("minimum difference should be 1")

#         Perform repetition with * operator
#
rep = eval(input("enter how many times you wantto repeat the string"))
for i in tuple :
    print(str(i)*rep)
print(tuple*rep)



#         Perform concatenation with other tuple.
print("enter another tuple")
z = eval(input("enter the size of tuple 2"))
#taking input from user
tuple1 = ()
for j in range(z):
    y = eval(input("enter element at index "+str(j)))
    tuple1 = tuple1 + (y,)
print(tuple1)

#merging two tuple
concatTuple = tuple + tuple1

#printing concated tuple
print(concatTuple)