# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
# a) By using For loop
# b) By using while loop
# c) Let mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure.

# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)

#using for loop
x= 1
y = 100
print("using for loop")
for i in range(100):
    print(x, y)
    x =x+1
    y = y-1
print("using while loop")
#using while loop
k= 1
l = 100
j=100
while(j!=0):
    print(k, l)
    k = k + 1
    l = l - 1
    j = j-1

mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure.
print("printing each character of string on new line ")
for i in mystring:
    print(i)