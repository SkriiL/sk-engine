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
        raise TypeError(
            f"unsupported operand type(s) for +: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        raise TypeError(
            f"unsupported operand type(s) for +=: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __sub__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError(
            f"unsupported operand type(s) for -: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        raise TypeError(
            f"unsupported operand type(s) for -=: '{self.__class__.__name__}' and '{other.__class__.__name__}'")
