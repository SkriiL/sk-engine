import math

import maths
from errors import SkTypeError


class Quaternion:
    def __init__(self, scalar: float, vector: maths.Vector):
        self.scalar: float = scalar
        self.vector: maths.Vector = vector

    def __eq__(self, other) -> bool:
        if isinstance(other, Quaternion):
            return self.scalar == other.scalar and self.vector == other.vector
        return False

    def __str__(self) -> str:
        return f"Quaternion({self.scalar}, {self.vector})"

    def __add__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            return Quaternion(self.scalar + other.scalar, self.vector + other.vector)
        raise SkTypeError(self, other, "+")

    def __iadd__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            self.scalar += other.scalar
            self.vector += other.vector
            return self
        raise SkTypeError(self, other, "+=")

    def __sub__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            return Quaternion(self.scalar - other.scalar, self.vector - other.vector)
        raise SkTypeError(self, other, "-")

    def __isub__(self, other) -> "Quaternion":
        if isinstance(other, Quaternion):
            self.scalar -= other.scalar
            self.vector -= other.vector
            return self
        raise SkTypeError(self, other, "-=")

    def __mul__(self, other) -> "Quaternion":
        if isinstance(other, (int, float)):
            return Quaternion(other * self.scalar, self.vector * other)
        if isinstance(other, Quaternion):
            scalar = self.scalar * other.scalar - self.vector.dot(other.vector)
            vector = other.vector * self.scalar + self.vector * other.scalar + self.vector * other.vector
            return Quaternion(scalar, vector)
        raise SkTypeError(self, other, "*")

    def __imul__(self, other) -> "Quaternion":
        if isinstance(other, (int, float)):
            self.scalar *= other
            self.vector *= other
        if isinstance(other, Quaternion):
            scalar_tmp = self.scalar
            self.scalar = self.scalar * other.scalar - self.vector.dot(other.vector)
            self.vector = other.vector * scalar_tmp + self.vector * other.scalar + self.vector * other.vector
            return self
        raise SkTypeError(self, other, "*=")

    def __truediv__(self, other) -> "Quaternion":
        if isinstance(other, (int, float)):
            return Quaternion(other / self.scalar, self.vector / other)
        raise SkTypeError(self, other, "/")

    def __itruediv__(self, other) -> "Quaternion":
        if isinstance(other, (int, float)):
            self.scalar /= other
            self.vector /= other
            return self
        raise SkTypeError(self, other, "/")

    def __abs__(self) -> float:
        return math.sqrt(self.scalar * self.scalar + self.vector.dot(self.vector))

    def normalize(self) -> "Quaternion":
        return self / abs(self)

    def conjugate(self) -> "Quaternion":
        return Quaternion(self.scalar, self.vector * (-1))

    def inverse(self) -> "Quaternion":
        return self.conjugate() / (abs(self) ** 2)

    def rotate_vector(self, vector: maths.Vector) -> maths.Vector:
        p = Quaternion(0, vector)
        q = self.normalize()
        i = q.inverse()
        rotated = q * p * i
        return rotated.vector


if __name__ == "__main__":
    q = Quaternion(90, maths.Vector(1, 1, 1))
    print(q)