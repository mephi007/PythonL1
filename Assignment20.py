# Write a program to generate a Fibonacci series of numbers.
# Starting numbers are 0 and 1,  new number in the series is generated by adding previous two numbers in the series.
# Example : 0, 1, 1, 2, 3, 5, 8,13,21,.....
#    a) Number of elements printed in the series should be N numbers, Where N is any +ve integer.
#    b) Generate the series until the element in the series is less than Max number.

n = eval(input("enter no. of elements"))
a = 0
b =1
list = [0,1]
for i in range(2,n):
     c = a+b
     a = b
     b = c
     list.append(c)

print(list)