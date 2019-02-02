# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

#importing system package as it contain command line arguments (argv)
from sys import argv

print("the biggest number among 3 is ::")

largest = argv[1]

for i in range(2,len(argv)):
    if(argv[i] > largest):
        largest = argv[i]

print(largest)
