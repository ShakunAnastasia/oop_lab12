import math


class RationalError(ZeroDivisionError):
    pass


class RationalValueError(ValueError):
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

    def __str__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"


class RationalList(list):
    def __init__(self, iterable=None):
        if iterable is None:
            super().__init__()
        else:
            self._validate_iterable(iterable)
            super().__init__(iterable)

    def _validate_item(self, item):
        if not isinstance(item, Rational):
            raise RationalValueError(f"Елемент {item} не є раціональним числом")

    def _validate_iterable(self, iterable):
        for item in iterable:
            self._validate_item(item)

    def append(self, item):
        self._validate_item(item)
        super().append(item)

    def extend(self, iterable):
        self._validate_iterable(iterable)
        super().extend(iterable)

    def insert(self, index, item):
        self._validate_item(item)
        super().insert(index, item)

    def __setitem__(self, index, item):
        self._validate_item(item)
        super().__setitem__(index, item)

    def __add__(self, other):
        if isinstance(other, (RationalList, list)):
            self._validate_iterable(other)
            return RationalList(super().__add__(other))
        raise RationalValueError("Можна додавати лише RationalList або список Rational")

    def __iadd__(self, other):
        if isinstance(other, (RationalList, list)):
            self._validate_iterable(other)
            return super().__iadd__(other)
        raise RationalValueError("Можна додавати лише RationalList або список Rational")



if __name__ == "__main__":
    print("Тестування RationalList з RationalValueError")

    try:
        r_list = RationalList([Rational(1, 2), Rational(3, 4)])
        print("Початковий список:", [str(x) for x in r_list])

        print("\nСпроба додати ціле число 5:")
        try:
            r_list.append(5)
        except RationalValueError as e:
            print(f"Спіймано RationalValueError: {e}")

        print("\nСпроба розширити список ['1/2', 3.14]:")
        try:
            r_list.extend([Rational("1/2"), 3.14])
        except RationalValueError as e:
            print(f"Спіймано RationalValueError: {e}")

        print("\nКоректні операції:")
        try:
            r_list.append(Rational(2, 3))
            r_list.extend([Rational(3, 5), Rational(4, 7)])
            print("Оновлений список:", [str(x) for x in r_list])
        except RationalValueError as e:
            print(f"Спіймано RationalValueError: {e}")

    except Exception as e:
        print(f"Несподівана помилка: {e}")
