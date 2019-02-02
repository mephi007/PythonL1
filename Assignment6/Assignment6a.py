# Write a program to read string and print each character separately.
#     a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.

#asking user to give a string for the slicing operation
str = input("enter a String")
start = eval(input("enter start of the substring"))  #starting of the substring
end = eval(input("enter end of the substring, that will be excluded")) #ending of the substring
dif = eval(input("enter difference between characters, enter 1, if you do not want so"))
print(str[start:end:dif]) #printing the substring