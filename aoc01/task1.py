import re


def main(file):
    input_lines = read_input(file)
    numbers = get_numbers(input_lines)

    return sum(numbers)


def read_input(file):
    with open(file) as input_file:
        return [x.rstrip('\n') for x in input_file.readlines()]


def get_numbers(lines):
    numbers = []

    for line in lines:
        digits = re.findall(r'\d', line)
        numbers.append(int(digits[0] + digits[-1]))

    return numbers


if __name__ == '__main__':
    print(main('input.txt'))
