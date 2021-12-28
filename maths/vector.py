from errors import SkTypeError


class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x: float = x
        self.y: float = y
        self.z: float = z

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

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            raise SkTypeError(self, other, "+=")

    def __sub__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise SkTypeError(self, other, "-")

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            raise SkTypeError(self, other, "-=")

    def __mul__(self, other) -> "Vector":
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other, self.z * other)
        raise SkTypeError(self, other, "*")

    def __imul__(self, other):
        if isinstance(other, (float, int)):
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            raise SkTypeError(self, other, "*=")

    def __truediv__(self, other) -> "Vector":
        if isinstance(other, (float, int)):
            return Vector(self.x / other, self.y / other, self.z / other)
        raise SkTypeError(self, other, "/")

    def __itruediv__(self, other):
        if isinstance(other, (float, int)):
            self.x /= other
            self.y /= other
            self.z /= other
        else:
            raise SkTypeError(self, other, "/=")

    def dot(self, other) -> float or int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise SkTypeError(self, other, "dot")


if __name__ == "__main__":
    v = Vector(1, 1, 1)
    print(v * 3)