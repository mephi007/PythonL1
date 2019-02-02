# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# a) From the above statement your program should receive arguments and print them each of them.


#importing system package as it contain command line arguments (argv)

from sys import argv

print("the numbers entered via command line arguments:")

#printing data 
for i in range(1,len(argv)):
    print(argv[i])