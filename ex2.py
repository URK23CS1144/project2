    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return number == sum_of_digits
number_to_check = int(input("Enter a number to check if it's an Armstrong number: "))
    print(number_to_check, "is an Armstrong number.")
else:
    print(number_to_check, "is not an Armstrong number.")
