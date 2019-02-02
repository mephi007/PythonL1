# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.


# Read 10 numbers from user
print("Enter 10 number")
list = []
for i in range(10):
    x = eval(input())
    list.insert(i,x)

# and find the average of all.
sum =0
for i in range(10):
    sum = sum+list[i]
avg = sum/10;

# Use comparison operator to check how many numbers are less than average and print them
less =0
for i in range(10):
    if( avg > list[i]):
        less += 1
        print("element of list is lesser than average", list[i])

print("in a list,", less, "elements are lesser than average")


#Check how many numbers are more than average.
more = 0
for i in range(10):
    if( avg < list[i]):
        more += 1
        print("element of list is bigger than average", list[i])

print("in a list,", more, "elements are bigger than average")

#How many are equal to average.
equal =0
for i in range(10):
    if( avg == list[i]):
        equal += 1
        print("element of list is equal to average", list[i])

print("in a list,", equal, "elements are  equal to  average")