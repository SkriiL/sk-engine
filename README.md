# sk-engine

A WIP game engine written in Python

## Documentation

### Math Engine
The maths package can be accessed like this:
```python
import maths
```

#### Vector
```python
from maths import Vector
```

Vector initialization
```python
v1 = Vector(1, 2, 3)
```

Unit Vector
```python
v2 = Vector.unit()
```

Vector Addition and Subtraction
```python
v3 = v1 - v2
v3 += Vector(3, 2, 1)
```

Scalar Multiplication and Division (always use the Vector object as the first operand)
```python
v4 = 3 * v3
v4 /= 2
```

Dot Product
```python
d = v4.dot(v3)
```

Cross Product
```python
v5 = v1 * v2
v5 *= v3
```

Magnitude
```python
abs(v5)
```
