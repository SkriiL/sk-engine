import unittest

import maths


class QuaternionTest(unittest.TestCase):
    def test_add(self):
        q1 = maths.Quaternion(0, maths.Vector(1, 0, 0))
        q2 = maths.Quaternion(90, maths.Vector(0, 1, 0))
        res = maths.Quaternion(90, maths.Vector(1, 1, 0))
        self.assertEqual(q1 + q2, res)
        q1 += q2
        self.assertEqual(q1, res)

    def test_sub(self):
        q1 = maths.Quaternion(90, maths.Vector(1, 0, 0))
        q2 = maths.Quaternion(90, maths.Vector(1, 0, 0))
        res = maths.Quaternion(0, maths.Vector(0, 0, 0))
        self.assertEqual(q1 - q2, res)
        q1 -= q2
        self.assertEqual(q1, res)

    def test_scalar_multiplication(self):
        q = maths.Quaternion(90, maths.Vector(1, 0, 0))
        res = maths.Quaternion(180, maths.Vector(2, 0, 0))
        self.assertEqual(q * 2, res)
        q *= 2
        self.assertEqual(q, res)

    def test_scalar_division(self):
        q = maths.Quaternion(180, maths.Vector(2, 0, 0))
        res = maths.Quaternion(90, maths.Vector(1, 0, 0))
        self.assertEqual(q / 2, res)
        q /= 2
        self.assertEqual(q, res)

    def test_quaternion_multiplication(self):
        q1 = maths.Quaternion(90, maths.Vector(1, 0, 0))
        q2 = maths.Quaternion(90, maths.Vector(0, 1, 0))
        res = maths.Quaternion(8100, maths.Vector(90, 90, 1))
        self.assertEqual(q1 * q2, res)
        q1 *= q2
        self.assertEqual(q1, res)

    def test_norm(self):
        q = maths.Quaternion(4, maths.Vector(3, 0, 0))
        self.assertEqual(abs(q), 5)

    def test_normalize(self):
        q = maths.Quaternion(4, maths.Vector(3, 0, 0))
        res = maths.Quaternion(4/5, maths.Vector(3/5, 0, 0))
        self.assertEqual(q.normalize(), res)

    def test_conjugate(self):
        q = maths.Quaternion(90, maths.Vector(1, 0, 0))
        res = maths.Quaternion(90, maths.Vector(-1, 0, 0))
        self.assertEqual(q.conjugate(), res)

    def test_inverse(self):
        q = maths.Quaternion(1, maths.Vector(1, 1, 1))
        res = maths.Quaternion(0.25, maths.Vector(-0.25, -0.25, -0.25))
        self.assertEqual(q.inverse(), res)

    def test_rotate_vector(self):
        v = maths.Vector(0, 1, 0)
        q = maths.Quaternion(90, maths.Vector(1, 0, 0))
        res = maths.Vector(0, 0, 1)
        self.assertEqual(q.rotate_vector(v), res)


if __name__ == '__main__':
    unittest.main()
