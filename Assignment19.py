# Using loop structures print even numbers between 1 to 100.
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#     i) Break the loop if the value is 50
#     ii) Use continue for the values 10,20,30,40,50
#       b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#       i) Break the loop if the value is 90
#       ii) Use continue for the values 60,70,80,90

# Using loop structures print even numbers between 1 to 100.
print("using for loop")
for i in range(1,101):
    if(i%2 == 0):
        print(i, end=" ")
    else:
        pass

print("\n")
print("using pass, break, continue")
for i in range(1, 101):
    if (i % 2 == 0):
        print(i, end=" ")
    else:
        pass
    if(i == 50):
        break      #     i) Break the loop if the value is 50
   

#       b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
print("\nusing While loop")
i = 1
while(i !=101):
    if (i % 2 == 0):
        print(i, end=" ")
    else:
        pass
    i = i+1

print(" \nusing pass, break, continue")
j=1
while (j != 101):
    if (j % 2 == 0):
        print(j, end=" ")
    else:
        pass
    if (j == 90):
        break  # i) Break the loop if the value is 90

    j = j + 1
