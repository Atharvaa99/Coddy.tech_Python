def print_sequence(n):
    if n == 0:
        print("Blast off!")
    else:
        print(f"T-minus {n}")
        print_sequence(n-1)