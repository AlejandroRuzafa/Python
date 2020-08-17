def fibonacci(n):
    """
    fib(1) = 1
    fib(2) = 1
    fib(3) = fib(2) + fib(1)
    fib(4) = fib(3) + fib(2)
    fib(10) = fib(9) + fib(8)

    fib(n) = fib(n - 1) + fib(n - 2)
    """
    if n > 2 :
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 1 
    
    
def factorial(n):
    if n == 1:
        return 1 
    else:
        return n * factorial(n - 1)
