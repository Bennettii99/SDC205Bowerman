# Simple Math Calculator Program
# This program does some basic math stuff with two numbers

# Get the user's info
user_name = input("Please enter your name: ")
student_id = input("Please enter your Student ID: ")

# Ask for two numbers
num1 = int(input("Please enter a whole number: "))
num2 = int(input("Please enter a different second whole number: "))

# Do the three math operations - I picked multiplication, division, and addition
multiply_result = num1 * num2
divide_result = num1 / num2
add_result = num1 + num2

# Show the results with 2 decimal places
print(f"The result of {num1} times {num2} is: {multiply_result:.2f}")
print(f"The result of {num1} divided by {num2} is: {divide_result:.2f}")
print(f"The result of {num1} plus {num2} is: {add_result:.2f}")

# Figure out which number is bigger
if num1 > num2:
    print(f"Number 1 is larger than Number 2")
else:
    print(f"Number 1 is smaller than Number 2")

# Print my info
print(user_name)
print(student_id)
