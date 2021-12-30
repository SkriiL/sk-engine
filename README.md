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

Matrix Vector Transformation
```python
m = Matrix(1, 0, 0, 0, -1, 0, 0, 0, 1)
v5 *= m
```

Rotate Vector
```python
q = Quaternion(90, Vector(1, 0, 0))
v6 = v5.rotate(q)
```

#### Matrix
````python
from maths import Matrix
````

Matrix initialization (row mayor)
````python
m1 = Matrix(1, 2, 3, 1, 2, 3, 1, 2, 3)
````

Identity Matrix
```python
m2 = Matrix.identity()
```

Matrix Addition and Subtraction
````python
m3 = m1 + m2
m3 -= m1
````

Scalar Multiplication and Division (always use the Matrix object as the first operand)
```python
m4 = m3 * 3
m4 /= 3
```

Matrix Multiplication
```python
m5 = m3 * m4
```

Matrix Transposition
```python
m6 = m5.transpose()
```

Determinant
````python
d = m6.determinant()
````

Adjugate Matrix
```python
m7 = m6.adjugate()
```

Inverse Matrix
```python
m8 = m7.inverse()
```

#### Quaternion
````python
from maths import Quaternion
````

Quaternion Initialization
````python
q1 = Quaternion(90, Vector(1, 0, 0))
````

Quaternion Addition and Subtraction
```python
q2 = Quaternion(90, Vector(0, 1, 0))
q3 = q1 + q2
q3 -= q2
```

Quaternion Scalar Multiplication and Division (always use the Quaternion object as the first operator)
````python
q4 = q3 * 2
q4 /= 2
````

Quaternion Multiplication
````python
q5 = q4 * q3
````

Quaternion Norm
```python
abs(q5)
```

Normalize
````python
q5.normalize()
````

Unit Normalize (needed for rotation)
```python
q5.unit_normalize()
```

Conjugate Quaternion
````python
q6 = q5.conjugate()
````

Inverse Quaternion
````python
q7 = q6.inverse()
````