import pytest
from triangle import Triangle


@pytest.fixture()
def triangle_best():
    print("Hello")
    triangle = Triangle(10, 8, 14)
    yield triangle
    print("Hi")
    del triangle


@pytest.fixture()
def printer():
    print("Set")
    yield
    print("Ter")

    def test_triangle_eq(triangle_best, printer):
        first = triangle_best
        second = Triangle(10, 10, 10)
        assert first == second

    class TestTriangle:
        def test_triangle_eq(self, printer):
            first = triangle_best
            assert first.is_right_triangle()


        def test_triangle_lt(self, printer):
            first = triangle_best
            second = Triangle(10, 17, 20)
            assert self.first < second

@pytest.mark.skip
def test_triangle_perimetr(self, printer):
    self.assertEqual(self.first.perimetr(), 24)
