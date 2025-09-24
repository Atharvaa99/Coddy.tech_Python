def sum_digits(n):
    if n < 10:
        return n
    else:
        sum = n % 10 + sum_digits(n//10)
        return sum
