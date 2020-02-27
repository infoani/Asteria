import argparse
from constant import *
from combination_algorithms import *

# other helper functions
def _convert_number_to_digits(num):
    digits = []
    while (num):
        last_digit = num % 10
        digits.append(last_digit)
        num //= 10
    return digits[::-1]

def char_from_number(number):
    number_arr = _convert_number_to_digits(number)
    return [keypad_num_char_map[x] for x in number_arr]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest='number', help="Provide the Keypad number to be dialed")
    parser.add_argument('--recurse', action='store_true', help="Specify if ")

    args = parser.parse_args()

    input_number = int(args.number)
    char_arr = char_from_number(input_number)

    com_o = CombineElements()

    if args.recurse:
        cobmination_algo = CombineRecursion
    else:
        cobmination_algo = CombineIteration

    print(*com_o.combination(char_arr, cobmination_algo), sep=", ")