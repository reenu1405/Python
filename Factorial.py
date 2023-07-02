# factorial
write a Python function which takes a positive number as input and
# return the factorial of the number.
def getfact(n):
    if n < 0:
        return " Error: Number must be +ve"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
num = int(input("Enter a positive number : "))
fact = getfact(num)
print("The factorial of {} is: {}".format(num, fact))
print(f"The factorial1 of {num} is: {fact}")
