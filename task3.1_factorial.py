# Function to calculate factorial using a loop
def factorial(num):
    """
    This function takes a number as an argument
    and returns its factorial.
    """
    result = 1

    # Loop from 1 to num (inclusive)
    for i in range(1, num + 1):
        result = result * i

    return result


# Taking input from the user
number = int(input("Enter a number: "))

# Calling the factorial function
fact = factorial(number)

# Printing the result
print("Factorial of", number, "is:", fact)