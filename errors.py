from typing import Any


class SkTypeError(TypeError):
    def __init__(self, type1: Any, type2: Any, operator: str):
        self.message: str = f"unsupported operand type(s) for {operator}: '{type1.__class__.__name__}' and '{type2.__class__.__name__}'"
        super(SkTypeError, self).__init__(self.message)
