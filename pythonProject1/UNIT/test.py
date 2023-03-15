from triangle import Triangle
import unittest

class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(9, 8, 7)


    def test_triangle_eq(self):
        second = Triangle(7, 9, 8)
        self.assertEqual(self.first, second)


    def test_triangle_ne(self):
        second = Triangle(4, 5, 6)
        self.assertNotEquals(self.first, second)

    def test_perimetr(self):
        self.assertEqual(self.first.perimetr(), 24)