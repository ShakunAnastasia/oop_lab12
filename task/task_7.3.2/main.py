import math
import os
from collections import deque


# 7.3.1
class RationalError(ZeroDivisionError):
    pass


# 7.3.2
class RationalValueError(ValueError):
    pass


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            if '/' in numerator:
                try:
                    n, d = map(int, numerator.split('/'))
                except ValueError:
                    raise RationalValueError("Невірний формат рядка для Rational")
            else:
                try:
                    n, d = int(numerator), 1
                except ValueError:
                    raise RationalValueError("Невірний формат рядка для Rational")
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
        if not isinstance(other, (Rational, int)):
            raise RationalValueError("Можна додавати лише Rational або цілі числа")
        if isinstance(other, int):
            other = Rational(other)
        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        if not isinstance(other, (Rational, int)):
            raise RationalValueError("Можна віднімати лише Rational або цілі числа")
        if isinstance(other, int):
            other = Rational(other)
        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        if not isinstance(other, (Rational, int)):
            raise RationalValueError("Можна множити лише Rational або цілі числа")
        if isinstance(other, int):
            other = Rational(other)
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __truediv__(self, other):
        if not isinstance(other, (Rational, int)):
            raise RationalValueError("Можна ділити лише Rational або цілі числа")
        if isinstance(other, int):
            other = Rational(other)
        if other.n == 0:
            raise RationalError("Ділення на нуль")
        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    def __eq__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.n == other.n and self.d == other.d

    def __lt__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.n * other.d < other.n * self.d

    def __le__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.n * other.d <= other.n * self.d

    def __gt__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.n * other.d > other.n * self.d

    def __ge__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        return self.n * other.d >= other.n * self.d

    def __neg__(self):
        return Rational(-self.n, self.d)

    def __abs__(self):
        return Rational(abs(self.n), abs(self.d))

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"

    def __repr__(self):
        return f"Rational({self.n}, {self.d})"


if __name__ == "__main__":
    print("=" * 50)
    print("Демонстрація роботи винятків для класу Rational")
    print("=" * 50)


    print("\nТест 1: Спробуємо створити дріб з нульовим знаменником")
    try:
        r = Rational(1, 0)
        print("Успішно створено:", r)
    except RationalError as e:
        print(f" Спіймано RationalError: {e}")
    except Exception as e:
        print(f" Спіймано інший виняток: {type(e).__name__}: {e}")
    else:
        print(" Помилка не виникла")
    finally:
        print("Тест завершено")


    print("\nТест 2: Спробуємо створити дріб з невірного формату рядка '1/a'")
    try:
        r = Rational("1/a")
        print("Успішно створено:", r)
    except RationalValueError as e:
        print(f" Спіймано RationalValueError: {e}")
    except Exception as e:
        print(f" Спіймано інший виняток: {type(e).__name__}: {e}")
    else:
        print(" Помилка не виникла")
    finally:
        print("Тест завершено")


    print("\nТест 3: Спробуємо додати дріб і рядок 'not_a_number'")
    try:
        r1 = Rational(1, 2)
        r2 = "not_a_number"
        result = r1 + r2
        print("Результат додавання:", result)
    except RationalValueError as e:
        print(f" Спіймано RationalValueError: {e}")
    except Exception as e:
        print(f" Спіймано інший виняток: {type(e).__name__}: {e}")
    else:
        print(" Помилка не виникла")
    finally:
        print("Тест завершено")


    print("\nТест 4: Коректні операції з дробами")
    try:
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        print(f"Створено дроби: {r1} і {r2}")

        print("\nДодавання:")
        result = r1 + r2
        print(f"{r1} + {r2} = {result}")

        print("\nВіднімання:")
        result = r1 - r2
        print(f"{r1} - {r2} = {result}")

        print("\nМноження:")
        result = r1 * r2
        print(f"{r1} * {r2} = {result}")

        print("\nДілення:")
        result = r1 / r2
        print(f"{r1} / {r2} = {result}")

    except RationalError as e:
        print(f" Спіймано RationalError: {e}")
    except RationalValueError as e:
        print(f" Спіймано RationalValueError: {e}")
    except Exception as e:
        print(f" Спіймано інший виняток: {type(e).__name__}: {e}")
    else:
        print("\n Всі операції виконані успішно")
    finally:
        print("\nТест завершено")
