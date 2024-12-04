'''
Requirements for Each Type of Number to be Valid with Samples

IMEI Number
Length: 15 digits
Validation: Luhn algorithm
Sample: 490154203237518 (Valid IMEI)

ISBN-10 Number
Length: 10 digits
Validation: Sum of the first 9 digits, each multiplied by its position (1-9), modulo 11. The check digit can be 0-9 or 'X'.
Sample: 0306406152 (Valid ISBN-10)

ISBN-13 Number
Length: 13 digits
Validation: Alternating sum of the digits multiplied by 1 or 3, modulo 10.
Sample: 9780306406157 (Valid ISBN-13)

Universal Product Code (UPC)
Length: 12 digits
Validation: Sum of the odd-positioned digits (1-indexed), multiplied by 3, plus the sum of the even-positioned digits, modulo 10.
Sample: 012345678905 (Valid UPC)

Visa Credit Card Number
Length: 16 digits
Validation: Luhn algorithm
Sample: 4111111111111111 (Valid Visa)

MasterCard Number
Length: 16 digits
Validation: Luhn algorithm.
Sample: 5555555555554444 (Valid MasterCard)

American Express (Amex) Card Number
Length: 15 digits
Validation: Luhn algorithm.
Sample: 378282246310005 (Valid Amex)
'''


def main():
    """
    Main function to get the number and type from the user, and validate based on the type.
    """
    number = get_number()
    number_type = get_number_type()
    """
    matching the type given by user and calling the necassary functions
    """
    match number_type:
        case 'a':
            print(check_luhn(number, 15), 'IMEI number')
        case 'b':
            print(check_ISBN10(number), 'ISBN-10 number')
        case 'c':
            print(check_ISBN13(number), 'ISBN-13 number')
        case 'e':
            print(check_upc(number), 'UPC')
        case '1':
            print(check_luhn(number, 16), 'Visa Card number')
        case '2':
            print(check_luhn(number, 16), 'MasterCard number')
        case '3':
            print(check_luhn(number, 15), 'Amex Card number')

def check_ISBN10(isbn):
    """
    Check if the given number is a valid ISBN-10.
    ISBN-10: 10 digits with a special calculation for the check digit.
    """
    if len(isbn) != 10:
        return 'It is not a valid'
    check_digit = isbn[-1]
    digits = isbn[:-1]
    total_sum = 0
    for i in range(9):
        total_sum += int(digits[i]) * (i + 1)
    remainder = total_sum % 11
    if remainder == 10 and check_digit == 'x':
        return 'It is a valid'
    elif remainder == int(check_digit):
        return 'It is a valid'
    else:
        return 'It is not a valid'

def check_ISBN13(isbn):
    """
    Check if the given number is a valid ISBN-13.
    ISBN-13: 13 digits with a specific checksum calculation.
    """
    if len(isbn) != 13:
        return 'It is not a valid'
    check_digit = isbn[-1]
    digits = isbn[:-1]
    total_sum = 0
    for i in range(0, len(digits), 2):
        total_sum += int(digits[i])
    for i in range(1, len(digits), 2):
        total_sum += int(digits[i]) * 3
    result = total_sum % 10
    if result == int(check_digit) or (10 - result) == int(check_digit):
        return 'It is a valid'
    else:
        return 'It is not a valid'

def check_upc(upc):
    """
    Check if the given number is a valid UPC (Universal Product Code).
    UPC: 12 digits with a specific checksum calculation.
    """
    if len(upc) != 12:
        return 'It is not a valid'
    check_digit = int(upc[-1])
    digits = upc[:-1]
    sum_odd = 0
    sum_even = 0
    for i in range(0, len(digits), 2):
        sum_odd += int(digits[i])
    for i in range(1, len(digits), 2):
        sum_even += int(digits[i])
    total_sum = (sum_odd * 3) + sum_even
    if (total_sum + check_digit) % 10 == 0:
        return 'It is a valid'
    else:
        return 'It is not a valid'

def check_luhn(number, length):
    """
    Check if the given number is valid based on the Luhn algorithm.
    Used for credit cards, IMEI, etc.
    """
    if len(number) != length:
        return 'It is not a valid'
    total_sum = 0
    check_digit = number[-1]
    digits_reversed = number[-2::-1]
    for i in range(1, len(digits_reversed), 2):
        total_sum += int(digits_reversed[i])
    for i in range(0, len(digits_reversed), 2):
        digit = int(digits_reversed[i])
        doubled = digit * 2
        total_sum += doubled if doubled <= 9 else doubled - 9
    if (total_sum + int(check_digit)) % 10 == 0:
        return 'It is a valid'
    else:
        return 'It is not a valid'

def get_number():
    """
    Prompt the user to input a number, ensure it is clean, and return it.
    """
    while True:
        number = input('Number: ').strip().replace('-', '').replace(' ', '').lower()
        if number[-1] == 'x':
            if number[:-1].isdigit():
                return number
            else:
                print('Only numerical digits are allowed. Please try again.')
        elif number.isdigit():
            return number
        else:
            print('Only numerical digits are allowed. Please try again.')

def get_number_type():
    """
    Prompt the user to select the type of number for validation and return the type.
    """
    print('Kindly choose the type of number you are trying to verify:\n'
          'a) IMEI\n'
          'b) ISBN-10\n'
          'c) ISBN-13\n'
          'd) Credit Card\n'
          'e) Universal Product Code')
    number_type = input('Choice: ').lower().strip()

    if number_type == 'd':
        print('Kindly specify the Credit Card company:\n'
              '1) Visa\n'
              '2) MasterCard\n'
              '3) Amex')
        number_type = input('Company: ')
    if number_type not in ['a','b','c','d','e','1','2','3']:
        print('Invalid option, try again.')
        return get_number_type()
    return number_type

def continue_input():
    """
    Ask the user if they want to input another number and return True if they choose 'n' for No.
    """
    answer = input('Do you want to input another number? (Y/N) ').strip().lower()
    if answer == 'n':
        return True
    elif answer == 'y':
        return False
    else:
        print('Invalid answer, try again.')
        return continue_input()

if __name__ == '__main__':
    while True:
        main()
        if continue_input():
            break