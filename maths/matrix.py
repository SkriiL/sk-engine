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

    @staticmethod
    def identity() -> "Matrix":
        return Matrix(1, 0, 0, 0, 1, 0, 0, 0, 1)

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

    def __add__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            return Matrix(
                self._data[0] + other._data[0], self._data[3] + other._data[3], self._data[6] + other._data[6],
                self._data[1] + other._data[1], self._data[4] + other._data[4], self._data[7] + other._data[7],
                self._data[2] + other._data[2], self._data[5] + other._data[5], self._data[8] + other._data[8],
            )
        raise SkTypeError(self, other, "+")

    def __iadd__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            for i in range(0, len(self._data)):
                self._data[i] += other._data[i]
            return self
        raise SkTypeError(self, other, "+=")

    def __sub__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            return Matrix(
                self._data[0] - other._data[0], self._data[3] - other._data[3], self._data[6] - other._data[6],
                self._data[1] - other._data[1], self._data[4] - other._data[4], self._data[7] - other._data[7],
                self._data[2] - other._data[2], self._data[5] - other._data[5], self._data[8] - other._data[8],
            )
        raise SkTypeError(self, other, "-")

    def __isub__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            for i in range(0, len(self._data)):
                self._data[i] -= other._data[i]
            return self
        raise SkTypeError(self, other, "-=")

    def __mul__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            return Matrix(self._data[0] * other, self._data[3] * other, self._data[6] * other,
                          self._data[1] * other, self._data[4] * other, self._data[7] * other,
                          self._data[2] * other, self._data[5] * other, self._data[8] * other,)
        if isinstance(other, Matrix):
            return Matrix(
                self._data[0] * other._data[0] + self._data[3] * other._data[1] + self._data[6] * other._data[2],
                self._data[0] * other._data[3] + self._data[3] * other._data[4] + self._data[6] * other._data[5],
                self._data[0] * other._data[6] + self._data[3] * other._data[7] + self._data[6] * other._data[8],
                self._data[1] * other._data[0] + self._data[4] * other._data[1] + self._data[7] * other._data[2],
                self._data[1] * other._data[3] + self._data[4] * other._data[4] + self._data[7] * other._data[5],
                self._data[1] * other._data[6] + self._data[4] * other._data[7] + self._data[7] * other._data[8],
                self._data[2] * other._data[0] + self._data[5] * other._data[1] + self._data[8] * other._data[2],
                self._data[2] * other._data[3] + self._data[5] * other._data[4] + self._data[8] * other._data[5],
                self._data[2] * other._data[6] + self._data[5] * other._data[7] + self._data[8] * other._data[8],
            )
        raise SkTypeError(self, other, "*")

    def __imul__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            for i in range(0, len(self._data)):
                self._data[i] += other
            return self
        if isinstance(other, Matrix):
            self._data[0] = self._data[0] * other._data[0] + self._data[3] * other._data[1] + self._data[6] * other._data[2]
            self._data[3] = self._data[0] * other._data[3] + self._data[3] * other._data[4] + self._data[6] * other._data[5]
            self._data[6] = self._data[0] * other._data[6] + self._data[3] * other._data[7] + self._data[6] * other._data[8]
            self._data[1] = self._data[1] * other._data[0] + self._data[4] * other._data[1] + self._data[7] * other._data[2]
            self._data[4] = self._data[1] * other._data[3] + self._data[4] * other._data[4] + self._data[7] * other._data[5]
            self._data[7] = self._data[1] * other._data[6] + self._data[4] * other._data[7] + self._data[7] * other._data[8]
            self._data[2] = self._data[2] * other._data[0] + self._data[5] * other._data[1] + self._data[8] * other._data[2]
            self._data[5] = self._data[2] * other._data[3] + self._data[5] * other._data[4] + self._data[8] * other._data[5]
            self._data[8] = self._data[2] * other._data[6] + self._data[5] * other._data[7] + self._data[8] * other._data[8]
            return self
        raise SkTypeError(self, other, "*=")

    def __truediv__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            return Matrix(self._data[0] / other, self._data[3] / other, self._data[6] / other,
                          self._data[1] / other, self._data[4] / other, self._data[7] / other,
                          self._data[2] / other, self._data[5] / other, self._data[8] / other, )
        raise SkTypeError(self, other, "/")

    def __itruediv__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            for i in range(0, len(self._data)):
                self._data[i] /= other
            return self
        raise SkTypeError(self, other, "/=")

    def transpose(self) -> "Matrix":
        return Matrix(self._data[0], self._data[1], self._data[2],
                      self._data[3], self._data[4], self._data[5],
                      self._data[6], self._data[7], self._data[8])


if __name__ == "__main__":
    print(Matrix(1, 1, 1, 1, 1, 1, 1, 1, 1))