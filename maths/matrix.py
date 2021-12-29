import maths
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
        self.data = [m0, m1, m2, m3, m4, m5, m6, m7, m8]

    @staticmethod
    def identity() -> "Matrix":
        return Matrix(1, 0, 0, 0, 1, 0, 0, 0, 1)

    def __eq__(self, other) -> bool:
        if isinstance(other, Matrix):
            for i in range(0, len(self.data)):
                if self.data[i] - other.data[i] > 0.0000000001:
                    return False
            return True
        return False

    def __str__(self) -> str:
        return f"Matrix({self.data[0]} {self.data[3]} {self.data[6]})\n" \
               f"      ({self.data[1]} {self.data[4]} {self.data[7]})\n" \
               f"      ({self.data[2]} {self.data[5]} {self.data[8]})"

    def __add__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            return Matrix(
                self.data[0] + other.data[0], self.data[3] + other.data[3], self.data[6] + other.data[6],
                self.data[1] + other.data[1], self.data[4] + other.data[4], self.data[7] + other.data[7],
                self.data[2] + other.data[2], self.data[5] + other.data[5], self.data[8] + other.data[8],
            )
        raise SkTypeError(self, other, "+")

    def __iadd__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            for i in range(0, len(self.data)):
                self.data[i] += other.data[i]
            return self
        raise SkTypeError(self, other, "+=")

    def __sub__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            return Matrix(
                self.data[0] - other.data[0], self.data[3] - other.data[3], self.data[6] - other.data[6],
                self.data[1] - other.data[1], self.data[4] - other.data[4], self.data[7] - other.data[7],
                self.data[2] - other.data[2], self.data[5] - other.data[5], self.data[8] - other.data[8],
            )
        raise SkTypeError(self, other, "-")

    def __isub__(self, other) -> "Matrix":
        if isinstance(other, Matrix):
            for i in range(0, len(self.data)):
                self.data[i] -= other.data[i]
            return self
        raise SkTypeError(self, other, "-=")

    def __mul__(self, other) -> "Matrix" or "maths.Vector":
        if isinstance(other, (int, float)):
            return Matrix(self.data[0] * other, self.data[3] * other, self.data[6] * other,
                          self.data[1] * other, self.data[4] * other, self.data[7] * other,
                          self.data[2] * other, self.data[5] * other, self.data[8] * other)
        if isinstance(other, Matrix):
            return Matrix(
                self.data[0] * other.data[0] + self.data[3] * other.data[1] + self.data[6] * other.data[2],
                self.data[0] * other.data[3] + self.data[3] * other.data[4] + self.data[6] * other.data[5],
                self.data[0] * other.data[6] + self.data[3] * other.data[7] + self.data[6] * other.data[8],
                self.data[1] * other.data[0] + self.data[4] * other.data[1] + self.data[7] * other.data[2],
                self.data[1] * other.data[3] + self.data[4] * other.data[4] + self.data[7] * other.data[5],
                self.data[1] * other.data[6] + self.data[4] * other.data[7] + self.data[7] * other.data[8],
                self.data[2] * other.data[0] + self.data[5] * other.data[1] + self.data[8] * other.data[2],
                self.data[2] * other.data[3] + self.data[5] * other.data[4] + self.data[8] * other.data[5],
                self.data[2] * other.data[6] + self.data[5] * other.data[7] + self.data[8] * other.data[8],
            )
        if isinstance(other, maths.Vector):
            return maths.Vector(self.data[0] * other.x + self.data[3] * other.y + self.data[6] * other.z,
                                self.data[1] * other.x + self.data[4] * other.y + self.data[7] * other.z,
                                self.data[2] * other.x + self.data[5] * other.y + self.data[8] * other.z)
        raise SkTypeError(self, other, "*")

    def __imul__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            for i in range(0, len(self.data)):
                self.data[i] *= other
            return self
        if isinstance(other, Matrix):
            tmp = self.data.copy()
            self.data[0] = tmp[0] * other.data[0] + tmp[3] * other.data[1] + tmp[6] * other.data[2]
            self.data[3] = tmp[0] * other.data[3] + tmp[3] * other.data[4] + tmp[6] * other.data[5]
            self.data[6] = tmp[0] * other.data[6] + tmp[3] * other.data[7] + tmp[6] * other.data[8]
            self.data[1] = tmp[1] * other.data[0] + tmp[4] * other.data[1] + tmp[7] * other.data[2]
            self.data[4] = tmp[1] * other.data[3] + tmp[4] * other.data[4] + tmp[7] * other.data[5]
            self.data[7] = tmp[1] * other.data[6] + tmp[4] * other.data[7] + tmp[7] * other.data[8]
            self.data[2] = tmp[2] * other.data[0] + tmp[5] * other.data[1] + tmp[8] * other.data[2]
            self.data[5] = tmp[2] * other.data[3] + tmp[5] * other.data[4] + tmp[8] * other.data[5]
            self.data[8] = tmp[2] * other.data[6] + tmp[5] * other.data[7] + tmp[8] * other.data[8]
            return self
        raise SkTypeError(self, other, "*=")

    def __truediv__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            return Matrix(self.data[0] / other, self.data[3] / other, self.data[6] / other,
                          self.data[1] / other, self.data[4] / other, self.data[7] / other,
                          self.data[2] / other, self.data[5] / other, self.data[8] / other, )
        raise SkTypeError(self, other, "/")

    def __itruediv__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            for i in range(0, len(self.data)):
                self.data[i] /= other
            return self
        raise SkTypeError(self, other, "/=")

    def transpose(self) -> "Matrix":
        return Matrix(self.data[0], self.data[1], self.data[2],
                      self.data[3], self.data[4], self.data[5],
                      self.data[6], self.data[7], self.data[8])

    def determinant(self) -> "float":
        det0 = self.data[0] * (self.data[4] * self.data[8] - self.data[5] * self.data[7])
        det1 = self.data[1] * (self.data[3] * self.data[8] - self.data[5] * self.data[6])
        det2 = self.data[2] * (self.data[3] * self.data[7] - self.data[4] * self.data[6])
        return det0 - det1 + det2

    def adjugate(self) -> "Matrix":
        return Matrix(self.data[4] * self.data[8] - self.data[5] * self.data[7],
                      self.data[6] * self.data[5] - self.data[3] * self.data[8],
                      self.data[3] * self.data[7] - self.data[6] * self.data[4],
                      self.data[7] * self.data[2] - self.data[1] * self.data[8],
                      self.data[0] * self.data[8] - self.data[6] * self.data[2],
                      self.data[6] * self.data[1] - self.data[0] * self.data[7],
                      self.data[1] * self.data[5] - self.data[4] * self.data[2],
                      self.data[3] * self.data[2] - self.data[0] * self.data[5],
                      self.data[0] * self.data[4] - self.data[3] * self.data[1])

    def inverse(self) -> "Matrix":
        return self.adjugate() * (1 / self.determinant())
