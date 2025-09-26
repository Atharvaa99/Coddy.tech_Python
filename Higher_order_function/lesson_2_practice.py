def prime_helper_function(x):
    if x <= 1:
        return False
  
    for i in range(2,int((x** 0.5)+1)):
        if x % i == 0:
             return  False
    return True

            
def get_prime_numbers(numbers):
    filter_numbers = filter(prime_helper_function, numbers )
    return list(filter_numbers)