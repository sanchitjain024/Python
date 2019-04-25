"""
*** THE PYTHON CALCULATOR PROJECT ***
"""
c = True
while c == True:
    print("CALCULATOR MENU:\n\nWelcome to the Python Calculator! Please choose from the below options to proceed :-\n")
    print("1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Modulo Division 6. Exponentiation 7. Quit\n")
    op = input("Select your choice of operation(1 - 7): ")
    if float(op) == 7:
        c = False
        print("\n\nThanks for using his calculator! Good Bye!\n\n\n")
    else :
        n1 = input("\nInput First Number: ")
        n2 = input("\nInput Second Number: ")
        if float(op) == 1:
            res = float(n1) + float(n2)
            print("\nThe sum of the two numbers = " + str(res)+"\n\n\n")
        elif float(op) == 2:
            res = float(n1) - float(n2)
            print("\nThe difference of the two numbers = " + str(res)+"\n\n\n")
        elif float(op) == 3:
            res = float(n1) * float(n2)
            print("\nThe product of the two numbers = " + str(res)+"\n\n\n")
        elif float(op) == 4:
            if n2 == 0:
                print("\nDivision by zero is not allowed!\n\n"+"\n\n\n")
            else:
                res = float(n1) / float(n2)
                print("\nThe quotient of the division between the two numbers = " + str(res)+"\n\n\n")
        elif float(op) == 5:
            if n2 == 0:
                print("\nDivision by zero is not allowed!\n\n"+"\n\n\n")
            else:
                res = float(n1) % float(n2)
                print("\nThe remainder of the division between the two numbers = " + str(res)+"\n\n\n")
        elif float(op) == 6:
            res = float(n1) ** float(n2)
            print("\n"+str(n1)+" raised to the power "+str(n2)+" = "+str(res)+"\n\n\n")
        else:
            print("\n\nInvalid choice. Please choose from the available options (1 - 7) only.\n\n\n\n")
c = False
"""
*** END OF PROGRAM ***
"""
