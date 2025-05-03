import math
import os
from collections import deque


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            if '/' in numerator:
                n, d = map(int, numerator.split('/'))
            else:
                n, d = int(numerator), 1
        else:
            n, d = numerator, denominator

        if d == 0:
            raise ZeroDivisionError("Знаменник не може бути нулем")

        common_divisor = math.gcd(abs(n), abs(d))
        self.n = n // common_divisor
        self.d = d // common_divisor

        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if other.n == 0:
            raise ZeroDivisionError("Ділення на нуль")
        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"


def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    tokens = expression.split()
    for token in tokens:
        if token.replace('/', '').isdigit() or ('/' in token and all(p.isdigit() for p in token.split('/'))):
            output.append(token)
        elif token in precedence:
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        output.append(operators.pop())

    return output


def evaluate_rpn(rpn):
    stack = []
    for token in rpn:
        if token.replace('/', '').isdigit() or ('/' in token and all(p.isdigit() for p in token.split('/'))):
            stack.append(Rational(token))
        else:
            try:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
            except IndexError:
                raise ValueError("Невірна кількість операндів для операції")
            except ZeroDivisionError:
                raise ValueError("Спроба ділення на нуль")

    if len(stack) != 1:
        raise ValueError("Невірний вираз")

    return stack[0]


def main():
    input_file = "input01.txt"
    output_file = "output1.txt"

    if not os.path.exists(input_file):
        print(f"Помилка: файл {input_file} не знайдено!")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f_in, \
                open(output_file, 'w', encoding='utf-8') as f_out:

            for line in f_in:
                line = line.strip()
                if line:
                    try:
                        rpn = shunting_yard(line)
                        result = evaluate_rpn(rpn)
                        f_out.write(f"{result}\n")
                        print(f"Результат: {result}")
                    except Exception as e:
                        error_msg = f"Помилка у виразі '{line}': {str(e)}"
                        f_out.write(f"{error_msg}\n")
                        print(error_msg)

        print(f"Результати збережено у файл {output_file}")

    except Exception as e:
        print(f"Помилка при роботі з файлами: {str(e)}")


if __name__ == "__main__":
    main()


class RationalError(ZeroDivisionError):
    pass


# Example
if __name__ == "__main__":
    try:
        r = Rational(1, 0)
    except RationalError as e:
        print(f"Спіймано RationalError: {e}")
