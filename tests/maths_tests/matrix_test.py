import unittest


from maths import Matrix, Vector


class MatrixTest(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(Matrix.identity(), Matrix(1, 0, 0, 0, 1, 0, 0, 0, 1))

    def test_addition(self):
        m1 = Matrix(1, 2, 3, 1, 2, 3, 1, 2, 3)
        m2 = Matrix(3, 2, 1, 3, 2, 1, 3, 2, 1)
        res = Matrix(4, 4, 4, 4, 4, 4, 4, 4, 4)
        self.assertEqual(m1 + m2, res)
        m1 += m2
        self.assertEqual(m1, res)

    def test_subtraction(self):
        m1 = Matrix(1, 2, 3, 1, 2, 3, 1, 2, 3)
        m2 = Matrix(3, 4, 5, 3, 4, 5, 3, 4, 5)
        res = Matrix(-2, -2, -2, -2, -2, -2, -2, -2, -2)
        self.assertEqual(m1 - m2, res)
        m1 -= m2
        self.assertEqual(m1, res)

    def test_scalar_multiplication(self):
        m = Matrix.identity()
        res = Matrix(3, 0, 0, 0, 3, 0, 0, 0, 3)
        self.assertEqual(m * 3, res)
        m *= 3
        self.assertEqual(m, res)

    def test_scalar_division(self):
        m = Matrix(3, 0, 0, 0, 3, 0, 0, 0, 3)
        self.assertEqual(m / 3, Matrix.identity())
        m /= 3
        self.assertEqual(m, Matrix.identity())

    def test_matrix_multiplication(self):
        m1 = Matrix(1, 2, 3, 1, 2, 3, 1, 2, 3)
        m2 = Matrix(3, 2, 1, 3, 2, 1, 3, 2, 1)
        res = Matrix(18, 12, 6, 18, 12, 6, 18, 12, 6)
        self.assertEqual(m1 * m2, res)
        m1 *= m2
        self.assertEqual(m1, res)

    def test_transpose(self):
        m = Matrix(1, 2, 3, 1, 2, 3, 1, 2, 3)
        m = m.transpose()
        self.assertEqual(m, Matrix(1, 1, 1, 2, 2, 2, 3, 3, 3))

    def test_determinant(self):
        m = Matrix(1, 2, 3, 3, 2, 1, 2, 3, 1)
        d = m.determinant()
        self.assertEqual(d, 12)

    def test_inverse(self):
        m = Matrix(1, 2, 3, 3, 2, 1, 2, 3, 1)
        m = m.inverse()
        res = Matrix(-1 / 12, 7 / 12, -1 / 3, -1 / 12, -5 / 12, 2 / 3, 5 / 12, 1 / 12, -1 / 3)
        self.assertEqual(m, res)

    def test_matrix_vector_transformation(self):
        m = Matrix(1, 0, 0, 0, 0, -1, 0, 1, 0)
        v = Vector(0, 1, 0)
        v = m * v
        self.assertEqual(v, Vector(0, 0, 1))


if __name__ == '__main__':
    unittest.main()
