def process_data(input_string):
    try:
        num = int(input_string)
        div = 100/num
        return div
    except ValueError:
        print("Input must be a number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except:
        print("An unexpected error occured!")