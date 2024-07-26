def is_armstrong_number(number):
    num_str = str(number)

    # Get the number of digits
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum equals the original number
    return armstrong_sum == number
