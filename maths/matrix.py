from errors import SkTypeError


class Matrix:
    """
    Column mayor implementation
    0 3 6
    1 4 7
    2 5 8
    """

    def __init__(self, m0: float, m3: float, m6: float, m1: float, m4: float, m7: float, m2: float, m5: float,
                 m8: float):
        self._data = [m0, m1, m2, m3, m4, m5, m6, m7, m8]

    def __eq__(self, other) -> bool:
        if isinstance(other, Matrix):
            for i in range(0, len(self._data)):
                if self._data[i] != other._data[i]:
                    return False
            return True
        return False

    def __str__(self) -> str:
        return f"Matrix({self._data[0]} {self._data[3]} {self._data[6]})\n" \
               f"      ({self._data[1]} {self._data[4]} {self._data[7]})\n" \
               f"      ({self._data[2]} {self._data[5]} {self._data[8]})"


if __name__ == "__main__":
    print(Matrix(1, 1, 1, 1, 1, 1, 1, 1, 1))