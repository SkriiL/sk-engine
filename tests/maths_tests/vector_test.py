import unittest


from maths import Vector, Matrix


class VectorTest(unittest.TestCase):
    def test_unit(self):
        self.assertEqual(Vector.unit(), Vector(1, 1, 1))

    def test_add(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)
        self.assertEqual(v1 + v2, Vector(4, 4, 4))
        v1 += v2
        self.assertEqual(v1, Vector(4, 4, 4))

    def test_sub(self):
        v1 = Vector(3, 2, 1)
        v2 = Vector(5, 4, 3)
        self.assertEqual(v1 - v2, Vector(-2, -2, -2))
        v1 -= v2
        self.assertEqual(v1, Vector(-2, -2, -2))

    def test_scalar_multiplication(self):
        v1 = Vector.unit()
        self.assertEqual(v1 * 3, Vector(3, 3, 3))
        v1 *= 3
        self.assertEqual(v1, Vector(3, 3, 3))

    def test_scalar_division(self):
        v1 = Vector(3, 3, 3)
        self.assertEqual(v1 / 3, Vector.unit())
        v1 /= 3
        self.assertEqual(v1, Vector.unit())

    def test_dot_product(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)
        self.assertEqual(v1.dot(v2), 10)

    def test_cross_product(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)
        self.assertEqual(v1 * v2, Vector(-4, 8, -4))
        v1 *= v2
        self.assertEqual(v1, Vector(-4, 8, -4))

    def test_magnitude(self):
        v1 = Vector(4, 3, 0)
        self.assertEqual(abs(v1), 5)

    def test_matrix_vector_multiplication(self):
        m = Matrix(1, 0, 0, 0, 0, -1, 0, 1, 0)
        v = Vector(0, 1, 0)
        self.assertEqual(v * m, Vector(0, 0, 1))
        v *= m
        self.assertEqual(v, Vector(0, 0, 1))


if __name__ == '__main__':
    unittest.main()
