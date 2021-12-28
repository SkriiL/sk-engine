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
