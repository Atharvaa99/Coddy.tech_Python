def fibonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib