import math

# Created a variable a to save the option chose by the user and
# Printing a massage to explain about the options available (investment and bond) is:

a= str(input("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on your home laon \n\nEnter either 'investment' or 'bond' from the menu above to proceed:"))

# Saving investment and bond under variables to compare with the user inputs.
b= "investment"
c = "bond"


# Using if, elif and else condition to compare the user input with variables(investment and bond), ask related questions and,
# Using lower function to convert the user input to lower case to make it case insensitive.


if a.lower() == b:
    P = int(input("Please enter the amount of deposit:"))
    r = int(input("Please enter interest rate: "))
    r = r/100
    t = int(input("Number of years you would like to invest"))

    # Using a variable to store user choice of simple interest or compund.
    interest = str(input("Please choose type of interest you want 'simple' or 'compound': "))

    # Using if,elif and else condition to check the user input is either simple or compund else print a prompt to choose either of the options.

    if interest == 'simple':
        A= P*(1+r*t)
        print("the amount you'll earn by the end of",t,"years is:",A);
    elif interest == 'compound':
        A = P * math.pow((1+r),t)
        print("the amount you'll earn by the end of",t,"years is:",A);
    else:
        print("sorry! you have choose either 'simple' or 'compund' only");

elif a.lower() == c:
    P = int(input("Please enter the present value of house: "))
    r = int(input("please enter the interest rate: "))
    r = r/100
    i = r/12
    n = int(input("Please enter the number of months you would like to repay the bond: "))
    R = (i*P)/(1-(1+i)**(-n))
    print("The amount you will have to pay each month is :",R);

else :
    print("Sorry! You have to choose either 'investment' or 'bond'");