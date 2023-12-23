import re


digit_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def main(file):
    input_lines = read_input(file)
    numbers = get_numbers(input_lines)

    return sum(numbers)


def read_input(file):
    with open(file) as input_file:
        return [x.rstrip('\n') for x in input_file.readlines()]


def get_numbers(lines):
    digits_regex = "|".join(digit_mapping.keys())
    numbers = []

    for line in lines:
        digits = re.findall(rf'(?=({digits_regex}|\d))', line)
        digits = [match for match in digits]
        numbers.append(int(get_digit(digits[0]) + get_digit(digits[-1])))

    return numbers


def get_digit(digit):
    if digit in digit_mapping:
        return digit_mapping[digit]

    return digit


if __name__ == '__main__':
    print(main('input.txt'))
