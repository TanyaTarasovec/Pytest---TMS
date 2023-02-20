import unittest
from triangle import Triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.first = Triangle(9, 8, 7)

    def tearDown(self) -> None:
        del self.first

    def test_triangle_eq(self):
        second = Triangle(7, 8, 9)
        self.assertEqual(self.first, second)

    def test_triangle_ne(self):
        second = Triangle(6, 8, 4)
        self.assertNotEquals(self.first, second)

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 24)

    def test_triangle_exist(self):
        assert Triangle._check_if_exist(self, 7, 8, 9)

    def test_triangle_lt(self):
        second = Triangle(10, 17, 20)
        self.assertLess(self.first, second)

    def test_triangle_gt(self):
        second = Triangle(5, 6, 7)
        self.assertGreater(self.first, second)

    def test_triangle_le(self):
        second = Triangle(9, 8, 7)
        self.assertLessEqual(self.first, second)

    def test_triangle_ge(self):
        second = Triangle(9, 8, 7)
        self.assertGreaterEqual(self.first, second)

