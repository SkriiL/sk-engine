import math

import maths
from errors import SkTypeError


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x: float = x
        self.y: float = y
        self.z: float = z

    @staticmethod
    def unit() -> "Vector":
        return Vector(1, 1, 1)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __add__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise SkTypeError(self, other, "+")

    def __iadd__(self, other) -> "Vector":
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        raise SkTypeError(self, other, "+=")

    def __sub__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise SkTypeError(self, other, "-")

    def __isub__(self, other) -> "Vector":
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        raise SkTypeError(self, other, "-=")

    def __mul__(self, other) -> "Vector":
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        if isinstance(other, Vector):
            return Vector(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        if isinstance(other, maths.Matrix):
            return Vector(self.x * other.data[0] + self.y * other.data[3] + self.z * other.data[6],
                          self.x * other.data[1] + self.y * other.data[4] + self.z * other.data[7],
                          self.x * other.data[2] + self.y * other.data[5] + self.z * other.data[8])
        raise SkTypeError(self, other, "*")

    def __imul__(self, other) -> "Vector":
        if isinstance(other, (float, int)):
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        x_tmp = self.x
        y_tmp = self.y
        z_tmp = self.z
        if isinstance(other, Vector):
            self.x = y_tmp * other.z - z_tmp * other.y
            self.y = z_tmp * other.x - x_tmp * other.z
            self.z = x_tmp * other.y - y_tmp * other.x
            return self
        if isinstance(other, maths.Matrix):
            self.x = x_tmp * other.data[0] + y_tmp * other.data[3] + z_tmp * other.data[6]
            self.y = x_tmp * other.data[1] + y_tmp * other.data[4] + z_tmp * other.data[7]
            self.z = x_tmp * other.data[2] + y_tmp * other.data[5] + z_tmp * other.data[8]
            return self
        raise SkTypeError(self, other, "*=")

    def __truediv__(self, other) -> "Vector":
        if isinstance(other, (float, int)):
            return Vector(self.x / other, self.y / other, self.z / other)
        raise SkTypeError(self, other, "/")

    def __itruediv__(self, other) -> "Vector":
        if isinstance(other, (float, int)):
            self.x /= other
            self.y /= other
            self.z /= other
            return self
        raise SkTypeError(self, other, "/=")

    def dot(self, other) -> float or int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise SkTypeError(self, other, "dot")

    def __abs__(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def rotate(self, q: maths.Quaternion) -> "Vector":
        p: maths.Quaternion = maths.Quaternion(0, self)
        q = q.normalize()
        i = q.inverse()
        rotated = q * p * i
        return rotated.vector
