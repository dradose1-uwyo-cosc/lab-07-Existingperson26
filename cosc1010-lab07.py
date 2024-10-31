# Peter Martinez
# UWYO COSC 1010
# Submission Date 10/31/2024
# Lab 07
# Lab Section: 12
# Sources, people worked with, help given to: Cole Jordan helped me on the last part because it was too confusing
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

factorial = 1
instance = 1
upBound = input("Please input an upper boundary")
upBound = int(upBound)
while instance <= upBound:
    factorial *= instance
    instance += 1
    ## print(factorial)

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
active = True
totalSum = 0
while active:
    sumAsk = input("Please insert a number to be added. Type 'exit' to stop the program.").lower()
    if sumAsk != "exit":
        if sumAsk.startswith("-"):
            sumAsk.removeprefix("-")
            totalSum += int(sumAsk)
            print(sumAsk)
        elif sumAsk.isdigit():
            if sumAsk.isdigit():
                totalSum += int(sumAsk)
            else:
                print("Enter a real number!")
                continue
    else:
        active = False
        

print(f"Your final sum is {totalSum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

active = True
def add(num1, num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def mult(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def rem(num1,num2):
    return num1%num2

while active:
    equAsk = input("Please input an equation")
    if equAsk.lower() != "exit":
        operator = ""
        check = False
        for num in equAsk:
            if not num.isdigit():
                if num == "+" or num == "-" or num == "*" or num == "/" or num == "%":
                    operator = num
                elif num == " ":
                    equAsk.replace("", '')
                else:
                    "Please input something else"
                    check = True
    if check == True:
        continue

    equation = equAsk.split(operator)

    equation[0] = int(equation[0])
    equation[1] = int(equation[1])

    answer = 0

    if operator == "+":
        answer = add(equation[0], equation[1])
    elif operator == "-":
        answer = subtract(equation[0], equation[1])
    elif operator == "*":
        answer = mult(equation[0], equation[1])
    elif operator == "/":
        answer = div(equation[0], equation[1])
    elif operator == "%":
        answer = rem(equation[0], equation[1])

    print(f"The answer to the equation given is {answer}")

