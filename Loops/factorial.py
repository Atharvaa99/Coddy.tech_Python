fact = 1
n = int(input())

if n == 0 or n == 1:
    fact = 1
else:
    for i in range(1,n+1):
        fact *= i

print(fact)