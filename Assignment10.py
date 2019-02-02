# Using assignment operators, perform following operations
# Addition, Substation, Multiplication, Division, Modulus, Exponent and Floor division operations


while(True):
    x = eval(input('''enter a number to perform basic arithmetic operation using assignment operator 
                           1. Addition
                           2. Subtraction
                           3. Multiplication
                           4. Division
                           5. Modulus
                           6. Exponent
                           7. Floor Division
                           8. Quit'''))
    if(x==8):
        break
    num1 = eval(input("enter number 1"))
    num2 = eval(input("enter number 2"))
    if(x == 1):
        num1 += num2
        print("Addition using Assignment operator is ::", num1)
    elif(x==2):
        num1 -= num2
        print("Subtraction using Assignment operator is ::", num1)
    elif(x==3):
        num1 *= num2
        print("Multiplication using Assignment operator is ::", num1)
    elif(x==4):
        num1 /= num2
        print("Division using Assignment operator is ::", num1)
    elif(x==5):
        num1 %= num2
        print("Modulus using Assignment operator is ::", num1)
    elif(x==6):
        num1 **= num2
        print("Exponent using Assignment operator is ::", num1)
    elif(x==7):
        num1 //= num2
        print("Floor Division using Assignment operator is ::", num1)

    else:
        print("please enter a number from the options only")



