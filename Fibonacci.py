# Fibonacci

# write a function called generate_fibonacci that takes an integer n as input and
# returns a list of the first n Fibonacci numbers.
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def generate_fibonacci(n):
    fib_list = []
    if n >= 1:
        fib_list.append(0)
    if n >= 2:
        fib_list.append(1)
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])

    return fib_list

fib_n = int(input("Enter an integer: "))
fib_res = generate_fibonacci(fib_n)
print(f"Fibonacci number series for n= {fib_n} : ", fib_res)
