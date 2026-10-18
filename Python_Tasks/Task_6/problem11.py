# Problem: String Formatting
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Code:
def print_formatted(number):
    width = len(format(number, 'b'))

    for i in range(1, number + 1):
        decimal = format(i, 'd')
        octal = format(i, 'o')
        hexadecimal = format(i, 'X')
        binary = format(i, 'b')

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexadecimal.rjust(width),
            binary.rjust(width)
    )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
