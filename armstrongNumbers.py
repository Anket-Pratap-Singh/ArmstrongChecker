"""
Author: John Kear
Version: v1.0
Date: 2/17/2020

Comments:
This program will get an integer input from the user.
The program will then determine if the input number is an Armstrong number.

An Armstrong number is a number with n-digits whose sum of each digit raised
to the nth power is equal to the original number.
EX: 4 has 1 digit. 4^1 = 4 therefore 4 is an Armstrong number.
EX: 10 has 2 digits. 1^2 + 0^2 = 1, therefore 10 is NOT an Armstrong number.
EX: 153 has 3 digits. 1^3 + 5^3 + 3^3 = 153, therefore 153 is an Armstrong number.

To accomplish the task of this program we will first need to determine the number of digits
if the input number. When the number of digits has been found we will need to take each
digit individually and multiply it by itself n times. That value will them need to be added
to the total sum. Once all digits have been multiplied and added to the total sum,
we will compare the total sum to the original input. Print the corresponding messages.
"""

# Variable for the original user input
userNumber = 0
# Variable for copy of user input (we don't want to change the input so it can be used later)
copyNumber = 0
# Variable to hold the number of digits
digits = 0
# Variable to hold the current digit being multiplied
curr = 0
# Variable to hold the total sum
totalSum = 0
# Boolean for user input error checking
isInteger = False
# Value to continue checking numbers
testAgain = True
# Variable for user choice
userCont = 'y'
# Variable for checking user choice
isValid = False

# Print message to let user know purpose of program
print('This program will take an integer input and determine if that number is an Armstrong number.')

# Loop through entire program until user quits
while testAgain:
    # Get user input (user error checking to make sure input is an integer value)
    # Continue to prompt user until a valid input is given
    while not isInteger:
        # This statement will print the prompt for the user and assign their input to the userNumber variable
        userNumber = input("Enter an integer EX: 153: ")
        # The try statement will attempt the desired process, if it fails the except statement will be entered
        try:
            # Here we are checking the user input to make sure it is an integer.
            # This is done by manually trying to cast the input to integer type.
            userNumber = int(userNumber)
            # If the process succeeds we change the value of isInteger to True so that we can exit the while loop
            isInteger = True
            print("You entered:", userNumber)
        except ValueError:
            # If an invalid input is entered, print out an error message.
            # There is no need to change the value of isInteger here because it is already set to False.
            print(
                "The number you entered is not an integer. Make sure you do not include letters, decimals or other "
                "special characters")

    # Now that we have the user input, we need to copy it into our copy variable so that we can manipulate it.
    copyNumber = userNumber

    # Determine the number of digits in the user input value (be sure to only use the copy variable
    # Using a while loop we will divide the number by 10 until the value 0 is reached
    # Note: dividing an integer type by ten returns an integer value. This means that the last number will be dropped.
    # EX: 153 / 10 = 15
    while copyNumber > 0:
        # Using Floor Division, divide the number by 10 to drop the last digit
        # Note: Using regular division will return a decimal value. Floor division must be used to return a whole number
        copyNumber //= 10
        # Increment the number of n digits each time we successfully divide by 10
        digits += 1

    # Because we changed the value of the copied user input while finding the number of digits, we need to recopy the
    # value
    copyNumber = userNumber

    # We now need to determine the total sum of each digit raised to the nth power
    # We use a while loop to repeat this process until all digits in the number have been completed
    while copyNumber != 0:
        # Using the modulus operator, we get the first number and set it to our current variable
        # NOTE: the modulus operator returns the remainder of division
        # EX: 153 % 10 returns the remainder 3. This is then set to the indicated variable.
        curr = copyNumber % 10
        # Using the exponential assignment operator '**=' we raise the current digit to the nth power
        curr **= digits
        # The value is added to the total sum
        totalSum += curr
        # As we did when finding the number of n digits, we divide by 10 here to drop the last digit.
        copyNumber //= 10

    # Now that we have the total sum, we need to compare to the original number.
    # Print an appropriate message.
    if totalSum == userNumber:
        print("The number: ", userNumber, "is an Armstrong number!")
    else:
        print("The number: ", userNumber, "is not an Armstrong number.")

    userCont = input("Would you like to continue? Enter y for yes or n for no: ")
    while not isValid:
        if userCont == 'y':
            # Set testAgain to continue program loop
            testAgain = True
            # Set isValid to True to exit current while loop
            isValid = True
        elif userCont == 'n':
            # Set testAgain to false so the program will end
            testAgain = False
            # Set isValid to True so the current while loop will exit (we could also simply use the break statement)
            isValid = True
        else:
            # Print error message and get the new user input.
            # There is no need to set isValid to False as it is already False
            userCont = input("You enter an invalid value. Please enter y to continue or n to quite: ")

    # Before returning to beginning of program, reset applicable variables so a new number may be tested
    # isInteger must be reset to False so that the error checking loop will be entered
    isInteger = False
    # digits must be reset to start the digit count at 0
    digits = 0
    # totalSum must be reset so the added values will begin at 0
    totalSum = 0
    # isValid must be reset to False so the continuation error checking loop will be entered
    isValid = False

# NOTE: some of the print statements and comments are broken to multiple lines. This is because pycharm has a fixed
# length for the allowed number of characters on a single line.
