
def factorial(num):
    """
    This function calculates the factorial of a number using recursion.
    """
    if num < 0:
        return "Factorial is not defined for negative numbers."
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
try:
    number = int(input("Enter a number: "))
    result = factorial(number)
    print("Factorial of", number, "is:", result)
except ValueError:
    print("Please enter a valid integer.")