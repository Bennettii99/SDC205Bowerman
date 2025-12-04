# performanceAssessmentFunctions.py
# Ishmael Bennett - SDC255 Week 3

def functionOne():
    print("My Student ID is ISHBEN9200")


def functionTwo():
    # Ask user for two numbers
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    
    totalSum = num1 + num2
    
    # Print the sum from inside this function (requirement)
    print(f"The sum of {num1} and {num2} is {totalSum}.")
    
    # Return the sum so main can use it
    return totalSum


def functionThree(sumFromTwo):
    if sumFromTwo > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    
    # Return the numeric part of the Student ID (1234)
    return 1234


def main():
    # Call functionOne - displays the full student ID
    functionOne()
    
    # Call functionTwo, store the returned sum in a variable
    theSum = functionTwo()
    
    # Pass that sum to functionThree and store what it returns
    numericId = functionThree(theSum)
    
    # Display the message showing what functionThree returned
    print(f"functionThree returned the value of {numericId}.")


# Start the program
main()