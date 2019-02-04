# Write program to find the biggest and Smallest of N numbers.
#       PS: Use the functions to find biggest and smallest numbers.

def biggest(list):   #Declaring and defining the function biggest() and passing list through it
    large = list[0]
    for i in range(1,N):
        if(large< list[i]):
            large = list[i]

    return large          #return the largest among all

def smallest(list):     #Declaring and defining the function smallest() and passing list through it
    small = list[0]
    for i in range(1,N):
        if(small > list[i]):
            small = list[i]
    return small                 #return the smallest among all

N = eval(input("Enter Number of elements you want to enter"))  #asking user for N elements
list =[]
for i in range(N):
    x = eval(input("Enter element"))      #stroring elements in the list of N size
    list.append(x)

print("The Biggest among all is ::", biggest(list))
print("The Smallest among all is ::", smallest(list))

