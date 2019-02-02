# Using assignment operators, perform following operations
# Addition, Substation, Multiplication, Division, Modulus, Exponent and Floor division operations


while(True):
    x = eval(input('''enter a number to perform basic arithmetic operation using assignment operator 
                           1. And
                           2. Or
                           3. XOR
                           4. Inverse
                           5. Left Shift
                           6. Right Shift
                           7. Quit
                           '''))
    if(x==7):
        break

    if(x == 1):
        num1 = eval(input("enter number 1"))
        num2 = eval(input("enter number 2"))
        res = num1 and num2
        print("And operation  ::", res)
    elif(x==2):
        num1 = eval(input("enter number 1"))
        num2 = eval(input("enter number 2"))
        res = num1 or num2
        print("OR operation  ::", res)
    elif(x==3):
        num1 = eval(input("enter number 1"))
        num2 = eval(input("enter number 2"))
        res = num1^num2
        print("XOR operation is ::", res)
    elif(x==4):
        num1 = eval(input("enter number 1"))
        res = ~num1
        print("NOT operation is ::", res)
    elif(x==5):
        num1 = eval(input("enter number 1"))
        num2 = eval(input("enter number 2"))
        res = num1 << num2
        print("Left Shift operation is ::", res)
    elif(x==6):
        num1 = eval(input("enter number 1"))
        num2 = eval(input("enter number 2"))
        res = num1 >> num2
        print("Right Shift operation is ::", res)
    else:
        print("please enter a number from the options only")
