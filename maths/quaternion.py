import maths


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


if __name__ == "__main__":
    q = Quaternion(90, maths.Vector(1, 1, 1))
    print(q)