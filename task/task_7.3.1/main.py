import math


# 7.3.1
class RationalError(ZeroDivisionError):
    """Виняток, що виникає при спробі створити Rational з нульовим знаменником"""
    pass


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
            raise RationalError("Знаменник не може бути нулем")

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
            raise RationalError("Ділення на нуль")
        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"



if __name__ == "__main__":
    print("Тестування RationalError (завдання 7.3.1)")

    # Test 1
    print("\nТест 1: Спробуємо створити дріб з нульовим знаменником (1/0)")
    try:
        r = Rational(1, 0)
        print("Успішно створено:", r)
    except RationalError as e:
        print(f"Спіймано RationalError: {e}")

    # Test 2
    print("\nТест 2: Спробуємо поділити дріб на нуль (1/2 / 0/1)")
    try:
        r1 = Rational(1, 2)
        r2 = Rational(0, 1)
        result = r1 / r2
        print("Результат ділення:", result)
    except RationalError as e:
        print(f"Спіймано RationalError: {e}")

